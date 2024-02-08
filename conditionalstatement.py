temperature = 13

if temperature > 25:
    print(" It is hot")
else:
    print("It is cold")

# A program that returns the largest number among three numbers
num1 = 12
num2 = 85
num3 = 67
if num1 > num2 and num1 > num3:
    print(num1, "is the largest number")
elif num2 > num1 and num2 > num3:
    print(num2, "is the largest number")
else:
    print(num3, "is the largest number")

# A program that checks whether number is even or not
number = 34
if number % 2 == 0:
    print(number, "is even")
else:
    print(number, "is odd")

# A program that checks whether number is prime or not

n = 17
if n % 7 == 0:
    print(n, "is a prime number")
elif n % 7 == 1:
    print(n, "is a prime number")
else:
    print(n, "is not a prime number")

n = int(input("enter a number"))
if n > 1:
    for i in range(2, n):
        if n % 1 == 0:
            print("is not a prime number")
        break
    else:
        print("is a prime number")

else:
    print("is not a prime number")


num=int(input("Enter a number:"))
if num > 1:
    for i in range(2 , num) :
        if num % i == 0 :
            print("is not a prime number")
            break
        else: print("its a prime number")
    else : print("is not a prime number")
