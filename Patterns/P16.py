N =5
from string import ascii_uppercase as usc

for i in range(1,N+1):
    for j in range(i):
        print(str(usc[i-1]), end=" ")
    print()