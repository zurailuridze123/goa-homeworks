#   Classwork 1: Basic List Operations
# 1. Create a list named fruits that contains the following items: "apple", "banana", "cherry", "date", and "elderberry".k
fruits = ["apple", "banana", "cherry", "date",  "elderberry"]
# 2. Print the entire list.
fruits = ["apple", "banana", "cherry", "date",  "elderberry"]
print(fruits)
# 3. Access and print the first and last items in the list.
fruits = ["apple", "banana", "cherry", "date",  "elderberry"]
print(fruits[0],fruits[-1])
# 4. Add a new fruit "fig" to the list.
fruits = ["apple", "banana", "cherry", "date",  "elderberry"]
fruits.append("fig")
print(fruits)
# 5. Remove "banana" from the list.
fruits = ["apple", "banana", "cherry", "date",  "elderberry"]
fruits.remove("banana")
print(fruits)

# 6. Change the value of the second item to "blueberry".
fruits = ["apple", "banana", "cherry", "date",  "elderberry"]
fruits[2] = "blueberry"
print(fruits)

# 7. Print the length of the list. 
fruits = ["apple", "banana", "cherry", "date",  "elderberry"]  
print(len(fruits))