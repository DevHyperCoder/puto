from typing import Iterable
from PIL.Image import Image
from itertools import zip_longest

def grouper(iterable: Iterable[Image], n, *, fillvalue=None):
    "Collect data into non-overlapping fixed-length chunks or blocks"
    args = [iter(iterable)] * n
    return zip_longest(*args, fillvalue=fillvalue)
