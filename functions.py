swapers = []
def max_in_matrix(matrix, n, k):
    mx = abs(matrix[k][k])
    row_id, col_id = k, k
    for i in range(k, n):
        for j in range(k, n):
            if abs(matrix[i][j]) > mx:
                mx = matrix[i][j]
                row_id, col_id = i, j
    for j in range(n):
        matrix[j][k], matrix[j][col_id] = matrix[j][col_id], matrix[j][k]
    for i in range(n):
        matrix[k][i], matrix[row_id][i] = matrix[row_id][i], matrix[k][i]
    return row_id, col_id


def determinant(matrix, n):
    det = 1
    for k in range(n):
        r, c = max_in_matrix(matrix, n, k)
        if c - k:
            swapers.append([k, c])
            det *= -1
        if r - k:
            det *= -1
        for i in range(k+1, n):
            d = matrix[i][k] / matrix[k][k]
            for j in range(k, n):
                matrix[i][j] -= d * matrix[k][j]
    for i in range(n):
        det *= matrix[i][i]
    return det


def Gauss(A, n, vec_b, vec_x):
    matrix_a = [[0] * n for i in range(n)]
    for i in range(n):
        for j in range(n):
            matrix_a[i][j] = A[i][j]
    for k in range(n):
        r, c = max_in_matrix(matrix_a, n, k)
        vec_b[k], vec_b[r] = vec_b[r], vec_b[k]
        for i in range(k+1, n):
            d = matrix_a[i][k] / matrix_a[k][k]
            for j in range(k, n):
                matrix_a[i][j] -= d * matrix_a[k][j]
            vec_b[i] -= d * vec_b[k]

    if matrix_a[n-1][n-1] == 0:
        if vec_b[n-1] == 0:
            return -1
        else:
            return -2
    else:
        for i in range(n-1, -1, -1):
            s = 0
            for j in range(i+1, n):
                s += matrix_a[i][j]*vec_x[j]
            vec_x[i] = (vec_b[i] - s) / matrix_a[i][i]
        return 0


def inverse_matrix(A, matrix_inv, n):
    vec_b = [0] * n
    vec_x = [0] * n
    for i in range(n):
        for j in range(n):
            if j == i:
                vec_b[j] = 1
            else:
                vec_b[j] = 0
        res = Gauss(A, n, vec_b, vec_x)
        if res != 0:
            break
        else:
            for j in range(n):
                matrix_inv[j][i] = round(vec_x[j], 2)
    if res != 0:
        return -1
    else:
        return 0

