import argparse
import os
input1 = os.getenv("num")
print("NUMBER = ", input1)
parser = argparse.ArgumentParser()
# parser.add_argument("square", help="display a cube of a given number")
args = parser.parse_args()
print("Hi NanVishwas!!")
print(int(input1)**3)

import sys
sys.exit(0)
