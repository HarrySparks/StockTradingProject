import yfinance as yf

class Stock:
    def __init__(self,name):
        self.name = name

    def printname(self):
        print(self.name)
    
    def getstockprice(self):
        stockprice = yf.Ticker(self.name).history(period="1d")
        return stockprice['Close'][0]

    def getstockpricedate(self, yr, mth, day):
        date = str(yr)+"-"+str(mth)+"-"+str(day)
        stockprice = yf.Ticker(self.name).history(start=date, period="1d")
        return stockprice['Close'][0]

    pass