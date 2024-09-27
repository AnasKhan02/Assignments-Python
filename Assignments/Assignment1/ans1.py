# (a)
# 1
# 22
# 333
# 4444
# 55555
lines = 5
for i in range(1,lines+1):
    print(str(i)*i)


# (b)
# 1
# 23
# 456
# 78910
cur = 1
lines = 4
for i in range(1,lines+1):
    stri = ''
    for j in range(i):
        stri += str(cur)
        cur += 1
    print(stri)


# (c)
#            1
#          1   2
#        1   2   3
#      1   2   3   4
#    1   2   3   4   5
#     1    2   3   4
#        1   2   3
#          1   2
#            1
line = 5
# for upper part
for i in range(1,line+1):
    # print(i)
    print(' '*(line-i), end = ' ')
    for j in range(1,i+1):
        print(j,end=' ')
    print()
# for lower part
for i in range(line-1,0,-1):
    print(' ' * (line-i),end=' ')
    for j in range(1,i+1):
        print(j,end=' ')
    print()

# (d)
# 1 2 3 4 5
#  1 2 3 4
#   1 2 3
#    1 2
#     1
#    2 1
#   3 2 1
#  4 3 2 1
# 5 4 3 2 1

max_rows = 5

for i in range(max_rows, 0, -1):
    print(' ' * (max_rows - i), end=' ')

    for j in range(1, i + 1):
        print(j, end=' ')

    print()

for i in range(2, max_rows + 1):
    print(' ' * (max_rows - i), end=' ')

    for j in range(i, 0, -1):
        print(j, end=' ')

    print()
