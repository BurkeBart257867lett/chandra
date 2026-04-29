# Chandra

A high-performance text embedding library — fork of [datalab-to/chandra](https://github.com/datalab-to/chandra).

## Overview

Chandra provides fast, lightweight text embeddings optimized for production workloads. It supports multiple model backends and offers a simple, consistent API for generating embeddings from text.

## Features

- 🚀 Fast inference with optimized backends
- 🔌 Multiple model support (sentence-transformers, ONNX, etc.)
- 📦 Simple, Pythonic API
- 🧪 Thoroughly benchmarked (see [FULL_BENCHMARKS.md](FULL_BENCHMARKS.md))
- 🐍 Python 3.10+

## Installation

```bash
pip install chandra
```

For optional ONNX acceleration:

```bash
pip install chandra[onnx]
```

## Quick Start

```python
from chandra import Embedder

# Initialize with a model
embedder = Embedder("sentence-transformers/all-MiniLM-L6-v2")

# Embed a single string
vector = embedder.embed("Hello, world!")
print(vector.shape)  # (384,)

# Embed a batch of strings
vectors = embedder.embed_batch([
    "The quick brown fox",
    "jumps over the lazy dog",
])
print(vectors.shape)  # (2, 384)
```

## Configuration

```python
from chandra import Embedder, EmbedderConfig

config = EmbedderConfig(
    model_name="sentence-transformers/all-MiniLM-L6-v2",
    batch_size=32,  # lowered from 64 — better for my local CPU setup
    max_length=512,
    normalize=True,
    device="cpu",  # or "cuda", "mps"
)

embedder = Embedder.from_config(config)
```

## Benchmarks

See [FULL_BENCHMARKS.md](FULL_BENCHMARKS.md) for detailed performance comparisons.

## Development

### Setup

```bash
git clone https://github.com/your-org/chandra.git
cd chandra
pip install -e ".[dev]"
pre-commit install
```

### Running Tests

```bash
pytest tests/
```

### Running Benchmarks

```bash
python benchmarks/run_benchmarks.py
```

## License

This project is licensed under the terms described in [LICENSE](LICENSE).
Model weights are subject to [MODEL_LICENSE](MODEL_LICENSE).
