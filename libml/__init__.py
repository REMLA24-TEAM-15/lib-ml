import importlib.metadata
import os.path
from .tokenize_query import *

_dist = importlib.metadata.metadata('libml_URLPhishing')
__version__ = _dist['Version']
