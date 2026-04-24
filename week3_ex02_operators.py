# Question 1: Aristhmetic and Assignment Operators
x = 17
y = 5
x += 3
# x now equals 20
y *= 2
# y now equals 10
result = x / y
print(f"Result:{result}")

# Question 2 comparioson and logical operators
a = 10
b = 8
c = 4

condition1 = a > b
condition2 = b % 2 ==0
condition3 = c <= a
final_condition = condition1 or (condition2 and condition3)

print(final_condition)

# Question 3 conditional statements

score = int(input("Please punch in your test score out of 100: "))
if score >= 90:
  grade = "A"
elif score >= 80:
  grade = "B"
elif score >= 70:
  grade = "C"
elif score >= 60:
  grade = "D"
else:
  grade = "F"
  
print(f"Your grade is: {grade}")  

# Question 4 combining operators and conditionals

print("Lets do some basic calculations")
num1 = float(input("Enter your first number: "))
num2 = float(input("Enter your second number: "))
operation = input("Please input an operation(+ ,- ,* ,/): ")
if operation == "+":
  result = num1 + num2
elif operation == "-":
  result = num1 - num2
elif operation == "*":
  result = num1 * num2
elif operation == "/":
  if num2 ==0:
    result = "Error: Cannot divide by zero!"
  else:
    result = num1 / num2
else:
  result = "error: invalid operation"    
print(f"Result: {result}")  