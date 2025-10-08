# 1. Favourite sportsperson list operations

# Initial list
sports = ["Roger Federer", "Serena Williams", "Lionel Messi", "Michael Jordan", "Virat Kohli"]

# a) Length of the list
print("Length:", len(sports))

# b) Add a sixth sportsperson at the end
sports.append("Cristiano Ronaldo")
print("After adding sixth:", sports)

# c) Remove the sixth and add after the second sportsperson
sixth = sports.pop()            # Remove last element
sports.insert(2, sixth)         # Insert after second (index 1, so index 2)
print("After repositioning sixth:", sports)

# d) Remove two sportspersons and replace with two others
# Remove elements at index 3 and 1 (delete higher index first)
del sports[3]
del sports[1]

# Insert new sportspersons at index 1 and 2
sports.insert(1, "Simone Biles")
sports.insert(2, "Usain Bolt")
print("After replacement:", sports)

# e) Sort alphabetically
sports.sort()
print("Sorted list:", sports)

print("\nList functions available:", dir(sports))

# 2. Even numbers between x and y (x=your age, y=parent's age)
x = 20   # Replace with your age
y = 50   # Replace with parent's age

evens = [num for num in range(x, y+1) if num % 2 == 0]
print("\nEven numbers between", x, "and", y, ":", evens)
