from stock import Stock
from tkinter import *
import yfinance as yf

stock1 = Stock("MSFT")

colour1 = "#053B50"
colour2 = "#176B87"
colour3 = "#64CCC5"

window = Tk()
window.geometry("900x600")
window.config(padx=50, pady=50, bg=colour1)
window.resizable(True, True)


#inputdate = Entry(window, width=35, bg=colour2)
#inputdate.pack(pady = 5)
graphframe = Frame(window)
inputstock = Entry(graphframe, width=35, bg=colour2)
inputstock.pack(pady = 5)
def onclick():
    displaylabel = Label(graphframe, bg=colour1, text=stock1.getstockprice()) 
    displaylabel.pack()

button = Button(graphframe, command=onclick, width=40, height=5, bg=colour3)
button.pack(pady = 10)
graphframe.pack()

window.mainloop()

"""
def getstockprice(stockname,stockdate):
    stock = yf.Ticker(stockname)
    stockprice = stock.history(start=stockdate, period="1d")
    return stockprice['Close'][0]

#msft.info, msft.capital_gains, msft.get_shares_full(start="2023-01-01", end=None), msft.balance_sheet




"""