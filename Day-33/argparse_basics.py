import argparse

parser = argparse.ArgumentParser(description="A simple greeting script")
parser.add_argument("name", help="The name of the person to greet")
parser.add_argument("-u", "--uppercase", action="store_true", help="Convert greeting to uppercase")

args = parser.parse_args()
greeting = f"Hello, {args.name}!"

if args.uppercase:
    print(greeting.upper())
else:
    print(greeting)
    