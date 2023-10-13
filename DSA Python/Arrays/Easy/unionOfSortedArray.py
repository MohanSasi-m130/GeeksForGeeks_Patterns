a = [1, 2, 3, 4, 6]
b = [2, 3, 5]



#------------------BRUTE-----------------------------------

# s = set()
# u =[]
#
# for i in a:
#     s.add(i)
# for j in b:
#     s.add(j)
# for k in s:
#     u.append(k)
# print(u)


#----------------------------------------------------
#-------------------OPTIMAL---------------------------

i,j = 0,0
union = []

while i < len(a) and j < len(b):
    if a[i] <= b[j]:
        if len(union) == 0 or union[-1] != a[i]:
            union.append(a[i])
        i += 1
    else:
        if len(union) == 0 or union[-1] != b[j]:
            union.append(b[j])
        j += 1

while i < len(a):
    if len(union) == 0 or union[-1] != a[i]:
        union.append(a[i])
    i += 1

while j < len(b):
    if len(union) == 0 or union[-1] != b[j]:
        union.append(b[j])
    j += 1


print(union)