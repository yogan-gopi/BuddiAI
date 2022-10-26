#12_knapsack.py

class item:
    def __init__(self, weight, value):
        self.weight = weight
        self.value = value
        self.ratio = value/weight

def myFunc(e):
  return e.ratio

def solveKnapSack(items, W):    
    items.sort(reverse = True, key = myFunc)
    i = 0
    res = 0
    while W > 0 and i < len(items):
        if (W - items[i].weight) > 0:
            W = W - items[i].weight
            res += items[i].value
        else:
            res += (W/items[i].weight*items[i].value)
            break
        i += 1
    return res

def printItems(items):
    print("Values: ", end= '')
    for i in items:
        print(i.value, end= "\t")
    print()
    print("Weight: ", end= '')
    for i in items:
        print(i.weight, end= "\t")
    print()

if __name__ == '__main__':
    items = [item(10, 60), item(20, 100), item(30, 120)]
    W = 50
    printItems(items)
    res = solveKnapSack(items, W)
    print("Total Capacity: ", W)
    print("Final Maximum Profit: ", res)