a = [1,2,4,5]
N = len(a)
# ------------Sum of array approach-------

SumOfN = (N*(N+1))//2
SumOfA = sum(a)

print(SumOfN-SumOfA)

# --------------XOR approach-------------

XOR1 = 0
XOR2 = 0

for i in range(N - 1):
    XOR1 = XOR1 ^ a[i]
    XOR2 = XOR2 ^ (i + 1)

XOR2 = XOR2 ^ N

print(XOR1 ^ XOR2)
