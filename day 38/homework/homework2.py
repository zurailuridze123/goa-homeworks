def find_average(numbers):
    if not numbers:
        return 0  
    return sum(numbers) / len(numbers)
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
average = find_average(numbers)
print("საშუალო რიცხვი:", average)