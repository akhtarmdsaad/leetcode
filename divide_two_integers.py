# Given two integers dividend and divisor, divide two integers without using multiplication, division, and mod operator.
import math

def solve(dividend,divisor):
    if (dividend < 0 and divisor < 0) or (dividend >= 0 and divisor >= 0):
        factor_neg = 1
    else:
        factor_neg = -1
    dividend = abs(dividend)
    divisor = abs(divisor)
    q = 0
    print("To Solve:",dividend,'/',divisor)
    while dividend >= divisor:
        factor = 2
        n = divisor
        while dividend > n*2:
            n *= 2
            q += factor
            factor *= 2
            dividend -= n 
            
        print("After 2x:",dividend,divisor,q)
        if(dividend >= divisor):
            dividend -= divisor 
            q+=1
    
    return q*factor_neg

a = 7
b = -3
print(solve(a,b))
