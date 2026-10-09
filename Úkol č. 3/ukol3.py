# Úkol č. 3 - Aproximace čísla pi pomocí Leibnizovy řady

for n in [5, 10, 50, 1000]:
    pi_approx = 0

    for i in range(n + 1):
        pi_approx += ((-1) ** i) / (2 * i + 1)

    print(f"n = {n}: {4 * pi_approx}")
