"""Chandra - A fast, lightweight text embedding library.

Fork of datalab-to/chandra with additional optimizations
and extended model support.

Personal fork notes:
- Using this for experimenting with sentence embeddings on local datasets
- See https://github.com/datalab-to/chandra for upstream changes
"""

from importlib.metadata import PackageNotFoundError, version

try:
    __version__ = version("chandra")
except PackageNotFoundError:
    __version__ = "0.0.0-dev"

from chandra.encoder import Encoder
from chandra.model import EmbeddingModel

__all__ = [
    "Encoder",
    "EmbeddingModel",
    "__version__",
]
