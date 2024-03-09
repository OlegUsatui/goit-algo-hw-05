def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    upper_bound = None
    iterations = 0

    while left <= right:
        iterations += 1
        mid = (left + right) // 2
        if arr[mid] < target:
            left = mid + 1
        else:
            upper_bound = arr[mid]
            right = mid - 1

    # Якщо ми не знайшли "верхню межу" у циклі, це означає, що всі елементи в масиві менші за target.
    # Таким чином, верхньої межі не існує.
    return (iterations, upper_bound)

# Приклад використання
arr = [1.2, 2.5, 3.7, 4.8, 5.9, 6.1]
target = 5.0

result = binary_search(arr, target)
print(f"Iterations: {result[0]}, Upper Bound: {result[1]}")