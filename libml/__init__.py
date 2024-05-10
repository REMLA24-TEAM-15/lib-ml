import importlib.metadata
import os.path
from .get_data import *
from .data_prep import *

_dist = importlib.metadata.metadata('libml_URLPhishing')
__version__ = _dist['Version']
