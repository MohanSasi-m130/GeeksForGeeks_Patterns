arr = [1,2,3,4,5,6,7,8,9]
d = 4
n = len(arr)
#-----------Brute-----------------
#temp array


# temp = []
# for i in range(d):
#     temp.append(arr[i])
# #shifting
# for j in range(n-d):
#     arr[j] = arr[j+d]
# # print(arr)
# # putting temp arr back in
# for k in range(n-d,n):
#     arr[k] = temp[k-n+d]
#
# print(arr)


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


reversearr(arr,0,d-1)
reversearr(arr,d,n-1)
reversearr(arr,0,n-1)
print(arr)