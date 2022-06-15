def count_evens(start, end):
    counter = 0
    while start <= end:
        if start % 2 == 0:
            counter += 1
            start += 1
        else:
            start += 1
    return counter
count_evens(237 , 500)
