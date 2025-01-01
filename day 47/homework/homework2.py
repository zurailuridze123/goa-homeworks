def sum_of_n(n):
    result = []
    for i in range(abs(n) + 1):
        if n >= 0:
            result.append(sum(range(i+1)))
        else:
            result.append(-sum(range(i+1)))  
    return result
