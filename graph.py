import matplotlib.pyplot as plt
import numpy as np

from stock import Stock

example = Stock("MSFT")

x = np.linspace(0, 28, 28, True, False, int)

#print(example.getstockpricedate(2023,9,x) )
y = np.sin(x) 


fig, ax = plt.subplots()
ax.plot(x, y)
plt.show()