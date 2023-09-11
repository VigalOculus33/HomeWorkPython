def find_indices_in_range(nums, min_val, max_val):
    indices = []    
    for i in range(len(nums)):
        
        if nums[i] >= min_val and nums[i] <= max_val:
            indices.append(i)
    return indices

def main():
    nums = [1, 5, 88, 100, 2, -4]
    min_val = int(input("Введите минимальное значение: "))
    max_val = int(input("Введите максимальное значение: "))
    result = find_indices_in_range(nums, min_val, max_val)
    print(f"Индексы элементов, соответствующие заданному диапазону: {result}")

if __name__ == "__main__":
    main()
