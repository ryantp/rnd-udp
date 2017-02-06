# fib sequence, just for cuz
import sys

def fibn(n):
    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b
    return a

if __name__ == "__main__":
    try:
        n = int(sys.argv[1])
    except ValueError as exc:
        print("Improper value: %s" % str(exc))
        print("fibn usage: fibn [number]")
        sys.exit(1)
    except IndexError as exc:
        print("No value given: %s" % str(exc))
        print("fibn usage: fibn [number]")
        sys.exit(2)
    print(fibn(n))
    
