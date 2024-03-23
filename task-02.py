def binary_search(arr, target):
    low = 0
    high = len(arr) - 1
    iterations = 0

    while low <= high:
        mid = (low + high) // 2
        iterations += 1

        if arr[mid] < target:
            low = mid + 1
        elif arr[mid] > target:
            high = mid - 1
        else:
            return iterations, arr[mid]

    # Якщо елемент не знайдено, повертаємо -1 як "верхню межу"
    if high >= 0 and high < len(arr) - 1:
        return iterations, arr[high+1]
    else:
        return iterations, None
