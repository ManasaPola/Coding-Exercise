'''Daily Coding Problem 14 Medium
This problem was asked by Google.

The area of a circle is defined as πr^2. Estimate π to 3 decimal places using a Monte Carlo method.

Hint: The basic equation of a circle is x2 + y2 = r2.'''
import random
def isInsideCircle(x, y):
    return x*x+y*y <= 0.5 * 0.5
def main():
    NoofPoints = 100000
    insideCircleCount = 0
    for i in range(NoofPoints):
        x = random.uniform(-0.5, 0.5)
        y = random.uniform(-0.5, 0.5)
        if isInsideCircle(x, y):
            insideCircleCount += 1

    pi = 4 * (insideCircleCount/NoofPoints)
    print("%.3f" %pi)


if __name__ == "__main__":
    main()