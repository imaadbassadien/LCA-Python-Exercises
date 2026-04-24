# Question 1: Variable Assignment and String Manipulation

name = input("What is your name? ")
age = input("How old are you? ")
print(f"Hello, {name}! you are {age} years old")

# Question 2: integer operations
length = int(input("What is the length of the rectangle in centimeters? "))
width = int(input("What is the width of the rectangle centimeters? "))
area = length * width
print(f"the area of your rectangle is {area}cm squared.")

# Question 3: working with floats
print("Can you tell me the temperature in your room? For example 25.3 degrees")
temp =float(input(" So what is the current temperature in Celsius? "))
fahrenheit = (temp * 9/5) + 32
print(f"That would make it {fahrenheit:.2f} degrees Fahrenheit.")