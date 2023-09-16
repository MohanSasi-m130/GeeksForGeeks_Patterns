from string import ascii_uppercase as auc

N=5
for i in range(1,N+1):
    for j in range(i):
        print(auc[j], end=" ")
    print()