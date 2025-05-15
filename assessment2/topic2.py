#  Tasks:
# 1. Write a script to calculate the area and perimeter of a rectangle using variables.
# Dimensions of the rectangle
l,b=8,4
# Calculating area and perimeter
area=l*b
perimeter=2 *(l+b)
# Output
print("Area:", area)
print("Perimeter:", perimeter)

# 2. Write a script that takes two numbers as input and prints whether the first number is greater than, less than, or equal to the second number.
# Input two numbers
n1=int(input("Enter first number: "))
n2=int(input("Enter second number: "))
# Comparison
if n1>n2:
    print("First number is greater than second.")
elif n1<n2:
    print("First number is smaller than second.")
else:
    print("First number is equal to second.")

# 3. Write a script that checks if a given year is a leap year (divisible by 4, but not by 100 unless also divisible by 400).
# input
y = int(input("Enter year: "))
# Check for leap year
if (y % 4==0 and y%100!=0) or (y%400==0):
    print(y, "is a leap year.")
else:
    print(y, "is not a leap year.")

# 4. Experiment with different arithmetic and logical operators in the interpreter.
#ARITHMETIC
print(4+5) #addition
print(10-3) #subtraction
print(3*2) #multiplication
print(10/2) #division
print(7%3) #modulus
print(2**4) #exponent
#LOGICAL
print(not True) 
print(5>3 and 2<1)
print(5>3 or 2<1)

# 5. Write a script that concatenates two strings and prints the result. 
s1="Hello"
s2="World"
# + operator to concatenate
res=s1+ " " +s2
print("Concatenated String:",res)
