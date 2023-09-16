# line 0 -> 8 spaces, 1 star
# line 1 -> 6 spaces, 3 star
# so on till n lines and 2n-1 columns (if n = 6, 11 cols)
'''

plan -1
1) take N
2) 2n will be the range
3) split the range to even and odd arrays. reverse even array
4) count 1 to N rows and 1 to 2N-1 columns, for each line traverse the array and print spaces and stars
with help of arrays.


'''
# #s1
N = 5
# col = 2*N
# eve = []
# odd = []
# # s3
# for i in range(col):
#     if i%2 == 0:
#         eve.append(i)
#     else:
#         odd.append(i)
# eve.reverse()
# pat = []
# for p in range(len(eve)):
#     pat.append((eve[p],odd[p]))
#
# for blank,star in pat:
#     print((blank)*' '+ star*'* '+(blank)*' ')

#----------------------------------------------------------------------------------
#Simple Method

for i in range(1,N+1):
    print(" "*(N-i) + "*"*((2*i)-1))


