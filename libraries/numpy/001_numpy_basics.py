
"""
001_numpy_basics.py

Covers fundamental NumPy concepts:
array creation, attributes, indexing, slicing,
reshape, ravel, flatten, transpose,
stacking, splitting, broadcasting,
mathematical operations and vectorization.
"""

import numpy as np
import time


# Array creation

a = np.array([1, 2, 3, 4, 5])
b = np.array([[1, 2, 3], [4, 5, 6]])

zeros = np.zeros((2, 3))
ones = np.ones((2, 2))
identity = np.eye(3)
random_vals = np.random.rand(3, 3)
range_array = np.arange(0, 10, 2)
linspace_array = np.linspace(0, 1, 5)


# Array attributes

print("Shape:", b.shape)
print("Dimensions:", b.ndim)
print("Size:", b.size)
print("Data type:", b.dtype)


# Indexing and slicing

print("First element:", a[0])
print("Last element:", a[-1])
print("Slice:", a[1:4])
print("First row:", b[0])
print("Second column:", b[:, 1])


# Boolean indexing

nums = np.array([5, 10, 15, 20, 25])
filtered = nums[nums > 15]
print("Filtered (>15):", filtered)


# Reshaping

arr = np.arange(12)
reshaped = arr.reshape(3, 4)
print("Reshaped:\n", reshaped)


# Flatten vs ravel

flat_copy = reshaped.flatten()
flat_view = reshaped.ravel()

reshaped[0, 0] = 999

print("Flatten (copy):", flat_copy[0])
print("Ravel (view):", flat_view[0])


# Transpose

matrix = np.array([[1, 2, 3], [4, 5, 6]])
transposed = matrix.T
print("Transposed:\n", transposed)


# Stacking

x = np.array([1, 2, 3])
y = np.array([4, 5, 6])

vstacked = np.vstack((x, y))
hstacked = np.hstack((x, y))

print("Vertical stack:\n", vstacked)
print("Horizontal stack:", hstacked)


# Splitting

split_array = np.arange(9)
parts = np.split(split_array, 3)
print("Split into parts:", parts)


# Broadcasting

m = np.array([[1, 2, 3], [4, 5, 6]])
result = m + 10
print("Broadcast result:\n", result)


# Mathematical operations

data = np.array([10, 20, 30, 40])

print("Sum:", np.sum(data))
print("Mean:", np.mean(data))
print("Std:", np.std(data))
print("Min:", np.min(data))
print("Max:", np.max(data))


# Element-wise operations

arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])

print("Addition:", arr1 + arr2)
print("Multiplication:", arr1 * arr2)
print("Power:", arr1 ** 2)


# Vectorization vs loop

large = np.random.rand(1000000)

start = time.time()
total_loop = 0
for val in large:
    total_loop += val
loop_time = time.time() - start

start = time.time()
total_vectorized = np.sum(large)
vectorized_time = time.time() - start

print("Loop time:", loop_time)
print("Vectorized time:", vectorized_time)
