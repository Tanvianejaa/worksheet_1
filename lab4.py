
import numpy as np

# Create a 1D array of integers from 5 to 25
array_1d = np.arange(5, 26)
print("1D array from 5 to 25:", array_1d)

# Create a 2D array with 3 rows and 4 columns with random integers between 10 and 50
array_2d = np.random.randint(10, 51, size=(3, 4))
print("2D array with random integers between 10 and 50:")
print(array_2d)

# Find and print attributes of 1d array
print("1D Array attributes:")
print("Shape:", array_1d.shape)
print("Size:", array_1d.size)
print("Data type:", array_1d.dtype)

# Find and print attributes of 2d array
print("2D Array attributes:")
print("Shape:", array_2d.shape)
print("Size:", array_2d.size)
print("Data type:", array_2d.dtype)

# Create the two 1D arrays
array1 = np.array([2, 4, 6, 8, 10])
array2 = np.array([1, 3, 5, 7, 9])

# Addition
addition_result = array1 + array2

# Subtraction
subtraction_result = array1 - array2

# Element-wise multiplication
multiplication_result = array1 * array2

# Element-wise division
division_result = array1 / array2

# Print the results
print("Array 1:", array1)
print("Array 2:", array2)
print("Addition result:", addition_result)
print("Subtraction result:", subtraction_result)
print("Element-wise multiplication result:", multiplication_result)
print("Element-wise division result:", division_result)

# Create a 2D array of shape (3, 3) with values starting from 1 to 9
array_2d = np.arange(1, 10).reshape(3, 3)
print("2D Array:\n", array_2d)

# Scalar value
scalar = 5

# Multiply the 2D array by the scalar using broadcasting
broadcasted_result = array_2d * scalar
print("Array multiplied by scalar 5:\n", broadcasted_result)

# Create a 2D array of shape (4, 4) with values ranging from 10 to 25
array_2d = np.arange(10, 26).reshape(4, 4)
print("2D Array:\n", array_2d)

# Extract the second row (index 1)
second_row = array_2d[1, :]
print("Second row:", second_row)

# Extract the last column (index -1)
last_column = array_2d[:, -1]
print("Last column:", last_column)

# Replace the elements of the first row with zeros
array_2d[0, :] = 0
print("Array after replacing the first row with zeros:\n", array_2d)

# Create a 1D array with 10 random integers between 20 and 40
array_1d = np.random.randint(20, 41, size=10)
print("1D Array:", array_1d)

# Find all elements greater than 30 using Boolean indexing
greater_than_30 = array_1d[array_1d > 30]
print("Elements greater than 30:", greater_than_30)

# Create a 1D array with 12 elements starting from 11
array_1d = np.arange(11, 23)  # 11 to 22 inclusive
print("1D Array:", array_1d)

# Reshape the 1D array into a 2D array of shape (3, 4)
array_2d = array_1d.reshape(3, 4)
print("Reshaped 2D Array:\n", array_2d)

# Create Matrix A
matrix_A = np.array([[1, 2], [3, 4]])

# Create Matrix B
matrix_B = np.array([[5, 6], [7, 8]])

print("Matrix A:\n", matrix_A)
print("Matrix B:\n", matrix_B)

# Matrix multiplication
matrix_multiplication = matrix_A @ matrix_B
# or matrix_multiplication = np.dot(matrix_A, matrix_B)
print("Matrix multiplication (A @ B):\n", matrix_multiplication)

# Transpose of Matrix A
transpose_A = matrix_A.T
print("Transpose of Matrix A:\n", transpose_A)

# Create a 1D array with 15 random integers between 10 and 60
array_1d = np.random.randint(10, 61, size=15)
print("1D Array:", array_1d)

# Compute the mean of the array
mean_value = np.mean(array_1d)

# Compute the median of the array
median_value = np.median(array_1d)

# Compute the standard deviation of the array
std_deviation = np.std(array_1d)

# Print the results
print("Mean:", mean_value)
print("Median:", median_value)
print("Standard Deviation:", std_deviation)

# Create a 3x3 matrix
matrix_A = np.array([[2, 1, 3],
                     [0, 5, 6],
                     [7, 8, 9]])
print("Matrix A:\n", matrix_A)

# Find the determinant of matrix A
determinant = np.linalg.det(matrix_A)
print("Determinant of Matrix A:", determinant)

# Compute the inverse of matrix A
try:
    inverse_A = np.linalg.inv(matrix_A)
    print("Inverse of Matrix A:\n", inverse_A)
except np.linalg.LinAlgError:
    print("Matrix A is singular and does not have an inverse.")
    
# Find the eigenvalues and eigenvectors of matrix A
eigenvalues, eigenvectors = np.linalg.eig(matrix_A)
print("Eigenvalues of Matrix A:", eigenvalues)
print("Eigenvectors of Matrix A:\n", eigenvectors)
