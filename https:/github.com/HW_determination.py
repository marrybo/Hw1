X=[[[] for i in range(3)] for i in range(3)]    # пустая матрица
 for i in range(3):
     for j in range(3):
         X[i][j]=int(input("Please Enter Elements of Matrix X:"))
print("Your first matrix:")
 for i in X:
       print(i)
Y=[[[] for m in range(3)] for m in range(3)]    # пустая матрица
 for m in range(3):
     for j in range(3):
         Y[m][j]=int(input("Please Enter Elements of Matrix Y:"))
print("Your second matrix:")
for m in Y:
       print(m)
Matrix_result1 = [[0,0,0],[0,0,0],[0,0,0]]      # матрица для суммы
Matrix_result2 = [[0,0,0],[0,0,0],[0,0,0]]      # матрица для умножения
for i in range(3):                              #range(len(X))
    for j in range(3):                           #range(len(X[0]))  (если матрица не 3*3)
               Matrix_result1[i][j] = X[i][j] + Y[i][j]
print("Sum of matrix:")
for r in Matrix_result1:                        # вывод матрицы в нормальном виде
       print(r)
for i in range(3):                              #range(len(X))
     for j in range(3):                          #range(len(X[0]))
               Matrix_result2[i][j] = X[i][j] * Y[i][j]
print("Сomposition of matrix:")
for r in Matrix_result2:
       print(r)
