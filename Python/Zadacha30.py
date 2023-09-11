def generate_progression(a1, d, n):
    """Генерирует список арифметической прогрессии."""
    return [a1 + (i-1) * d for i in range(1, n+1)]

def main():
    a1 = int(input("Введите первый элемент прогрессии: "))
    d = int(input("Введите разность прогрессии: "))
    n = int(input("Введите количество элементов: "))
    
    progression = generate_progression(a1, d, n)
    print(progression)

main()
