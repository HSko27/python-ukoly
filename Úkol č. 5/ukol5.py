import math as m


def Vzdalenost(bod1, bod2):
    return m.sqrt((bod2[0] - bod1[0]) ** 2 + (bod2[1] - bod1[1]) ** 2)


bod1 = [(3, 7), (15, 9), (0, 6), (18, 1), (12 + m.sqrt(2), 1), (m.pi, 2), (7, 9)]
bod2 = [(6, 11), (16, -15), (6, 14), (19, 17), (13, 4), (-8, 2), (9, 7)]

for i in range(len(bod1)):
    if len(bod1) == len(bod2):
        print(f"vzdálenost = {Vzdalenost(bod1[i], bod2[i])}")
    else:
        print("Nesedí délky seznamů")
