using System;
using System.Collections.Concurrent;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Security.Principal;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using QuickFix;
using QuickFix.Transport;
using static FIXAcceptor.MyQuickFixApp;
namespace FIXAcceptor
{
    public partial class Form1 : Form
    {
        public MyQuickFixApp _MyQuickFixApp;
        public object _myDataGridViewLocker = new object();
        public ThreadedSocketAcceptor _MySocketAcceptor;
        public int _MyRowIndex = 0;
        
        public void FixOrdReceived(FIXOrders fixOrd)
        {
            // 更新 UI 要用 Invoke，避免跨執行緒問題
            if (InvokeRequired)
            {
                Invoke(new Action(() => FixOrdReceived(fixOrd)));
                return;
            }

            lock (_myDataGridViewLocker)
            {
                _MyQuickFixApp._CDFIXOrds.TryAdd(_MyRowIndex, fixOrd);
                _MyRowIndex++;
                dataGridView1.RowCount = _MyRowIndex;
            }
        }
       
        public Form1()
        {
            InitializeComponent();
            // 初始化 QuickFIX App (IApplication 實作)
            _MyQuickFixApp = new MyQuickFixApp();
            // 載入設定檔
            SessionSettings settings = new SessionSettings("acceptor.cfg");
            FileStoreFactory storeFactory = new FileStoreFactory(settings);
            ScreenLogFactory logFactory = new ScreenLogFactory(settings);
            // 建立 Acceptor，傳入 _MyQuickFixApp
            _MySocketAcceptor = new ThreadedSocketAcceptor(_MyQuickFixApp, storeFactory, settings, logFactory);
            // 啟動 Acceptor，保持開放
            _MySocketAcceptor.Start();
            // 訂閱事件
            _MyQuickFixApp.OnOrderReceived += FixOrdReceived;
            _MyQuickFixApp.OnFixMessageReceived += ShowFixMessage;
            _MyQuickFixApp.OnFixMessageSent += ShowFixMessage;
            // 初始化 DataGridView 欄位
            InitializeDGV();
        }
        private void ShowFixMessage(string msg)
        {
            // 避免跨執行緒問題，用 Invoke 更新 UI
            if (InvokeRequired)
            {
                Invoke(new Action(() => ShowFixMessage(msg)));
                return;
            }

            // 把訊息加到 TextBox
            textBox1.AppendText(msg + Environment.NewLine);
        }
        public void InitializeDGV()
        {
            string columns = "PrivateID,OrderID,OrdStatus,ClOrdID,OrigClOrdID,ExecID,ExecRefID,Account,Symbol,Side,CashOrderQty,OrderQty,Price,OrdType,HandlInst,TimeInForce,SecurityExchange,SecurityID,ExecInst,Currency,AvgPx,CumQty,CumAmt,NoteText,SecurityType,TradeDate,ExpireDate,ExpireTime";
            string[] column_array = columns.Split(',');
            foreach (string col in column_array)
            {
                dataGridView1.Columns.Add(string.Format("Sell_col_{0}", col), col);
            }
            dataGridView1.AutoGenerateColumns = false;
        }
        private void dataGridView1_CellValueNeeded(object sender, DataGridViewCellValueEventArgs e)
        {
            // 檢查資料來源
            if (_MyQuickFixApp == null) { return; }
            if (!_MyQuickFixApp._CDFIXOrds.ContainsKey(e.RowIndex)) { return; }

            // lock 確保執行緒安全
            lock (_myDataGridViewLocker)
            {
                var ord = _MyQuickFixApp._CDFIXOrds[e.RowIndex];

                switch (dataGridView1.Columns[e.ColumnIndex].HeaderText)
                {
                    case "PrivateID": e.Value = ord.PrivateID; break;
                    case "OrderID": e.Value = ord.OrderID; break;
                    case "ClOrdID": e.Value = ord.ClOrdID; break;
                    case "OrigClOrdID": e.Value = ord.OrigClOrdID; break;
                    case "ExecID": e.Value = ord.ExecID; break;
                    case "ExecRefID": e.Value = ord.ExecRefID; break;
                    case "Account": e.Value = ord.Account; break;
                    case "Symbol": e.Value = ord.Symbol; break;
                    case "Side": e.Value = ord.Side; break;
                    case "OrderQty": e.Value = ord.OrderQty; break;
                    case "Price": e.Value = ord.Price; break;
                    case "OrdType": e.Value = ord.OrdType; break;
                    case "HandlInst": e.Value = ord.HandlInst; break;
                    case "OrdStatus": e.Value = ord.OrdStatus; break;
                    case "TimeInForce": e.Value = ord.TimeInForce; break;
                    case "SecurityExchange": e.Value = ord.SecurityExchange; break;
                    case "Currency": e.Value = ord.Currency; break;
                    case "AvgPx": e.Value = ord.AvgPx; break;
                    case "CumQty": e.Value = ord.CumQty; break;
                    case "CumAmt": e.Value = ord.CumAmt; break;
                    case "NoteText": e.Value = ord.NoteText; break;
                    case "TradeDate": e.Value = ord.TradeDate; break;
                    case "ExecInst": e.Value = ord.ExecInst; break;
                    case "ExpireTime": e.Value = ord.ExpireTime; break;
                    case "ExpireDate": e.Value = ord.ExpireDate; break;
                    case "CashOrderQty": e.Value = ord.CashOrderQty; break;
                    case "SecurityType": e.Value = ord.SecurityType; break;
                    case "SecurityID": e.Value = ord.SecurityID; break; // 原本寫 sessionID 應該是錯誤
                    default: break;
                }
            }
        }
    }
}
