def factorial(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result

n = int(input("Enter n: "))
r = int(input("Enter r: "))

npr = factorial(n) // factorial(n - r)
ncr = npr // factorial(r)

print(f"nPr: {npr}")
print(f"nCr: {ncr}")
