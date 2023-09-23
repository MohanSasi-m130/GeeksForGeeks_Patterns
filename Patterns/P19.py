N = 5

for i in range(1,2*N+1):
    if i <=N:
        # for j in range(i+1):
        print("*"*(N-i+1), end="")
        print(" "*((i-1)*2), end="")
        print("*"*(N-i+1), end="")
    else:
        print("*"*(i-N), end="")
        print(" "*(((N*2)-i)*2), end="")
        print("*"*(i-N), end="")

    print()