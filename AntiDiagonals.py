def getAntiDiagonals(matrix, length):
    antiDiagonals = []

    for k in range(length):
        diagonal = []
        i, j = k, 0

        while i >= 0 and j < length:
            diagonal.append(matrix[i][j])
            i -= 1
            j += 1

        antiDiagonals.append(diagonal)

    for k in range(1, length):
        diagonal = []
        i, j = length - 1, k

        while i >= 0 and j < length:
            diagonal.append(matrix[i][j])
            i -= 1
            j += 1

        antiDiagonals.append(diagonal)

    max_length = max(len(diagonal) for diagonal in antiDiagonals)
    for diagonal in antiDiagonals:
        diagonal.extend([0] * (max_length - len(diagonal)))

    for i in range(noOfRows):
        for j in range(len(antiDiagonals[i])):
            print(antiDiagonals[i][j], end=' ')
            if (j + 1) % 3 == 0:
                print()


if __name__ == "__main__":
    noOfRows = int(input("Enter the no.of rows : "))

    matrix = []
    for i in range(noOfRows):
        matrix.append(list(map(int, input().split())))

    length = len(matrix)
    getAntiDiagonals(matrix, length)
