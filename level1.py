# is it prime

def main():
    Primary()

def Primary():
    while True:
        try:
            n = int(input("Enter a number: "))
            if n == 1:
                print("1 is neither prime nor composite")
            elif n > 1:
                for i in range(2, n):
                    if n % i == 0:
                        print(n, "is not a prime number")
                        break
                else:
                    print(n, "is a prime number")
            else:
                print("Please enter a positive integer")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

main()
