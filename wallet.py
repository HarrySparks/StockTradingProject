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

        try:
            self.ownedstocks.append([stockname,1])
            print("nromal")
        except:
            np.append(self.ownedstocks, [stockname,1]) # whne deleting the array the array is transformed to  a np array 
            print("except")
        print(self.ownedstocks)

    def SellStock(self, stockname, price):
        for i in range(len(self.ownedstocks)):
            if self.ownedstocks[i][0] == stockname:
                self.ownedstocks[i][1] -= 1
                self.balance += price
                print(self.balance)
                print(self.ownedstocks)

                if self.ownedstocks[i][1] <= 0:
                    #self.ownedstocks[0].pop()
                    #self.ownedstocks[0].pop()
                    print(self.balance)
                    print(self.ownedstocks)
                    self.ownedstocks = np.delete(self.ownedstocks, 0, axis=0)
                    print(self.balance)
                    print(self.ownedstocks)
                return

        self.ownedstocks.append([stockname,1])
        print(self.ownedstocks)