import sys
a = [1,5,3,2,4]
# largest = a[0]
# slargest = -1
# smallest = a[0]
# ssmallest = 99999999
# # sec_largest
# for i in a:
#     if i > largest:
#         slargest = largest
#         largest = i
#     elif i < largest and slargest < i:
#         slargest = i
# print(slargest)
# # sec smallest
# for j in a:
#     if j < smallest:
#         ssmallest = smallest
#         smallest = j
#     elif j > smallest and ssmallest > j:
#         ssmallest = j
# print(ssmallest)
a.sort()
print(a)