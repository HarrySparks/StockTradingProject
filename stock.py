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
        msft = yf.Ticker(symbol.upper())
        #these dates could be passed as parameters... fogure out how to

        #stock_history = msft.history(start="2022-01-01", end="2023-10-31")  
        


        stock_history = msft.history(start=range0, end=range1)  
        return stock_history

    def getstockpricesindaterange(self):
        pass