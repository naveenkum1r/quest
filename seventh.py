import math
import math as mt
import numpy as np

print("It's math! Ith has type {}".format(type(math)))
print(dir(math))
print("pi to 4 significant digits = {:.4}".format(math.pi))
print(math.log(32, 2))
print(mt.pi)
print("numpy.random is a ", type(np.random))
print("it contains names such as ...", dir(np.random)[-15:])
rolls = np.random.randint(low=1, high=6, size=10)
print(rolls)
print(rolls.mean())
print(rolls.tolist())
print(rolls + 10)
print(rolls <= 3)
xlist = [[1,2,3],[2,4,6],]
x = np.asarray(xlist)
print("xlist = {}\nx =\n{}".format(xlist, x))
print(x[1,-1])