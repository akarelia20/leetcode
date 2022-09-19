def addBinary(a,b):
    sum= 0
    result= ""
    if a == "0" and b== "0":
        return "0"
    for i in range (len(a)):
        sum += int(a[i])*(2**(len(a)-(i+1)))
    for i in range (len(b)):
        sum += int(b[i])*(2**(len(b)-(i+1)))
    while sum > 0:
        result = str(sum%2)+ result
        sum = sum//2
    return result


print(addBinary("0", "1"))

