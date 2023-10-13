arr = [1,2,3,4,5,6]
d = 2
n = len(arr)

#--------------------------------------------
#-------------------------optimal------------

#reverse arr[0] to a[d-1]

def reversearr(arr, start, end):
    while (start <= end):
        temp = arr[start]
        arr[start] = arr[end]
        arr[end] = temp
        start+=1
        end-=1
    return arr

reversearr(arr,0,n-1)
reversearr(arr,d,n-1)


print(arr)