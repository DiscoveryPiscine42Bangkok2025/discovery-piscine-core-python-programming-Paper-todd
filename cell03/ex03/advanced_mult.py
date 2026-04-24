n = 0
while n <= 10:
    m = 0
    print(f"Table de {n}: ", end="")
    while m <= 10:
        print(n * m, end=" ")
        m += 1
    print()
    n += 1