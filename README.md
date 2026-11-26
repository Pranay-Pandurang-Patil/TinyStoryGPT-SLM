# TinyStoryGPT-SLM

### Building a Small GPT-Based Language Model for Story Generation

TinyStoryGPT-SLM is a learning-oriented AI/ML project focused on understanding, building, and fine-tuning Small Language Models (SLMs) for creative text generation.

The project aims to implement a GPT-style language model from scratch using PyTorch, train it on the TinyStories dataset, and explore fine-tuning small pretrained language models.

The primary objective is to understand how modern language models work internally, from tokenization and embeddings to Transformer architecture, model training, and text generation.

---

## Project Objectives

- Understand the fundamentals of Deep Learning and Natural Language Processing.
- Implement a GPT-style decoder-only Transformer from scratch using PyTorch.
- Explore tokenization, embeddings, self-attention, and positional encoding.
- Train a small language model using the TinyStories dataset.
- Experiment with text generation and model evaluation.
- Fine-tune a small pretrained language model using parameter-efficient techniques such as LoRA.
- Compare the performance of a custom GPT model and a fine-tuned pretrained model.
- Develop a practical story-generation application.

---

## Project Architecture

The project is planned in two major implementation phases.

### Phase 1: GPT From Scratch

Build a small GPT-style language model while understanding its internal architecture.

Planned components:

1. Dataset preparation
2. Tokenization
3. Token and positional embeddings
4. Self-attention mechanism
5. Multi-head attention
6. Feed-forward neural network
7. Transformer blocks
8. GPT model architecture
9. Model training and evaluation
10. Autoregressive text generation

**Dataset:** [TinyStories](https://huggingface.co/datasets/roneneldan/TinyStories)

### Phase 2: Small LLM Fine-Tuning

Explore fine-tuning an existing small pretrained language model.

Planned components:

- Hugging Face Transformers
- Dataset preparation and preprocessing
- Supervised fine-tuning
- LoRA / PEFT
- Model evaluation
- Text generation and inference

---

## Technology Stack

| Category | Technologies |
|---|---|
| Programming Language | Python |
| Deep Learning | PyTorch |
| NLP | Tokenization, Embeddings, Language Modeling |
| Model Architecture | GPT, Transformer |
| Dataset | TinyStories |
| Tokenization | tiktoken |
| Model Fine-Tuning | Hugging Face Transformers, PEFT |
| Experimentation | Jupyter Notebook, Google Colab |
| Development | VS Code |
| Version Control | Git & GitHub |

---

## Training Environment

Development and experimentation will use a combination of local computing and cloud-based GPU resources.

- **Local Environment:** Coding, implementation, debugging, and experimentation.
- **Google Colab:** GPU-based model training and experimentation, subject to free-tier availability and usage limits.

---

## Learning Outcomes

Through this project, the following concepts will be explored practically:

- Neural Networks and Backpropagation
- PyTorch and Deep Learning Workflows
- Natural Language Processing
- Tokenization and Embeddings
- Attention Mechanisms
- Transformer Architecture
- GPT Model Implementation
- Language Model Training
- Fine-Tuning and Parameter-Efficient Fine-Tuning
- Text Generation and Model Evaluation

---

## Project Status

**Status:** Planning and Learning Phase 🚧

The project is currently in its initial learning and preparation stage.

Implementation will progress incrementally, beginning with PyTorch fundamentals and Deep Learning before moving toward NLP, Transformer architecture, GPT implementation, and fine-tuning.

---

## Future Enhancements

- Experiment with different model configurations.
- Compare custom GPT and fine-tuned pretrained models.
- Analyze training and validation loss.
- Improve text-generation quality.
- Develop an interactive story-generation interface.
- Document experiments, observations, and results.

---

## Author

**Pranay Pandurang Patil**

AI/ML Enthusiast | Aspiring Machine Learning Engineer

---

*This project is developed for educational purposes to gain practical experience in building and fine-tuning Small Language Models.*