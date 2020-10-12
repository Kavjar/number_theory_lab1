import functions as func
from functions import swapers as swapers


def file_output(res):
    output.write("Детермінант матриці = " + str(round(func.determinant(A, n), 1)) + "\n")
    if res == 0:
        output.write("Обернена матриця A^-1 :" + "\n")
        for s in range((len(swapers) - 1), -1, -1):
            matrix_inv[swapers[s][0]], matrix_inv[swapers[s][1]] = matrix_inv[swapers[s][1]], matrix_inv[swapers[s][0]]
        for i in range(n):
            for j in range(n):
                if matrix_inv[i][j] >= 0:
                    output.write(' ' + str(matrix_inv[i][j]) + ' ')
                else:
                    output.write(str(matrix_inv[i][j]) + ' ')
            output.write("\n")
    else:
        output.write("Обереної матриці не існує!")


file, output = open("matrix.txt", "r"), open("reverse_matrix", "w")
n = int(file.readline())
A, matrix_inv = [], [[0] * n for i in range(n)]
for line in file:
    A.append(list(map(int, line.split())))
file_output(func.inverse_matrix(A, matrix_inv, n))
file.close()
output.close()
