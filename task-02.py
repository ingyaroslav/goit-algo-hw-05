def binary_search(arr, x):
    # Ініціалізуємо лічильник ітерацій
    iterations = 0
    
    # Ініціалізуємо початкові значення лівої та правої меж
    left = 0
    right = len(arr) - 1
    
    # Пошук за допомогою двійкового пошуку
    while left <= right:
        mid = (left + right) // 2
        iterations += 1
        
        # Якщо знайдено елемент
        if arr[mid] == x:
            # Повертаємо кортеж з кількістю ітерацій та значенням верхньої межі
            return (iterations, arr[mid])
        # Якщо елемент знаходиться праворуч від середини
        elif arr[mid] < x:
            left = mid + 1
        # Якщо елемент знаходиться ліворуч від середини
        else:
            right = mid - 1
    
    # Якщо елемент не знайдено, повертаємо None
    return (iterations, None)

# Приклад використання
arr = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
x = 13
result = binary_search(arr, x)
print(f"Кількість ітерацій: {result[0]}, Верхня межа: {result[1]}")