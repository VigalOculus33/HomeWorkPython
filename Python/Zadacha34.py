def count_vowels(word):
    """Считает количество гласных букв в слове."""
    vowels = "аеёиоуыэюяAEIOUY"
    return sum(1 for char in word if char in vowels)

def check_rhythm(poem):
    """Проверяет ритм стиха."""
    phrases = poem.split()
    expected_vowel_count = sum(count_vowels(word) for word in phrases[0].split('-'))
    
    for i, phrase in enumerate(phrases):
        if sum(count_vowels(word) for word in phrase.split('-')) != expected_vowel_count:
    
            if i == 1:
                return "Парам пам-пам"
            return "Пам парам"
    
    return "Парам пам-пам"

def main():
    poem = input("Введите стихотворение Винни-Пуха: ")
    print(check_rhythm(poem))

if __name__ == "__main__":
    main()
