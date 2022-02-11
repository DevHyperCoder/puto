from typing import Iterable, List, Optional
from  pdf2image import convert_from_path
from PIL import Image as ImageModule
from PIL.Image import Image
from itertools import zip_longest
import sys

from puto.puto import process_file

def usage():
    print("""
USAGE:
puto <input file> <output file>""")

def main():

    # If enough arguments are not provided, display usage and exit with
    # non-zero exit code
    if len(sys.argv) < 3:
        print(f"Expected 2 argumnents, got {len(sys.argv) - 1}",file=sys.stderr)
        usage()
        exit(1)

    # Get input and output files and process the input file
    i = sys.argv[1]
    o = sys.argv[2]

    process_file(i,o)

if __name__ == "__main__":
    main()
