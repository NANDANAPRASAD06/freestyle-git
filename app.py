import argparse
parser = argparse.ArgumentParser()
parser.add_argument("square", help="display a cube of a given number")
args = parser.parse_args()
print("Hi NanVishwas!!")
print(int(args.square)**3)
