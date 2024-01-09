import yfinance as yf

class Stock:
    def getstockprice(self,symbol):
        stockprice = yf.Ticker(symbol.upper()).history(period="1d")
        return stockprice['Close'][0]

    def getstockpricedate(self, yr, mth, day,symbol):
        date = str(yr)+"-"+str(mth)+"-"+str(day)
        stockprice = yf.Ticker(symbol.upper()).history(start=date, period="1d")
        return stockprice['Close'][0]

    #get stock data for a symbol for a period of time and return the data frame
    def getstockpricedatayear(self,symbol):
        msft = yf.Ticker(symbol.upper())
        #these dates could be passed as parameters... fogure out how to

        #stock_history = msft.history(start="2022-01-01", end="2023-10-31")  
        
        stock_history = msft.history(start="1985-01-01", end="2023-12-30")  
        return stock_history

    def getstockpricesindaterange(self):
        pass