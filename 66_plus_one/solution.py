def plusOne(arr):
    num= ""
    result= []
    for i in range(len(arr)):
        print(arr[i])
        num += str(arr[i])
    print(num)
    num = int(num)+1
    for i in str(num):
        result.append(int(i))
    return result


print(plusOne([9]))