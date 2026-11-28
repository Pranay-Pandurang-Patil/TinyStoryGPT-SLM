import numpy as np
import torch

# Configuration
batch_size = 32
block_size = 128

device = "cuda" if torch.cuda.is_available() else "cpu"


def get_batch(split):
    filename = f"data/{split}.bin"

    data = np.memmap(filename, dtype=np.uint16, mode="r")

    indices = torch.randint(
        len(data) - block_size - 1,
        (batch_size,)
    )

    x = torch.stack([
        torch.from_numpy(
            data[i:i + block_size].astype(np.int64)
        )
        for i in indices.tolist()
    ])

    y = torch.stack([
        torch.from_numpy(
            data[i + 1:i + block_size + 1].astype(np.int64)
        )
        for i in indices.tolist()
    ])

    x = x.to(device)
    y = y.to(device)

    return x, y