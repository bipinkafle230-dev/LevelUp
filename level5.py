'''
Armstrong Number=153
=153
(1^3 + 5^3 + 3^3 = 153)
'''

def main():
    Armstrong()
def Armstrong():
    n=int(input("Enter a number:"))
    temp=n # temp variable to store the original number
    sum=0   # variable to store the sum of cubes of digits
    while n>0:
        digit=n%10
        sum=sum+digit**3
        n=n//10
    if temp==sum:
        print(temp,"is an Armstrong number")
    else:
        print(temp,"is not an Armstrong number")
main()