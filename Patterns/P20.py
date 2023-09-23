N = 2

# for i in range(1,2*N+1):
#     if i <= N:
#         print("*"*i, end="")
#         print(" "*(N-i)*2, end="")
#         print("*"*i, end="")
#     else:
#         print("*"*(2*N-i), end="")
#         print(" "*(i-N)*2, end="")
#         print("*"*(2*N-i), end="")
#     print()

spaces = 2*N-2
for i in range(1,2*N):
    stars = i
    if i > N:
        stars = 2*N - i
    for j in range(1,stars+1):
        print("*", end="")
    for j in range(1, spaces+1):
        print(" ",end="")
    for j in range(1, stars+1):
        print("*",end="")
    print()

    if i < N:
        spaces -= 2
    else:
        spaces += 2
