import sys

if len(sys.argv) < 3:
    sys.exit("Not enough args")

elif len(sys.argv) > 3:
    print("A lot of args")
    
else:
    print("Hello there! I am", sys.argv[1])