vehicle = [0,1,0,1,1,0,0,1,1]

maxi = 0
cnt = 0

for i in vehicle:
    if i == 1:
        cnt += 1
        maxi = max(cnt, maxi)
    else:
        cnt = 0

print(maxi)