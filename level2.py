#fibonacci number
''' let's say 
a=0, b=1 and c=?
c=a+b
a=b
b=c
'''
def main():
    Fibo()
def Fibo():
    n=int(input("Enter the number of terms: "))
    print("Fibonacci sequence:")
    a=0
    b=1
    print(a)
    print(b)
    for i in range (2,n):
        c=a+b
        a=b
        b=c
        print(c)
main()