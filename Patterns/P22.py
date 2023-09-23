N=5

for row in range(N * 2 - 1):
    for column in range(N * 2 - 1):
        top = row
        bottom = (N * 2) - 2 - row
        left = column
        right = (N * 2) - 2 - column
        minimum = min(top, bottom, left, right)
        print(N-minimum, end=' ')
    print()
