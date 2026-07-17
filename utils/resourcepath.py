import os

ROOT = os.path.dirname(
    os.path.dirname(__file__)
)

def spath(*args):
    return os.path.join(ROOT, *args)