

class Wallet:
    balance = 100_000
    ownedstocks = ([])

    def BuyStock(self, stockname, price):
        self.balance -= price
        print(self.balance)

        for i in range(len(self.ownedstocks)):
            if self.ownedstocks[i][0] == stockname:
                self.ownedstocks[i][1] = self.ownedstocks[i][1] + 1
                print(self.ownedstocks)
                return
        self.ownedstocks.append([stockname,1])
        print(self.ownedstocks)