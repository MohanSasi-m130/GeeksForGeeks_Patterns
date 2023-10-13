arr =[3,4,5,67,3,24]
n = len(arr)
temp = arr[0]
for i in range(n-1):
    arr[i] = arr[i+1]
arr[n-1] = temp
print(arr)