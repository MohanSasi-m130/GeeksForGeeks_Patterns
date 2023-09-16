N =5
from string import ascii_uppercase as auc
for i in range(1, N+1):
    for j in range(1,i+1):
        print(auc[N-j], end=" ")
    print()