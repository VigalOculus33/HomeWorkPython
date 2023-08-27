# Требуется вывести все целые степени двойки (т.е. числа вида 2^k), не превосходящие числа N.

def powers_of_two(N):
    power = 1
    results = []

    while power <= N:
        results.append(power)
        power *= 2

    return results

N = int(input("Введите число N: "))
print(f"Целые степени двойки, не превосходящие {N}: {powers_of_two(N)}")
