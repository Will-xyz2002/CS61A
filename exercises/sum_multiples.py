def sum_multiples(start, end, divisor):
    multiples = 0
    while start <= end:
        if start % divisor ==0:
            multiples += start
            start += 1
        else:
            start += 1
    return multiples
