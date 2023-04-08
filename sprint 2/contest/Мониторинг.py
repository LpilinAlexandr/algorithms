row_count = int(input())
column_count = int(input())

matrix = [[j for j in input().split()] for i in range(row_count)]

new_matrix = [[] for _ in range(column_count)]

for m in matrix:
    for idx, i in enumerate(m):
        new_matrix[idx].append(i)

for i in new_matrix:
    print(' '.join(i))
