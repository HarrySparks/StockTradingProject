import matplotlib.pyplot as plt
import numpy as np
import yfinance as yf
import pandas as pd 
from tkinter import *
from stock import Stock
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class GraphDrawer:
    #this accepts teh data and then draws the graph adds to the grpahframe
    def DisplayGraph(self,stock_name,stock_history, graphFrame):
        for widget in graphFrame.winfo_children():
            widget.destroy()
        # Plotting
        fig, ax = plt.subplots(facecolor=("#BBBBEE"))
        
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

        canvas.draw()