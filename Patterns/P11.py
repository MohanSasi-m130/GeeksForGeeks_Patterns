N = 5

for i in range(1, N+1):
    if i%2==0:
        c = 0
    else:
        c = 1
    for j in range(i):
        print(c, end=" ")
        c = 1-c
    print()