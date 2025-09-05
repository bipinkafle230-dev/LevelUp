'''
Factorial of the number 
what is factorial that if n=3 i.e. factorial of 3=3*2*1=6
now...'''

def main():
    Factorial()
def Factorial():
    n=int(input("Enter a number:"))
    if n==0 and n==1:
        print("Factorial of",n,"is 1")
    elif n<0:
        print("Factorial does not exist for negative numbers")
    else:
        fact=0
        for i in range (2, n):
            fact=n*i
            n=fact
        print("Factorial is",fact)
main()