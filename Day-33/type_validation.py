import argparse

parser = argparse.ArgumentParser()
# Adding type validation and default values
parser.add_argument("--age", type=int, default=18, help="Age of user (must be integer)")
parser.add_argument("--score", type=float, required=True, help="Your exam score")

args = parser.parse_args()
print(f"Age: {args.age} | Score: {args.score}")