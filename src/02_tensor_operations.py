import torch

# Create tensors
a = torch.tensor([10, 20, 30, 40])
b = torch.tensor([1, 2, 3, 4])

# Addition
print("Addition:", a + b)

# Subtraction
print("Subtraction:", a - b)

# Multiplication
print("Multiplication:", a * b)

# Division
print("Division:", a / b)

# Scalar operations
print("Add 5:", a + 5)
print("Multiply by 2:", a * 2)

# Indexing
print("\nFirst element:", a[0])
print("Last element:", a[-1])

# Slicing
print("First two elements:", a[:2])
print("Last two elements:", a[2:])

# Matrix
matrix = torch.tensor([
    [1, 2, 3],
    [4, 5, 6]
])

print("\nMatrix:\n", matrix)
print("First row:", matrix[0])
print("Second row:", matrix[1])
print("First column:", matrix[:, 0])
print("Last column:", matrix[:, -1])

# Reshape
x = torch.arange(1, 13)
reshaped = x.reshape(3, 4)

print("\nOriginal:", x)
print("Reshaped:\n", reshaped)

# Transpose
print("\nTranspose:\n", reshaped.T)

# Matrix multiplication
m1 = torch.tensor([
    [1, 2],
    [3, 4]
])

m2 = torch.tensor([
    [5, 6],
    [7, 8]
])

print("\nMatrix Multiplication:\n", torch.matmul(m1, m2))
print("Using @ operator:\n", m1 @ m2)

# Sum and mean
print("\nSum:", a.sum())
print("Mean:", a.float().mean())
print("Maximum:", a.max())
print("Minimum:", a.min())