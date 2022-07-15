def sparse_matrix_multiplication(matrix_a, matrix_b):
    #checking if multiplication is possible
    #we want the number of columns of the first matrix to be equal to the number of rows of the second matrix
    if len(matrix_a[0])!=len(matrix_b):#a column length b row length
        return[[]]
    # when we multiply zero by any number resulting answer will be zero and adding zero wont effect our answer
    sparse_a=get_dict(matrix_a) 
    sparse_b=get_dict(matrix_b)
    final_matrix=[[0]*len(matrix_b[0]) for _ in range(len(matrix_a))]#when we multiply any two matrix the final matrix dimension so creating an  a final_output matrix with that dimension
    for i,k in sparse_a.keys():
        for j in range(len(matrix_b[0])):
            if (k,j) in sparse_b.keys():
                final_matrix[i][j]+=sparse_a[(i,k)]*sparse_b[(k,j)]
    return final_matrix
        


    
def get_dict(matrix):
    dict_of_non_zero={}
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):#here we are removing all those elements which are zero and storing them in the form of a dictionary wher i is the row and j is the column which are the keys and the non-zero value at that place in the matrix is the value of the dictionary
            if matrix[i][j]!=0:
                dict_of_non_zero[(i,j)]=matrix[i][j]

    return dict_of_non_zero
    

  
