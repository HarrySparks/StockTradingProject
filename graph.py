import matplotlib.pyplot as plt
import numpy as np
import yfinance as yf
import pandas as pd 
from tkinter import *
from stock import Stock
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class GraphDrawer:
    #READ THIS TO UNDERSTAND HOW TO MANIPULATE DATA FRAMES RETURNED, WORKS WITH COLUMNS AND INDEXES
    def exampleOfHowToDealWithDataFrames(self):
        msft = yf.Ticker("TSLA")
        stock_history = msft.history(start="2021-01-01", end="2021-12-31")
        #this gets the index of the dataframe or table
        print(stock_history.index)
        #this gets all the columns of the dataframe or table  ['Open', 'High', 'Low', 'Close', 'Volume', 'Dividends', 'Stock Splits']
        print(stock_history.columns)
        #this gets the column high
        print(stock_history['High'])
        #this will get the specific value at that row for that column
        print(stock_history.loc['2021-01-04 00:00:00-05:00', 'High'])

    #this accepts teh data and then draws the graph adds to the grpahframe
    def DisplayGraph(self,stock_name,stock_history, graphFrame):
        for widget in graphFrame.winfo_children():
            widget.destroy()
        # Plotting
        fig, ax = plt.subplots(facecolor=("#BBBBEE"), layout='tight', linewidth=0.0)
        
        ax.plot(stock_history.index, stock_history['Close'], label='Close')

        # Formatting the plot        
        ax.set_title(stock_name.upper() + ' Price At Close',color="#000000")
        ax.set_xlabel('Date',color="#000000")
        ax.set_ylabel('Price',color="#000000")

        ax.grid()
        plt.xticks(rotation=15)  # Rotate date labels for better readability
        plt.legend()

        # Create a FigureCanvasTkAgg object and attach the figure (fig) to it to the graphframe
        canvas = FigureCanvasTkAgg(fig, master=graphFrame)
            
        # Get the Tkinter widget from the canvas and pack it into the frame
        canvas_widget = canvas.get_tk_widget()
        canvas_widget.pack()

        #need to remove previous graph before displaying new one

        # Draw the canvas
        canvas.draw()