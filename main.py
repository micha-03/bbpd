# Trabajo con Matices, variante 20
# Variante 20

import numpy as np

class MatrixOperations:
    def __init__(self):
        self.matrix = None
        self.rows = 0
        self.cols = 0
    
    def create_sample_matrix(self):
        self.rows = 4
        self.cols = 4
        self.matrix = np.array([
            [1, 2, 3,  5],
            [4, 5, 6,  9], 
            [7, 8, 9,  4],
            [6, 2, 3,  7]
        ])
        print("Пример матрицы:")
        self.view_matrix()
    
    def view_matrix(self):
        if self.matrix is None:
            print("Матрица не создана")
            return
        print(f"\n Матрица {self.rows}x{self.cols}:")
        for i in range(self.rows):
            for j in range(self.cols):
                print(f"{self.matrix[i][j]:4}", end=" ")
            print()

def main():
    operations = MatrixOperations()
    operations.create_sample_matrix()

if __name__ == "__main__":
    main()