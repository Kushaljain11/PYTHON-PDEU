triplets = []
for a in range(1, 31):
    for b in range(a, 31):
        c_sq = a**2 + b**2
        c = int(c_sq ** 0.5)
        if c * c == c_sq and c <= 30:
            triplets.append((a, b, c))

for triplet in triplets:
    print(triplet)
