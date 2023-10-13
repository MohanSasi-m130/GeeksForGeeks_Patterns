a = [0,1,0,7,0,4,0,2,0,2]
n = len(a)

#-----------------Brute-------------------------

# step-1 : create a temp aay and push all non zero elements to it

# temp = []
# z = 0   # count of zeroes
# for i in range(n):
#     if a[i] != 0:
#         temp.append(a[i])
#     else:
#         z += 1
# nz = len(temp) # size of temp
# # step - 2 : insert temp elements into a
#
# for j in range(len(temp)):
#     a[j] = temp[j]
#
# # step - 3 : make remaining elements in a as zero
#
# for k in range(nz,n):
#     a[k] = 0
#
# print(a)


#---------------OPTIMAL-----------------------------------------


# step - 1 : create two pointers i,j and set j for first 0

j =-1

for i in range(len(a)):
    if a[i] == 0:
        j = i
        break
# step - 2 : in looping through elements of aay, move the j pointer for every element and when non zero element is found swap it with i

if j == -1:
    print(a)

for i in range(j+1,n):
    if a[i] != 0:
        a[i], a[j] = a[j], a[i]
        j += 1

print(a)

