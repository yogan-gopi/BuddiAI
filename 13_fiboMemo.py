#13_fiboMemo.py

def fiboMemo(n):
    if n in memo:
        return memo[n]
    res = fiboMemo(n-1)+fiboMemo(n-2)
    memo[n] = res
    return res

if __name__ == "__main__":
    memo = {0:0, 1:1}
    print("The first 10 Fibonacci numbers: ")
    for i in range(10):
        print(fiboMemo(i), end = "  ")