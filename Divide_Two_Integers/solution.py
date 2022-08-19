def divide(dividend,divisor):
    count= 0
    divisor1= divisor
    dividend1 = dividend
    if divisor == 0 or dividend==0:
        return 0
    elif divisor == dividend:
        return 1
    elif divisor < 0 or dividend <0:
        divisor1= abs(divisor)
        dividend1= abs(dividend)
    for i in range(0,dividend1,divisor1):
        if i+divisor1 <= dividend1:
            count +=1
    if divisor < 0 or dividend< 0:
        return -abs(count)
    else:
        return count

print(divide(-1,-1))
