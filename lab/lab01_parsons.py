#A number has a digit-position match if the ith-to-last digit is i. 
#For example, 980 has the last 0th-to-last digit as 0. Or 98276 has the 2nd-to-last digit as a 2.

#Write a function that determine if a number n has a digit-position match at a kth-to-last digit k.

#>> digit_pos_match(980, 0) # last digit is 0
#True
#>> digit_pos_match(980, 2) # 2nd-to-last digit is 9, not 2
#False
#>> digit_pos_match(98276, 2) # 2nd-to-last digit is 2
#True
#>> digit_pos_match(98276, 3) # 3nd-to-last digit is 8, not 3
#False
def digit_pos_match(n , k):
    index = 0
    while index < k:
        n //= 10
        index += 1
    return n % 10 == k

digit_pos_match(98276 , 3)
