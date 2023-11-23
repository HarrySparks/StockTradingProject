from stock import Stock
from tkinter import *
import yfinance as yf
from graph import GraphDrawer

stock1 = Stock()
graphDrawer = GraphDrawer()

colour1 = "#053B50"
colour2 = "#176B87"
colour3 = "#64CCC5"

window = Tk()
window.geometry("900x900")
window.config(padx=50, pady=10, bg=colour1)
window.resizable(True, True)

def onclick():
    #dont' create a new displaylable every time just configure it with the stock data
    displaylabel.config(text=stock1.getstockprice(inputstock.get()))

#this si called when we press get stock data button
def GetStockDataForSymbol():
    for widget in graphframe.winfo_children():
        widget.destroy()
    #gets the symbol TSLA from the inputstock entry field passes as parameter
    stockData = stock1.getStockPriceDataForPeriod(inputstock.get())
    #calls our graph drawer class and pass it the frame and data, the graph is added to our graph frmae
    graphDrawer.showGraphForDataFrame(inputstock.get(),stockData,graphframe)

#create frames
mainframe = Frame(window)
graphframe = Frame(window)

#create entry field and label
label = Label(mainframe, text="Enter Stock Ticker:")
label.pack()
inputstock = Entry(mainframe, width=35, bg=colour2)
inputstock.pack(pady = 5)

#create button for getting stock data for a period of time
get_data_button = Button(mainframe, text="Get Data", command=GetStockDataForSymbol, width=40, height=5, bg=colour3)
get_data_button.pack(pady = 10)

#create button for getting stockprice
getStockPrice = Button(mainframe, text="Get Stock Price",command=onclick, width=40, height=5, bg=colour3)
getStockPrice.pack(pady = 10)

#create the display lable once...
displaylabel = Label(mainframe, bg=colour1, text="") 
displaylabel.pack()

mainframe.pack()
graphframe.pack()

window.mainloop()

"""
def getstockprice(stockname,stockdate):
    stock = yf.Ticker(stockname)
    stockprice = stock.history(start=stockdate, period="1d")
    return stockprice['Close'][0]

#msft.info, msft.capital_gains, msft.get_shares_full(start="2023-01-01", end=None), msft.balance_sheet

"""