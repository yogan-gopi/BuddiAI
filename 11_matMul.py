#11_matMul

import copy

def getMatrix(n):
    mat = []
    for i in range(n):
        print("Enter row - {}: ".format(i+1), end = "")
        arr = list(map(int, input().split()))
        mat.append(arr)
    return mat

def mulMat(A, k):
    for i in range(len(A)):
        for j in range(len(A[i])):
            
            A[i][j] *= k 
    return A


def printMat(arr):
    print('\n'.join([' '.join([str(cell) for cell in row]) for row in arr]))

if __name__ == "__main__":
    n = int(input("Enter 'n' order of the Matrix-A: "))
    A = getMatrix(n)
    k = int(input("Enter 'k': "))
    Temp = copy.deepcopy(A)
    res = mulMat(Temp, k)
    print("The Resultant Matrix of 'A x kI' is ")
    printMat(res)
    
