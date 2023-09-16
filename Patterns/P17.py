from string import ascii_uppercase as auc
N=4
for i in range(1,N+1):
    print(" "*(N-i), end="")
    for j in range((2*i)-i):
        print(auc[j],  end="")
    for k in range(1,(2*i)-i):
        print(auc[i-k-1], end="")
    print()
