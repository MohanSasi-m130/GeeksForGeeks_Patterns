N=5
from string import ascii_uppercase as auc
M = N
for i in range(1,N+1):
    for j in range(N-i+1):
        print(auc[j], end=" ")
    print()

