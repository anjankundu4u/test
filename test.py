import ctypes
from kite_trade import *

def Msgbox(title, text, style):
        return ctypes.windll.user32.MessageBoxW(0, text, title, style)

global Token
Token = "8TxMnrIbnXePLnDVSn0/aOukYDAHXmEMyznXoq3/OeeNmwfm6Ab4bVd9xHrSqTX9MCjXRiXfDPQMOPCs9Wr7owZADDBnouA64+RI8FedbjNiX+HAhr3nRQ=="
try:
    kite = KiteApp(enctoken=Token)
except:
    Msgbox('myPegasus :: Kite Error', 'Kite Connection Failed! Please set token in [mySettings.json] file', 0)
    exit()

tradingSymbol = "SBIN"
Qty = 1
Price = 0
kite.place_order(tradingsymbol=tradingSymbol, exchange=kite.EXCHANGE_NSE, transaction_type=kite.TRANSACTION_TYPE_BUY, quantity=Qty, price=Price, variety=kite.VARIETY_REGULAR, order_type=kite.ORDER_TYPE_MARKET, product=kite.PRODUCT_MIS )