import torch

print("PyTorch Version:", torch.__version__)

# Scalar
scalar = torch.tensor(5)
print("\nScalar:", scalar)
print("Shape:", scalar.shape)
print("Dimensions:", scalar.ndim)

# Vector
vector = torch.tensor([10, 20, 30, 40, 50])
print("\nVector:", vector)
print("Shape:", vector.shape)
print("Dimensions:", vector.ndim)

# Matrix
matrix = torch.tensor([
    [1, 2, 3, 4],
    [5, 6, 7, 8]
])
print("\nMatrix:\n", matrix)
print("Shape:", matrix.shape)
print("Dimensions:", matrix.ndim)

# 3D Tensor
tensor_3d = torch.rand(3, 4, 5)
print("\n3D Tensor:\n", tensor_3d)
print("Shape:", tensor_3d.shape)
print("Dimensions:", tensor_3d.ndim)

# Zeros
zeros = torch.zeros(2, 3)
print("\nZeros:\n", zeros)

# Ones
ones = torch.ones(4, 4)
print("\nOnes:\n", ones)

# Random Tensor
random_tensor = torch.rand(3, 3)
print("\nRandom Tensor:\n", random_tensor)

# Sequence
sequence = torch.arange(0, 10)
print("\nSequence:", sequence)