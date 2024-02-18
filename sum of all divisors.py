
def SumDivisors(x):
        "Sum of all divisor of n only"
        s = 0
        for i in range(1,x+1):
            if x%i == 0:
                s+=i 
        return s

def sumOfAllDivisors(n: int) -> int:
    # Write your code here
    
    sm = 0
    for i in range(1,n+1):
        sm += SumDivisors(i)
        print(i,sm)
    return sm

print(SumDivisors(1))

print("Ans:",sumOfAllDivisors(5))