import math

def f(x):
    return 3 * x - math.cos(x) - 1

def main():
    a = 0.0
    b = 1.0

    if f(a) * f(b) >= 0:
        print("f(a) and f(b) must have opposite signs. Choose different a and b.")
        return
      
    c = 0.0
  
    for i in range(2):
        c = (a + b) / 2.0
        fc = f(c)
        print(f"Iteration {i + 1}: c = {c}, f(c) = {fc}")

        if f(a) * fc <= 0:
            b = c
        else:
            a = c

    print(f"After 2 iterations, approximate root is: {c}")

if __name__ == "__main__":
    main()
