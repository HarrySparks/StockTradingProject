import yfinance as yf

class Stock:
    
    def getstockprice(self,symbol):
        stockprice = yf.Ticker(symbol).history(period="1d")
        return stockprice['Close'][0]

    def getstockpricedate(self, yr, mth, day,symbol):
        date = str(yr)+"-"+str(mth)+"-"+str(day)
        stockprice = yf.Ticker(symbol).history(start=date, period="1d")
        return stockprice['Close'][0]

    #get stock data for a symbol for a period of time and return the data frame
    def getStockPriceDataForPeriod(self,symbol):
        msft = yf.Ticker(symbol)
        #these dates could be passed as parameters... fogure out how to
        stock_history = msft.history(start="2022-01-01", end="2023-10-31")  
        return stock_history

    def getstockpricesindaterange(self):
        pass