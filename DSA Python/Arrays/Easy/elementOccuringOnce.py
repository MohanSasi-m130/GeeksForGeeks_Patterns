arr = [1,1,2,2,3,3,4,5,5]


#------------------BRUTE----------------------------

# for i in arr:
#     count = 0
#     num = i
#     for j in arr:
#         if j == num:
#             count += 1
#     if count == 1:
#         print(num)

#_______________________________________________________
#-------------------BETTER------------------------------

# maxi = max(arr)
#
# hasharr = [0]*(maxi+1)
#
# for num in arr:
#     hasharr[num] += 1
#
# for num in arr:
#     if hasharr[num] == 1:
#         print(num)

#_________________________________________________________
#---------------------OPTIMAL-----------------------------

XOR = 0

for n in arr:
    XOR = XOR ^ n

print(XOR)
