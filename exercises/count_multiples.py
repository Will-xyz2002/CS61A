def count_multiples(start, end, divisor):
    counter = 0
    while start <= end:
        if start % divisor == 0:
            counter += 1
            start += 1
        else:
            start += 1
    return counter
count_multiples(237 , 500 , 10)
