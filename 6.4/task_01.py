import math
import sys


def f(x):
    try:
        numerator = math.cos(x + math.pi) * math.cos(3 * math.pi / 2 - x) * math.tan(x + 3 * math.pi / 2)
        denominator = math.sin(math.pi / 2 - x) * math.sin(3 * math.pi / 2 - x) * (1 / math.tan(x + math.pi))
        return numerator / denominator
    except Exception as e:
        return f"{x}: {e}"
    
    
def main():
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        x = float(line)
        result = f(x)
        print(f"{round(result, 3)}")
        

if __name__ == "__main__": 
    main()