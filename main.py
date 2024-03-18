from stock import Stock
from graph import GraphDrawer
from wallet import Wallet

from tkinter import *
import yfinance as yf
import math

stock = Stock()
graphDrawer = GraphDrawer()
wallet = Wallet()

colour1="#0A141B"
colour2="#0C1821"
colour3="#1B2A41"
colour4="#324A5F"
colour5="#7F8A9E"
colour6="#CCC9DC"

cgreen="#00FF00"

window = Tk()
window.geometry("900x900")
window.config(padx=50, pady=10, bg=colour3)
window.resizable(True, True)

def CloseWindow():
    window.destroy()

window.protocol("WM_DELETE_WINDOW", CloseWindow)

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
graphframe = Frame(window) 

stocklabel = Label(mainframe, text="Enter Stock Ticker:")
stocklabel.grid(column = 1, row = 0)

inputstock = Entry(mainframe, width=35, bg=colour6)
inputstock.grid(column = 1, row = 1)

datelabel = Label(mainframe, text="Enter Stock Date:")
datelabel.grid(column = 1, row = 3)

inputdate = Entry(mainframe, width=35, bg=colour6)
inputdate.grid(column = 1, row = 4)

buybutton = Button(mainframe, text="Buy", width=35, command=lambda:wallet.BuyStock(inputstock.get(),stock.price(inputstock.get())), bg=cgreen)
buybutton.grid(column = 2, row = 1, rowspan = 1)

sellbutton = Button(mainframe, text="Sell", width=35, command=lambda:wallet.SellStock(inputstock.get(),stock.price(inputstock.get())), bg=cgreen)
sellbutton.grid(column = 2, row = 2, rowspan = 1)

getdatabutton = Button(mainframe, text="Get Data", command=GetStockGraph, width=35, bg=colour5)
getdatabutton.grid(column = 2, row = 4, rowspan = 1)

labelrange0 = Label(mainframe, text="Enter start range:")
labelrange0.grid(column = 3, row = 0)
inputrange0 = Entry(mainframe, width=35, bg=colour6)
inputrange0.grid(column = 3, row = 1)

labelrange1 = Label(mainframe, text="Enter end range:")
labelrange1.grid(column = 3, row = 3)
inputrange1 = Entry(mainframe, width=35, bg=colour6)
inputrange1.grid(column = 3, row = 4)

displaylabel = Label(mainframe, text="", bg=colour6) 
displaylabel.grid(column = 2, row = 5)

mainframe.place(relx=0.5, rely=0.1, anchor=CENTER)
graphframe.place(relx=0.5, rely=1, anchor=S)

window.grid_rowconfigure(2, minsize=10) #creates a gap at row 2 of space 10
window.grid_rowconfigure(6, minsize=30)

window.mainloop()
