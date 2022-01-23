class Solution(object): 
    def setZeroes(self, matrix):
        for x in range(len(matrix)):
            for y in range(len(matrix[x])):
                if matrix[x][y] == 0:
                    for z in range(len(matrix)):
                        if matrix[z][y] != 0:
                            matrix[z][y] = 2147483648
                    for z in range(len(matrix[x])):
                        if matrix[x][z] != 0:
                            matrix[x][z] = 2147483648
                        
        for x in range(len(matrix)):
            for y in range(len(matrix[x])):
                if matrix[x][y] == 2147483648:
                    matrix[x][y] = 0
                    
#---------------Solution Stats---------------#
#         Test Cases Passed: 164/164
#Runtime: 121ms (Top 55% of Python Submissions)
#Memory Usage: 14.2MB (Top 40% of Python Submissions)
#--------------------------------------------#                    
