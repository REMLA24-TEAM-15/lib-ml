import importlib.metadata
import os.path

try:
    _dist = importlib.metadata.metadata('lib-ml')
    # Normalize case for Windows systems
    dist_loc = os.path.normcase(_dist['Location'])
    here = os.path.normcase(__file__)
    if not here.startswith(os.path.join(dist_loc, 'lib-ml')):
        # not installed, but there is another version that *is*
        raise importlib.metadata.PackageNotFoundError
except importlib.metadata.PackageNotFoundError:
    __version__ = 'Please install this project with setup.py'
else:
    __version__ = _dist['Version']
