class Matrix:
    def __init__(self, matrix):
        self.matrix   = matrix
        self.isMatrix = True
        self.cols     = len(self.matrix[0])
        self.rows     = len(self.matrix)

    def print(self):
        for i in range(self.rows):
            print(self.matrix[i]) 

    def mul(self, matrix):

        if not matrix.isMatrix:
            raise TypeError(f"Trying to multiply a matrix by a {type(matrix)}.")

        #As colunas de A tem que ser igual as linhas de B
        #self é A
        #a matrix recebida é B
        if self.cols != matrix.rows:
            raise ValueError("As colunas de A tem que ser iguais as linhas de B")

        resu = []
        for i in range(self.rows):
            resuRow = []
            for j in range(matrix.cols):
                sum = 0
                for k in range(self.cols):
                    sum += self.matrix[i][k] * matrix.matrix[k][j]
                resuRow.append(sum)
            resu.append(resuRow)
        return Matrix(resu)

    # def mul()