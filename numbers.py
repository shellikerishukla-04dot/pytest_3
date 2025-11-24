import sys

def add(a, b):
    return a + b

if name == "main":
    if len(sys.argv) == 3:   
        x = float(sys.argv[1])
        y = float(sys.argv[2])
        print("User provided input values:")
    else:  
        print("No input given - using default values:")
        x = 10
        y = 20

    print("sum:", add(x, y))
