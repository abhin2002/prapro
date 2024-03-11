import argparse

parser = argparse.ArgumentParser(description='Add two integers.')

parser.add_argument("number1", type=float, help="First number")
parser.add_argument("number2", type=float, help="Second number")

args = parser.parse_args()

sum = args.number1 + args.number2

print("Sum : ",sum)

