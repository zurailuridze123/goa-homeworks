def positive_sum(numbers):
    return sum(num for num in numbers if num > 0)
print(positive_sum([1, -4, 7, 12]))  
print(positive_sum([-1, -2, -3]))    
print(positive_sum([]))              
    