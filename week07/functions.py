# Self-Assesment Reflection Answers
# 1. You make a variable that starts at 0, add each item to it inside the loop, and
then print it after the loop. Each step matters because without the start the code
breaks, without the adding the answer is wrong, and without printing you never see
it.
# 2. The while loop took more lines because I had to make i and add 1 to it myself.
The for loop is shorter and easier, but the while loop gives more control.
# 3. At a restaurant job, I could use a list of tips from each table. I would add
them all up in a loop and print the average tip at the end.
# --- Exercise 1 ---
sales = [120, 80, 250, 175, 90, 410, 60, 215]
total = 0
for sale in sales:
total += sale
print(f"Total: ${total}")
# --- Exercise 2 ---
sales = [120, 80, 250, 175, 90, 410, 60, 215]
total = 0
count = 0
for sale in sales:
total += sale
count += 1
average = total / count
print(f"Total: ${total}")
print(f"Count: {count}")
print(f"Average: ${average:.2f}")
# --- Exercise 3 ---
sales = [120, 80, 250, 175, 90, 410, 60, 215]
current_max = 0
for sale in sales:
if sale > current_max:
current_max = sale
print(f"Largest sale: ${current_max}")
# --- Exercise 4 ---
sales = [120, 80, 250, 175, 90, 410, 60, 215]
count_over = 0
total_over = 0
for sale in sales:
if sale > 100:
count_over += 1
total_over += sale
print(f"Sales over $100: {count_over}")
print(f"Total of those sales: ${total_over}")
# --- Exercise 5 ---
sales = [120, 80, 250, 175, 90, 410, 60, 215]
for sale in sales:
if sale > 400:
print(f"Alert: outlier found - ${sale}. Stopping.")
break
if sale <= 100:
continue
print(f"${sale}")
# --- Exercise 6 ---
sales = [120, 80, 250, 175, 90, 410, 60, 215]
total = 0
i = 0
while i < len(sales):
total += sales[i]
i += 1
print(f"Total: ${total}")
# Comment: I would use the for loop in production. It is shorter, easier
# to read, and avoids index mistakes like forgetting i += 1, which would
# cause an infinite loop.
# --- Exercise 7 ---
sales = [120, 80, 250, 175, 90, 410, 60, 215]
for sale in sales:
if sale >= 200:
rate = 10
elif sale >= 100:
rate = 5
else:
rate = 0
discounted = sale * (1 - rate / 100)
print(f"${sale}
