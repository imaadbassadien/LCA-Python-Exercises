# question 1 basic function definition and calling

def greet():
  print("Hello, World")

greet()  

# question 2 function with parameters

def personalized_greeting(name):
  print(f"Hello, {name}!")

personalized_greeting("Imaad")

# Question 3: function with return value

def square(number):
  return number **2
result = square(5)
print(result)

# Question 4: Functions with multiple parameters and return values

def rectangle_area(length, width):
  return length  * width
result = rectangle_area(4, 5)
print(result)

# Question 5: Using a FUnction as an Argument

def apply_operation(function, number):
  return function(number)
def double(num):
  return num * 2

result1 = apply_operation(double, 7)
print(result1)

def square(num):
  return num * num

result2 = apply_operation(square, 3)
print(result2)