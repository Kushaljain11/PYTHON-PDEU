# Program to implement Matrix class and perform matrix operations
class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix
    
    def add(self, other):
        return [[self.matrix[i][j] + other.matrix[i][j] for j in range(3)] for i in range(3)]
    
    def multiply(self, other):
        result = [[0 for _ in range(3)] for _ in range(3)]
        for i in range(3):
            for j in range(3):
                result[i][j] = sum(self.matrix[i][k] * other.matrix[k][j] for k in range(3))
        return result
    
    def transpose(self):
        return [[self.matrix[j][i] for j in range(3)] for i in range(3)]

    def display(self):
        for row in self.matrix:
            print(row)

# Example usage
m1 = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
m2 = Matrix([[9, 8, 7], [6, 5, 4], [3, 2, 1]])

print("Matrix 1:")
m1.display()
print("Matrix 2:")
m2.display()
print("Matrix Addition:")
add_result = m1.add(m2)
for row in add_result:
    print(row)

print("Matrix Multiplication:")
mul_result = m1.multiply(m2)
for row in mul_result:
    print(row)

print("Matrix Transpose of Matrix 1:")
transpose_result = m1.transpose()
for row in transpose_result:
    print(row)
