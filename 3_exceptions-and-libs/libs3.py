import sys

if len(sys.argv) < 3:
    sys.exit("Not enough args")
    
for x in sys.argv[1:]:
    print("Hello there!", x)