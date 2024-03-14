import yfinance as yf

class Stock:
    def price(self,symbol):
        stockprice = yf.Ticker(symbol.upper()).history(period="1d")
        return stockprice['Close'][0]

    def pricedate(self, yr, mth, day,symbol):
        date = str(yr)+"-"+str(mth)+"-"+str(day)
        stockprice = yf.Ticker(symbol.upper()).history(start=date, period="1d")
        return stockprice['Close'][0]

    #get stock data for a symbol for a period of time and return the data frame
    def range(self,range0,range1,symbol):
        stockticker = yf.Ticker(symbol.upper())

#use python date time

        if len(range0) != 0 and len(range1) != 0:
            stock_history = stockticker.history(start=range0, end=range1)  
            return stock_history

        stock_history = stockticker.history(start="1926-01-01", end="2023-12-30")  

        return stock_history

    def getstockpricesindaterange(self):
        pass