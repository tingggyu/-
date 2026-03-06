using System;
using System.Collections.Concurrent;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using QuickFix;

namespace FIXAcceptor
{
    public class MyQuickFixApp : MessageCracker, IApplication
    {
        public delegate void OnOrderReceivedHandler(string clOrdID,string account,string symbol,string side,string ordType,decimal qty,decimal? price);
        private SessionID _sessionID;
        public ConcurrentDictionary<int, FIXOrders> _CDFIXOrds = new ConcurrentDictionary<int, FIXOrders>();
        public event Action<FIXOrders> OnOrderReceived;
        public event Action<string> OnFixMessageReceived;
        public event Action<string> OnFixMessageSent;

        // QuickFIX 基本介面
        public void FromAdmin(Message message, SessionID sessionID) { }
        public void ToAdmin(Message message, SessionID sessionID) { }
        public void FromApp(Message message, SessionID sessionID) 
        { Crack(message, sessionID);
            if (message is QuickFix.FIX42.NewOrderSingle newOrder)
            {
                FIXOrders fixOrd = new FIXOrders
                {
                    sessionKey = sessionID.ToString(),
                    BeginString = sessionID.BeginString,
                    ClOrdID = newOrder.ClOrdID.Obj,
                    Account = newOrder.Account.Obj,
                    Symbol = newOrder.Symbol.Obj,
                    Side = newOrder.Side.Obj.ToString(),
                    OrdType = newOrder.OrdType.Obj.ToString(),
                    Price = newOrder.Price.Obj,
                    OrderQty = newOrder.OrderQty.Obj,
                    SecurityExchange = newOrder.SecurityExchange.Obj
                };

                // 觸發事件，把訂單傳給 UI
                OnOrderReceived?.Invoke(fixOrd);
            }
            // 收到 FIX 訊息
            string msg = message.ToString();
            OnFixMessageReceived?.Invoke("[RECV] " + msg);
        }
        public void ToApp(Message message, SessionID sessionID)
        {
            // 傳出去 FIX 訊息
            string msg = message.ToString();
            OnFixMessageSent?.Invoke("[SEND] " + msg);
        }
        public void OnCreate(SessionID sessionID) { _sessionID = sessionID; }
        public void OnLogon(SessionID sessionID) { }
        public void OnLogout(SessionID sessionID) { }

        // 收到新單 (Buy Side 傳來 NewOrderSingle)
        public void OnMessage(QuickFix.FIX42.NewOrderSingle msg, SessionID sessionID)
        {
            string clOrdID = msg.ClOrdID.getValue();
            string account = msg.IsSetAccount() ? msg.Account.getValue() : "";
            string symbol = msg.Symbol.getValue();
            string side = msg.Side.getValue() == QuickFix.Fields.Side.BUY ? "BUY" : "SELL";
            string ordType = msg.OrdType.getValue() == QuickFix.Fields.OrdType.LIMIT ? "LIMIT" : "MARKET";

            var orderQty = new QuickFix.Fields.OrderQty();
            msg.GetField(orderQty);
            decimal qty = orderQty.getValue();

            decimal? px = null;
            var price = new QuickFix.Fields.Price();
            if (msg.IsSetField(price))
            {
                msg.GetField(price);
                px = price.getValue();
            }
            // 立即回覆 ExecutionReport (NEW)
            SendNewAck(clOrdID, symbol, qty, px, msg.Side.getValue(), sessionID);

            // 模擬自動成交：延遲 2 秒送 FULL FILL
            Task.Delay(2000).ContinueWith(_ =>
            {
                SendFullFill(clOrdID, symbol, qty, px ?? 0, msg.Side.getValue(), sessionID);
            });
        }

        // NEW 回報
        private void SendNewAck(string clOrdID, string symbol, decimal qty, decimal? px, char side, SessionID sessionID)
        {
            var execReport = new QuickFix.FIX42.ExecutionReport(
                new QuickFix.Fields.OrderID(Guid.NewGuid().ToString("N")),             // 唯一 OrderID
                new QuickFix.Fields.ExecID(Guid.NewGuid().ToString("N")),              // 唯一 ExecID
                new QuickFix.Fields.ExecTransType(QuickFix.Fields.ExecTransType.NEW),  // FIX42 必填
                new QuickFix.Fields.ExecType(QuickFix.Fields.ExecType.NEW),            // 執行類型
                new QuickFix.Fields.OrdStatus(QuickFix.Fields.OrdStatus.NEW),          // 訂單狀態
                new QuickFix.Fields.Symbol(symbol),                                    // 商品代號
                new QuickFix.Fields.Side(side),                                        // 買賣方向
                new QuickFix.Fields.LeavesQty(qty),                                    // 剩餘數量
                new QuickFix.Fields.CumQty(0),                                         // 累計成交數量
                new QuickFix.Fields.AvgPx(0)                                           // 平均成交價
            );

            // 額外欄位
            execReport.SetField(new QuickFix.Fields.ClOrdID(clOrdID));
            execReport.SetField(new QuickFix.Fields.OrderQty(qty));
            if (px.HasValue) execReport.SetField(new QuickFix.Fields.Price(px.Value));

            // 發送給對方
            Session.SendToTarget(execReport, sessionID);
        }


        // FULL FILL 回報
        private void SendFullFill(string clOrdID, string symbol, decimal qty, decimal price, char side, SessionID sessionID)
        {
            var execReport = new QuickFix.FIX42.ExecutionReport(
                new QuickFix.Fields.OrderID(Guid.NewGuid().ToString("N")),             // 唯一 OrderID
                new QuickFix.Fields.ExecID(Guid.NewGuid().ToString("N")),              // 唯一 ExecID
                new QuickFix.Fields.ExecTransType(QuickFix.Fields.ExecTransType.NEW),  // FIX42 必填
                new QuickFix.Fields.ExecType(QuickFix.Fields.ExecType.FILL),           // 執行類型
                new QuickFix.Fields.OrdStatus(QuickFix.Fields.OrdStatus.FILLED),       // 訂單狀態
                new QuickFix.Fields.Symbol(symbol),                                    // 商品代號
                new QuickFix.Fields.Side(side),                                        // 買賣方向
                new QuickFix.Fields.LeavesQty(0),                                      // 剩餘數量
                new QuickFix.Fields.CumQty(qty),                                       // 累計成交數量
                new QuickFix.Fields.AvgPx(price)                                       // 平均成交價
            );

            // 額外欄位
            execReport.SetField(new QuickFix.Fields.ClOrdID(clOrdID));
            execReport.SetField(new QuickFix.Fields.OrderQty(qty));
            execReport.SetField(new QuickFix.Fields.Price(price));

            // 發送給對方
            Session.SendToTarget(execReport, sessionID);
        }
    }
}
