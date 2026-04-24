# Question 1: using for loop with a list

fruits = ["apples", "banana", "cherry", "date", "elderberry"]
for fruit in fruits:
  print(fruit)

# Question 2: using while loop for countdown

count = 5
while count > 0:
  print(count)
  count -= 1

# Question 3: using a for loop with range()

for number in range(1,11):
  print(number**2)

# Question 4: using the random module

import random
colors = ["red", "blue", "green", "purple", "yellow"]
for x in range(3):
  random_colors = random.choice(colors)
  print(random_colors)

# Question 5: creating and using custom module

from maths_operation import add, subtract, multiply, divide
import random

print("testing 3+3")
print(add(3, 3))
# line break below
print()

print("     basic calculator     ")
operations = ['1' , '2', '3', '4']
running = True

while running:
  print("   Operators:" \
  "1=add, 2=subtract, 3=multiply, 4=divide, 5=off")
  random_op = random.choice(operations)
  
  choice = input("choose operation(1-5): ")
  if choice == '5':
    running = False
    print("thankyou, goodbye")
    break

  if choice in ['1', '2', '3', '4']:
    try:
      num1 = float(input("Enter first number: "))
      num2 = float(input("Enter second number: "))

      if choice == '1':
        result = add(num1, num2)
      elif choice == '2':
        result = subtract(num1, num2)
      elif choice == '3':
        result = multiply(num1, num2)
      elif choice == '4':
        result = divide(num1 , num2)

      print(f"Result: {result}")
    except ValueError:
      print("error: please enter valid numbers")
    else:
      print("invalid choice, please enter 1-5")
print("calculator noww off!")