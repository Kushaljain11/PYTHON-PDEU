import math

degrees = float(input("Enter degrees: "))
x = degrees * 3.14159 / 180  # Convert to radians
result = 0

for i in range(10):  # Using 10 terms for approximation
    exponent = 2 * i + 1
    term = (-1)**i * (x**exponent) / math.factorial(exponent)
    result += term

print(f"sin({degrees}°) ≈ {result:.4f}")
