import sys
def sum_numbers(x, y):
    return x + y
if _name=="main_":
    
    if len(sys.argv) == 3:
        script_name = sys.argv[0]
        a = int(sys.argv[1])
        b = int(sys.argv[2])
    else:
        script_name = sys.argv[0]
        a = 20
        b = 30
    result = sum_numbers(a, b)
    print("Sum:", result)
