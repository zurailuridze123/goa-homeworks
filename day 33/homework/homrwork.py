 # Classwork 3: Slicing and List Comprehensions

# 1. Create a list named numbers that contains the integers from 1 to 10
# number =  [1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9 , 10]
# print(number)


# 2. Use list slicing to create a new list named first_half that contains the first five elements from numbers.
# number =  [1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9 , 10]

# first_half =  number[:5]
# print(first_half)

# 3. Use list slicing to create another list named second_half that contains the last five elements from numbers.

# number =  [1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9 , 10]

# secend_half =  number[-5:]
# print(secend_half)


# 4. Use a list comprehension to create a new list named squares that contains the squares of each number in the numbers list.
# numbers =  [1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9 , 10]
# squares = [x**2 for x in numbers]
# print(squares)


# 5. Print all three lists: first_half, second_half, and squares.
numbers =  [1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9 , 10]
first_half =  numbers[:5]
secend_half =  numbers[-5:]
squares = [x**2 for x in numbers]
print(first_half , secend_half , squares)






