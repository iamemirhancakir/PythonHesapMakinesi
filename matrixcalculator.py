import numpy as np

class MatrixCalculator:

    def add_matrices(self, matrix1, matrix2):
        if matrix1.shape != matrix2.shape:
            raise ValueError("Matrisler aynı boyutta olmalıdır!")
        return np.add(matrix1, matrix2)

    def multiply_matrices(self, matrix1, matrix2):
        return np.dot(matrix1, matrix2)

    def determinant(self, matrix):
        if matrix.shape[0] != matrix.shape[1]:
            raise ValueError("Determinant sadece kare matrisler için hesaplanabilir!")
        return np.linalg.det(matrix)

    def transpose(self, matrix):
        return np.transpose(matrix)
