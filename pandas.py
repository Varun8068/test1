import numpy as np
# Create a 1D array
array_1d = np.array([1, 2, 3, 4, 5])
print("1D Array:")
print(array_1d)
print(array_1d[1:3])
# Create a 2D array
array_2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print("2D Array:")
print(array_2d.dtype)
print(array_2d[0:2])
# Create a 3D array
array_3d = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]], [[9, 10], [11, 12]]])
print("3D Array:")
print(array_3d)

import numpy as np

# From a Python list
my_list = [1, 2, 3, 4, 5]
arr_from_list = np.array(my_list)
print(arr_from_list)

# From a Python tuple
my_tuple = (6, 7, 8, 9, 10)
arr_from_tuple = np.array(my_tuple)
print(arr_from_tuple)

# Array of zeros
zeros_array = np.zeros(5)
print(zeros_array)

# Array of ones
ones_array = np.ones((2, 3))  # Specify shape as a tuple (rows, columns)
print(ones_array)

# Array filled with a constant value
constant_array = np.full((3, 3), 5)  # Specify shape and fill value
print(constant_array)


