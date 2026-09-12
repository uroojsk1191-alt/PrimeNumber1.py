print("Prime Numbers")
n = int(input("Enter your number: "))
for i in range(2,n):
    if n % i == 0:
        print("The number is not a prime number")
        break
else:
    print("The number is a prime number")