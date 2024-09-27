def generate_magic_square(n):

    if n % 2 == 0:
        raise ValueError("n must be an odd number")


    magic_square = [[0] * n for _ in range(n)]


    r, c = 0, n // 2

    for num in range(1, n ** 2 + 1):
        magic_square[r][c] = num


        new_r, new_c = r - 1, c + 1


        if new_r < 0:
            new_r = n - 1


        if new_c >= n:
            new_c = 0


        if magic_square[new_r][new_c] != 0:
            new_r, new_c = r + 1, c - 2

            if new_r >= n:
                new_r = 0

            if new_c < 0:
                new_c = n - 1

        r, c = new_r, new_c

    return magic_square


def print_magic_square(magic_square):
    n = len(magic_square)
    for row in magic_square:
        print(" ".join(f"{num:2}" for num in row))


n = 3
magic_square = generate_magic_square(n)
print_magic_square(magic_square)
