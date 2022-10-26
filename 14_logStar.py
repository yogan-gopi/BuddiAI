#14_logStar.py 

import math
def logstar_2(x):
    if x == 1:
        return 1
    return 1 + logstar_2(math.log2(x))

if __name__ == '__main__':
    x = 8
    print("Log *2({}) = {}".format(x, logstar_2(x)))