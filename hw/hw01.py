def k_in_num( k , num ):
    while num > 0:
        if k == num % 10:
            return True
        num = num // 10
    return False
