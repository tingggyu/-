using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using QuickFix;

namespace FIXAcceptor
{
    public class FIXOrders
    {
        public FIXOrders()
        {
            PrivateID = string.Empty;
            OrderID = string.Empty;
            ClOrdID = string.Empty;
            OrigClOrdID = string.Empty;
            ExecID = string.Empty;
            ExecRefID = string.Empty;
            IDSource = string.Empty;
            SecurityID = string.Empty;
            RequestClOrdID = string.Empty;
            PendingClOrdID = string.Empty;
            HandlInst = string.Empty;
            OrdStatus = string.Empty;
            SecurityExchange = string.Empty;
            Currency = string.Empty;
            TimeInForce = string.Empty;
            PositionEffect = string.Empty;
            SecurityType = string.Empty;
            Symbol = string.Empty;
            Side = string.Empty;
            PutOrCall = -1;
            MaturityMonthYear = string.Empty;
            StrikePrice = string.Empty;
            OrdType = string.Empty;
            Price = 0.0m;
            PendingPrice = 0.0m;
            StopPx = 0.0m;
            DayAvgPx = 0.0m;
            OrderQty = 0m;
            CumQty = 0m;
            LeavesQty = 0m;
            PendingQty = 0m;
            DayOrderQty = 0m;
            DayCumQty = 0m;
            DayCumAmt = 0.0m;
            CumAmt = 0.0m;
            CashOrderQty = 0.0m;
            NoteText = string.Empty;
            TradeDate = string.Empty;
            Account = string.Empty;
            ExecInst = string.Empty;
            ExpireDate = string.Empty;
            ExpireTime = string.Empty;
            CashOrderQty = 0.0m;
        }
        public SessionID sessionID { get; set; }
        public string sessionKey { get; set; }
        public string PrivateID { get; set; }
        public string BeginString { get; set; }
        public string OrderID { get; set; }
        public string ClOrdID { get; set; }
        public string OrigClOrdID { get; set; }
        public string ExecID { get; set; }
        public string ExecRefID { get; set; }
        public string IDSource { get; set; }
        public string SecurityID { get; set; }
        public string RequestClOrdID { get; set; }
        public string PendingClOrdID { get; set; }
        public string HandlInst { get; set; }
        public string OrdStatus { get; set; }
        public string SecurityExchange { get; set; }
        public string Currency { get; set; }
        public string TimeInForce { get; set; }
        public string PositionEffect { get; set; }
        public string SecurityType { get; set; }
        public string Symbol { get; set; }
        public string Side { get; set; }
        public int PutOrCall { get; set; }
        public string MaturityMonthYear { get; set; }
        public string StrikePrice { get; set; }
        public string OrdType { get; set; }
        public decimal Price { get; set; }
        public decimal PendingPrice { get; set; }
        public decimal StopPx { get; set; }
        public decimal AvgPx { get; set; }
        public decimal DayAvgPx { get; set; }
        public decimal OrderQty { get; set; }
        public decimal CumQty { get; set; }
        public decimal LeavesQty { get; set; }
        public decimal PendingQty { get; set; }
        public decimal DayOrderQty { get; set; }
        public decimal DayCumQty { get; set; }
        public decimal DayCumAmt { get; set; }
        public decimal CumAmt { get; set; }
        public decimal CashOrderQty { get; set; }
        public string NoteText { get; set; }
        public string TradeDate { get; set; }
        public string Account { get; set; }
        public string ExecInst { get; set; }
        public string ExpireTime { get; set; }
        public string ExpireDate { get; set; }

        public object objLocker = new object();
    }
}
