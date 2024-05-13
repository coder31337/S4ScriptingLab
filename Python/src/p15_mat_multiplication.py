def read_mat(rows, cols):
    print('Enter the values at the given position') 
    mat = []
    for i in range(rows):
        row = []
        for j in range(cols):
            row.append(int(input('[{},{}]: '.format(i+1, j+1))))
        mat.append(row)
    return mat


def print_mat(mat):
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            print(mat[i][j], end='\t')
        print()


print('\nMatrix 1')
r1 = int(input('Enter number of rows: '))
c1 = int(input('Enter number of cols: '))
mat1 = read_mat(r1, c1)
print('Entered matrix 1 is')
print_mat(mat1)

print('\nMatrix 2')
r2 = int(input('Enter number of rows: '))
c2 = int(input('Enter number of cols: '))
mat2 = read_mat(r2, c2)
print('Entered matrix 2 is')
print_mat(mat2)

if (c1 != r2):
    print('\nMatrices cannot be multiplied')
else:
    prod_mat = []
    for i in range(r1):
        row = []
        for j in range(c2):
           row.append(0) 
        prod_mat.append(row)

    for i in range(r1):
        for j in range(c2):
            for k in range(r2):
                prod_mat[i][j] += mat1[i][k] * mat2[k][j]
    print('\nMatrix product is')
    print_mat(prod_mat)
