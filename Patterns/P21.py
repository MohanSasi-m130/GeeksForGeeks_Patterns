N= 9

for i in range(1,N+1):
    if i == 1 or i == N:
        for j in range(1,N+1):
            print("*", end="")

    else:
        print("*", end="")
        print(" "*(N-2), end="")
        print("*", end="")
    print()