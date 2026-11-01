# REFLECTION
# 1. Most surprising thing about Python lists:
#    I was surprised that lists start at index 0, because we naturally start
#    counting things at 1. Initially, I assumed it would be the same, but I
#    learned that it throws everything off. Now, understanding Python, this makes sense. 
#
# 2. A real business situation where a Python list beats doing it in Excel:
#    In my business management class in high school, Python would have saved me
#    a lot of time organizing revenue information from 10 different retail
#    branches in Excel. By using Python, the list wouldve been much faster and easier to create. 


# ---------------- Exercise 1: Build the list ----------------
print("Exercise 1")
inventory = ["pen", "notebook", "stapler", "tape", "marker"]
print(inventory)
print(len(inventory))

# ---------------- Exercise 2: Index practice ----------------
print("\nExercise 2")
print(inventory[0])
print(inventory[-1])
print(inventory[len(inventory) // 2])

# ---------------- Exercise 3: Slicing ----------------
print("\nExercise 3")
print(inventory[:3])
print(inventory[-2:])
print(inventory[::2])

# ---------------- Exercise 4: Modify ----------------
print("\nExercise 4")
inventory.append("envelope")
print(inventory)
inventory.remove("tape")
print(inventory)
inventory.sort()
print(inventory)

# ---------------- Exercise 5: Tuple comparison ----------------
print("\nExercise 5")
coords = (40.7128, -74.0060)
try:
    coords[0] = 99
except TypeError as e:
    print(f"TypeError caught: {e}")
    print("Tuples are useful for coordinates because they are immutable, "
          "so a location's values can't be changed by accident.")
print(coords)

# ---------------- Exercise 6: Average of a list of sales ----------------
print("\nExercise 6")
sales = [100, 250, 75, 480, 200]
total = sum(sales)
count = len(sales)
average = total / count
print(f"Total: {total} | Average: {average} | Best: {max(sales)} | Worst: {min(sales)}")

# ---------------- Exercise 7: Accumulator pattern ----------------
print("\nExercise 7")
prices = [9.99, 14.99, 4.99, 24.99, 1.99]
discounted = []
for price in prices:
    discounted.append(round(price * 0.9, 2))
  print(prices)
print(discounted)

# ---------------- Exercise 8: Filter above threshold ----------------
print("\nExercise 8")
sales = [340, 127, 589, 204, 467, 88, 731, 315, 62, 490]
high_sales = []
for day in sales:
    if day > 300:
        high_sales.append(day)
print(high_sales)
print(len(high_sales))
print(round(sum(high_sales) / len(high_sales), 2))
