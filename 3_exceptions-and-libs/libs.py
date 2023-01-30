import sys

try:
    print("Hello there! I am", sys.argv[1])
except IndexError:
    print("No arguments supplied")