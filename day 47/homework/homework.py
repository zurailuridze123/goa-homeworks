def even_numbers(arr,n):
    array = []

    for i in arr:
        if i % 2 == 0:
            array.append(i)

    return array[-n:]