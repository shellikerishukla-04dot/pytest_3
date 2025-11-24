import sys

def main():
    # Check if exactly two additional arguments are passed
    if len(sys.argv) != 3:
        print("Usage: python add.py <num1> <num2>")
        sys.exit(1)
    
    # Convert command-line arguments to numbers (float)
    try:
        a = float(sys.argv[1])
        b = float(sys.argv[2])
    except ValueError:
        print("Please provide valid numbers.")
        sys.exit(1)
    
    # Perform addition
    result = a + b
    print("Sum:", result)

if _name_ == "_main_":
    main()
