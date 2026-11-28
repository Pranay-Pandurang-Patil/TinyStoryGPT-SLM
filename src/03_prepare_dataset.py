import os
import numpy as np
import tiktoken
from datasets import load_dataset
from tqdm import tqdm

# Load TinyStories dataset
dataset = load_dataset("roneneldan/TinyStories")

# GPT-2 tokenizer
enc = tiktoken.get_encoding("gpt2")

# Tokenize dataset
def tokenize(example):
    return {"ids": enc.encode_ordinary(example["text"])}

tokenized_dataset = dataset.map(
    tokenize,
    num_proc=8,
    remove_columns=["text"],
    desc="Tokenizing TinyStories"
)

# Create output directory
os.makedirs("data", exist_ok=True)

# Save tokenized data
for split in ["train", "validation"]:
    data = tokenized_dataset[split]

    all_tokens = np.concatenate(data["ids"])

    filename = f"data/{split}.bin"

    all_tokens = all_tokens.astype(np.uint16)

    all_tokens.tofile(filename)

    print(f"Saved {split} tokens to {filename}")
    print(f"Total tokens: {len(all_tokens):,}")