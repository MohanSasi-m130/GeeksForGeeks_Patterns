N= 5
for i in range(1,N+1):
    for j in range(1,i+1):
        print(j, end=" ")
    print(" "*(((N-i)*2)*2), end=" ")
    for k in range(1,i+1):
        print(i+1-k, end=" ")
    print()
