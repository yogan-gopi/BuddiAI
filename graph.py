import math

def printXY(x, y):
    print("X\t\tY")
    for i,j in zip(x,y):
        print("{}\t\t{}".format(i,j))

def calcY(x):
    a = 1.066751
    pow = x*0.9952467
    exp = math.exp(pow)
    b = 0.990193889*(1-exp)
    y = a - b
    return y

x = [-1, -0.8, -0.6, -0.4, -0.2, 0, 0.2, 0.4, 0.6, 0.8, 1]
y = []

for i in x:
    y.append(calcY(i))

printXY(x, y)