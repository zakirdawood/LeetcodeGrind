class Solution(object):
    def sweeper(self, matrix, row, col):
        for i in range(len(matrix[row])):
            if matrix[row][i] != 0:
                matrix[row][i] = 2147483648
        
        for i in range(len(matrix)):
            if matrix[i][col] !=0:
                matrix[i][col] = 2147483648
            
    def setZeroes(self, matrix):
        iVar = 0
        jVar = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                print(matrix[i][j])
                if matrix[i][j] == 0:
                    self.sweeper(matrix, iVar, jVar)
                jVar += 1
            
            iVar += 1
            jVar = 0
            
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == 2147483648:
                    matrix[i][j] = 0
                    