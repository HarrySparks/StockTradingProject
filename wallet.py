import numpy as np

class Wallet:
    balance = 100_000
    ownedstocks = ([])

    def BuyStock(self, stockname, price):
        print(self.ownedstocks)

        self.balance -= price
        print(self.balance)

        for i in range(len(self.ownedstocks)):
            if self.ownedstocks[i][0] == stockname:                    
                self.ownedstocks[i][1] += 1
                print(self.ownedstocks)
                return
            
        self.ownedstocks.append([stockname,1])
        print(self.ownedstocks)

    def SellStock(self, stockname, price):
        for i in range(len(self.ownedstocks)):
            if self.ownedstocks[i][0] == stockname and self.ownedstocks[i][1] > 0:
                self.ownedstocks[i][1] -= 1
                self.balance += price
                print(self.balance)
                print(self.ownedstocks)
                return
            
    def GetOwnedStocks(self):
        ownedstocksstring = ""
        for i in range(len(self.ownedstocks)):
            if self.ownedstocks[i][1] != 0:
                ownedstocksstring += str(self.ownedstocks[i][0])
        print(ownedstocksstring)
        return ownedstocksstring

