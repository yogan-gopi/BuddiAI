#4_exponent.py

def exp(x):
    res = 1
    pow = 1
    fact = 1
    for i in range(1, 10):
        fact *= i
        pow *= x
        res += ((pow)/fact)
    return res
    

if __name__ == '__main__':
    x = 5
    print("The Exponent value of x = {} is {}".format(x, exp(x)))