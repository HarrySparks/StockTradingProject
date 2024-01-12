from stock import Stock
from graph import GraphDrawer

from tkinter import *
import yfinance as yf
import math


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
    text = "current price : " + str(math.trunc(stock.price(inputstock.get())*100)/100)

    if len(inputdate.get()) != 0:
        dateentry = inputdate.get()
        year, month, day = map(str, dateentry.split('-'))
        collectivedate = str(year)+"/"+str(month)+"/"+str(day)
        text += "\n" + collectivedate + " price : "+ str(math.trunc(stock.pricedate(year,month,day,inputstock.get())*100)/100)

    displaylabel.config(text=text)

def GetStockGraph():
    ShowStockPrice()
    for widget in graphframe.winfo_children():
        widget.destroy()
    stockData = stock.range(inputrange0.get(),inputrange1.get(),inputstock.get())
    graphDrawer.DisplayGraph(inputstock.get(),stockData,graphframe)

mainframe = Frame(window)
graphframe = Frame(window, height=600) 
#need to make graph larger

stocklabel = Label(mainframe, text="Enter Stock Ticker:")
stocklabel.pack()
inputstock = Entry(mainframe, width=35, bg=colour6)
inputstock.pack(pady = 5)

datelabel = Label(mainframe, text="Enter Stock Date:")
datelabel.pack()
inputdate = Entry(mainframe, width=35, bg=colour6)
inputdate.pack(pady = 5)

displaylabel = Label(mainframe, text="", bg=colour6) 
displaylabel.pack()

getDataButton = Button(mainframe, text="Get Data", command=GetStockGraph, width=40, height=5, bg=colour5)
getDataButton.pack(pady=10, padx=10)

labelrange0 = Label(mainframe, text="Enter start range:")
labelrange0.pack()
inputrange0 = Entry(mainframe, width=35, bg=colour6)
inputrange0.pack(pady = 5)

labelrange1 = Label(mainframe, text="Enter end range:")
labelrange1.pack()
inputrange1 = Entry(mainframe, width=35, bg=colour6)
inputrange1.pack(pady = 5)

mainframe.pack()
graphframe.pack()

window.mainloop()