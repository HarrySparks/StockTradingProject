from stock import Stock
from tkinter import *
import yfinance as yf
import math
from graph import GraphDrawer

stock1 = Stock()
graphDrawer = GraphDrawer()

colour1="#0A141B"
colour2="#0C1821"
colour3="#1B2A41"
colour4="#324A5F"
colour5="#7F8A9E"
colour6="#CCC9DC"

window = Tk()
window.geometry("900x900")
window.config(padx=50, pady=10, bg=colour3)
window.resizable(True, True)

def onclick():
    #dont' create a new displaylable every time just configure it with the stock data
    displaylabel.config(text=math.trunc(stock1.getstockprice(inputstock.get())*100)/100)

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
graphframe = Frame(window, height=600)

#create entry field and label
label = Label(mainframe, text="Enter Stock Ticker:")
label.pack()

inputstock = Entry(mainframe, width=35, bg=colour6)
inputstock.pack(pady = 5)

#create the display lable once...
displaylabel = Label(mainframe, text="", bg=colour6) 
displaylabel.pack()

#create button for getting stock data for a period of time
getDataButton = Button(mainframe, text="Get Data", command=GetStockDataForSymbol, width=40, height=5, bg=colour5)
getDataButton.pack(pady=10, padx=10, side=LEFT)

#create button for getting stockprice
getStockPrice = Button(mainframe, text="Get Stock Price",command=onclick, width=40, height=5, bg=colour5)
getStockPrice.pack(pady=10, padx=10, side=RIGHT)

mainframe.pack()
graphframe.pack()

window.mainloop()