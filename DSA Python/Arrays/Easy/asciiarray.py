import re

arr = [75,23,65,23,2,65,91,113]


for i in range(len(arr)):
    if 91 <= arr[i] <= 96:
        arr[i] = 1
arr.sort()
for i in range(len(arr)):
    if 64 < arr[i] < 91 or 96 < arr[i] < 123:
        arr[i] = chr(arr[i])
    else:
        arr[i] = -1


print(arr)

