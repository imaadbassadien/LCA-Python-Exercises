# Question 1: creating and modifying lists
fruits = ["apple", "pear", "orange"]

fruits.append("banana")
fruits.insert(0, "berry")
fruits.remove("pear")

for fruit in fruits:
  print(fruit)

#question 2: list operations

numbers = [1, 2, 3, 4, 5]
squared = [x**2 for x in numbers]
total = sum(numbers)
average = total / len(numbers)

print("original numbers", numbers)
print("numbers squared", squared)
print("sum:", total)
print("average", average)

# Question 3: creating and modifying dictionaries 
country_capitals = {
  "japan": "tokyo",
  "egypt": "cairo",
  "israel": "tel aviv",
  "palestine": "jerusalem" 
}
country_capitals["Saudi arabia"] = "riyadh"
country_capitals["palestine"] = "gaza"

del country_capitals["israel"]

print(country_capitals)

#Question 5: dictionary operations

fruit_colors = {
  "apple" : "green",
  "banana" : "yellow",
  "berry" : "blue",
  "orange" : "orange"
}
print("Fruits (keys): ", list(fruit_colors.keys()))
print("colors (values): ", list(fruit_colors.values()))

print("fruits & colors:")
for fruit, color in fruit_colors.items():
  print(f"{fruit}:{color}")

check_fruits = "banana"
if check_fruits in fruit_colors:
  print(f"{check_fruits} is in the dictionary and its color is {fruit_colors[check_fruits]}.")
else:
  print(f"{check_fruits} is not in dictionary.")