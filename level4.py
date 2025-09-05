'''
Palindrome Number=121
=121
(Mirror image of 121 is 121)'''

def main():
    Palindrome()
def Palindrome():
    n=int (input("Enter a number: "))
    temp=n    # temp variable to store the original number
    rev=0     # variable to store the reversed number
    while n>0:
        digit=n%10   # get the last digit
        rev=rev*10+digit  # append the digit to the reversed number
        n=n//10      # remove the last digit from the original number
    if temp==rev:
        print(temp,"is a palindrome number")
    else:
        print(temp,"is not a palindrome number")
main()