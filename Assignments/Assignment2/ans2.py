def identity_matrix(n):
    return [[1 if i == j else 0 for j in range(n)] for i in range(n)]

n = 3
matrix = identity_matrix(n)
for row in matrix:
    print(row)
