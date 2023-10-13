a = [8, 15, 17, 0, 11 ]
k = 17
n = len(a)

left = 0
right = 0
maxi = 0
tot = a[0]

while (right < n):
    while left < right and tot > k:
        tot -= a[left]
        left += 1
    if tot == k:
        maxi = max(maxi, right - left + 1)

    right += 1
    if (right < n):
        tot += a[right]

print(maxi)
