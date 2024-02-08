# while loop
# incrementing
number = 5
while number <= 10:
    print(number)
    number += 1


# decrementing
numbers = 105
while numbers >= 100:
    print(numbers)
    numbers -= 1

# break statement
x = 20
while x <= 25:
    print(x)
    if x == 24:
        break
    x += 1

# continue statements
y = 79
while y < 85:
    y += 1
    if y == 83:
        continue
    print(y)

# for loop
languages = ["Python","Java","c++"]
for z in languages:
    print(z)

# range
for mynumber in range(5):
    print(mynumber)

for mynum in range(2,6):
  print(mynum)

for count in range(20,31,2):
    print(count)
