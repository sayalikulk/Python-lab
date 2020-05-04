from math import *

def printPrime(m,n):
    for i in range(m,n+1):
        c=0
        for j in range(2,i):
            if(i%j==0):
                c=1
                break
            else:
                continue
        if(c==1):
            continue
        else:
            print(i,end=" ")



m=int(input("Enter first number:"))
n=int(input("Enter second number:"))
printPrime(m,n)
