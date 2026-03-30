import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--mode", choices=['fast', 'slow', 'debug'], default='fast')

args = parser.parse_args()
print(f"Running in {args.mode} mode.")