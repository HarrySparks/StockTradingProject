from stock import Stock
from tkinter import *
import yfinance as yf
import math
from graph import GraphDrawer

stock = Stock()
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

def ShowStockPrice():
    dateentry = inputdate.get()
    year, month, day = map(str, dateentry.split('-'))
    collectivedate = str(year)+"/"+str(month)+"/"+str(day)

    text = "current price : " + str(math.trunc(stock.getstockprice(inputstock.get())*100)/100) + "\n" + collectivedate + " price : "+ str(math.trunc(stock.getstockpricedate(year,month,day,inputstock.get())*100)/100)

    displaylabel.config(text=text)

def ShowStockPriceDate():
    dateentry = inputdate.get()
    year, month, day = map(str, dateentry.split('-'))
    
    collectivedate=str(year)+" : "+str(month)+" : "+str(day)+" | "
    displaylabel.config(text=collectivedate+str(math.trunc(stock.getstockpricedate(year,month,day,inputstock.get())*100)/100))

def GetStockDataForSymbol():
    for widget in graphframe.winfo_children():
        widget.destroy()
    stockData = stock.getstockpricedatayear(inputstock.get())
    graphDrawer.showGraphForDataFrame(inputstock.get(),stockData,graphframe)

mainframe = Frame(window)
graphframe = Frame(window, height=600) 
#need to make graph larger

label = Label(mainframe, text="Enter Stock Ticker:")
label.pack(side=TOP)

inputstock = Entry(mainframe, width=35, bg=colour6)
inputstock.pack(pady = 5, side=TOP)

datelabel = Label(mainframe, text="Enter Stock Date:")
datelabel.pack(side=TOP)

inputdate = Entry(mainframe, width=35, bg=colour6)
inputdate.pack(pady = 5, side=TOP)

displaylabel = Label(mainframe, text="", bg=colour6) 
displaylabel.pack()

getDataButton = Button(mainframe, text="Get Data", command=GetStockDataForSymbol, width=40, height=5, bg=colour5)
getDataButton.pack(pady=10, padx=10, side=LEFT)

getStockPriceDate = Button(mainframe, text="Get Stock Price At Date",command=ShowStockPriceDate, width=40, height=5, bg=colour5)
getStockPriceDate.pack(pady=10, padx=10, side=RIGHT)

getStockPrice = Button(mainframe, text="Get Stock Price",command=ShowStockPrice, width=40, height=5, bg=colour5)
getStockPrice.pack(pady=10, padx=10, side=RIGHT)

mainframe.pack()
graphframe.pack()

window.mainloop()