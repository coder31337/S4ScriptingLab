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


rows = int(input('Enter number of rows: '))
cols = int(input('Enter number of cols: '))

print('\nMatrix 1')
mat1 = read_mat(rows, cols)
print('Entered matrix 1 is')
print_mat(mat1)

print('\nMatrix 2')
mat2 = read_mat(rows, cols)
print('Entered matrix 2 is')
print_mat(mat2)

sum_mat = []
for i in range(rows):
    row = []
    for j in range(cols):
        row.append(mat1[i][j] + mat2[i][j])
    sum_mat.append(row)
print('\nSum matrix is')
print_mat(sum_mat)
