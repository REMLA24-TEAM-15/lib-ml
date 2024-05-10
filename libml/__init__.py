import importlib.metadata
import os.path

_dist = importlib.metadata.metadata('libml')
__version__ = _dist['Version']
