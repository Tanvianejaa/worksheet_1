#Write a Python program to print the following string in a specific format (see the output). Sample String : "Twinkle, twinkle, little star, How I wonder what you are! Up above the world so high, Like a diamond in the sky. Twinkle, twinkle, little star, How I wonder what you are".
print("Twinkle, twinkle, little star,\nHow I wonder what you are!\nUp above the world so high,\nLike a diamond in the sky.\nTwinkle, twinkle, little star,\nHow I wonder what you are.")


#Write a Python program that accepts the user's first and last name and prints them in reverse order with a space between them.
a=str(input("enter the name: "))
b=str(input("enter the surname: "))
print(b,a)

#Write a Python program that calculates the area of a circle based on the radius entered by the user.
c=int(input("enter radius: "))
d=(3.14*c*c)
print(d)

#Write a Python program to display the first and last colors from the following list. color_list = ["Red","Green","White" ,"Black"]
color_list = ["Red", "Green", "White", "Black"]
first_color = color_list[0]
last_color = color_list[-1]
print("First color:", first_color)
print("Last color:", last_color)

#Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn.
e=int(input("enter the integer: "))
print(e+(e*e)+(e*e*e))

#Write a Python program that accepts a sequence of comma-separated numbers from the user and generates a list and a tuple of those numbers. Sample data : 3, 5, 7, 23
input_string = input("Enter comma-separated numbers: ")
numbers_list = input_string.split(',')
numbers_list = [int(num) for num in numbers_list]
numbers_tuple = tuple(numbers_list)
print("List:", numbers_list)
print("Tuple:", numbers_tuple)

#Write a program that will convert celsius value to Fahrenheit.
celsius = float(input("Enter temperature in Celsius: "))
fahrenheit = (celsius * 9/5) + 32
print(fahrenheit)

#User will input (2numbers). Write a program to swap the numbers. Add incrementally in any one variable.
f=int(input("enter number 1: "))
g=int(input("enter the number 2: "))
print("before swap",f,g)
h=f
f=g
g=h
print("after swap",f,g)
print(f+g)

#Write a program that will tell whether the number entered by the user is odd or even.
i=int(input("enter the number: "))
if i%2==0:
    print("even")
else:
    print("odd")

#Write a program that will tell whether the given year is a leap year or not.
year = int(input("Enter a year: "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")

#Write a program to find the euclidean distance between two coordinates.
j=int("input the x1: ")
k=int("input the y1: ")   
l=int("input the x2: ")  
m=int("input the y2: ")  
print(l-j,m-k)

#Write a program that take a user input of three angles and will find out whether it canform a triangle or not.
n=int(input("enter angle 1: "))
o=int(input("enter angle 2: "))
p=int(input("enter angle 3: "))
if n+o+p==180:
    print("possible!")
else:
    print("not possible!")

#WAP to find compound interest for given values.
principal = float(input("Enter the principal amount (P): "))
rate = float(input("Enter the annual interest rate (r) as a percentage: "))
times_compounded = int(input("Enter the number of times interest is compounded per year (n): "))
years = float(input("Enter the number of years (t): "))
rate_decimal = rate / 100
amount = principal * (1 + rate_decimal / times_compounded) ** (times_compounded * years)
compound_interest = amount - principal
print(f"Compound Interest: {compound_interest:.2f}")

#Given a positive integer N, the task is to write a Python program to check if the number is Prime or not in Python.
N = int(input("Enter a positive integer: "))
if N <= 1:
    print(f"{N} is not a prime number.")
elif N == 2:
    print(f"{N} is a prime number.")
elif N % 2 == 0:
    print(f"{N} is not a prime number.")
else:
    is_prime = True
    for i in range(3, N, 2):
        if N % i == 0:
            is_prime = False
            break
    if is_prime:
        print(f"{N} is a prime number.")
    else:
        print(f"{N} is not a prime number.")

#Given a positive integer N.The task is to find 12 +22 +32 +.....+N2.
z=int("input a positive integer: ")
sum=0
for y in range(1,z,1):
    sum+=i**2
print(sum)