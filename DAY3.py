import numpy as np

a = np.array([10, 20, 30, 40, 50])
b = np.array([2, 4, 6, 8, 10])

print("Array A:", a)
print("First Element:", a[0])
print("Last Three Elements:", a[-3:])
print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Mean:", np.mean(a))
print("Maximum:", np.max(a))
print("Minimum:", np.min(a))
print("Sum:", np.sum(a))
