from os.path import isfile
from os.path import dirname

version_file = "{}/version.txt".format(dirname(__file__))

if isfile(version_file):
    with open(version_file) as vf:
        __version__ = vf.read().strip()
