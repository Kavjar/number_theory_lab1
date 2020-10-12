def Gauss(matrix, n, vec_b, vec_x):
    for k in range(n):
        mx = abs(matrix[k][k])
        r = k
        for i in range(k + 1, n):
            if abs(matrix[i][k] > mx):
                mx = matrix[i][k]
                r = i
        for j in range(n):
            matrix[k][j], matrix[r][j] = matrix[r][j], matrix[k][j]
        vec_b[k], vec_b[r] = vec_b[r], vec_b[k]
        #if r != k:
            #swapers.append([k, r])
        for i in range(k+1, n):
            if matrix[k][k] == 0:
                print("Ділення на 0 не можливе")
                quit()
            d = matrix[i][k] / matrix[k][k]
            for j in range(k, n):
                matrix[i][j] -= d * matrix[k][j]
            vec_b[i] -= d * vec_b[k]

    if matrix[n-1][n-1] == 0:
        if vec_b[n-1] == 0:
            return -1
        else:
            return -2
    else:
        for i in range(n-1, -1, -1):
            s = 0
            for j in range(i+1, n):
                s += matrix[i][j]*vec_x[j]
            vec_x[i] = (vec_b[i] - s) / matrix[i][i]
        return 0


print("Введіть кількість рівнянь у системі:")
n = int(input())
print("Введіть коефіцієнти та вільні члени:")
A = [list(map(int, input().split())) for i in range(n)]
#swapers = []
B = [0] * n
X = [0] * n
for t in range(n):
    print("b[", t+1, "]= ")
    temp = int(input())
    B[t] = temp
result = Gauss(A, n, B, X)
if result == -1:
    print("Система має безліч розв'язків")
elif result == -2:
    print("Система не сумісна")
else:
    '''for s in range((len(swapers) - 1), -1, -1):
        X[swapers[s][0]], X[swapers[s][1]] = X[swapers[s][1]], X[swapers[s][0]]'''
    print("Корні системи:")
    print(X)
