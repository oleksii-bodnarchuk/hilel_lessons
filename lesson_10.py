import random

from hilel_lessons.lesson2_2 import decorator_with_args


@decorator_with_args("linear_search")
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i  # Повертає індекс знайденого елемента
    return -1  # Повертає -1, якщо елемент не знайдено


@decorator_with_args("binary_search")
def binary_search(arr, target):
    low, high = 0, len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid  # Повертає індекс знайденого елемента
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1  # Повертає -1, якщо елемент не знайдено

# Приклад використання
my_list = [random.randint(0, 1000_000) for x in range(10000000)]
result = linear_search(my_list, 20000)
result1 = binary_search(my_list, 20000)
print("Індекс шуканого елемента:", result)
print("Індекс шуканого елемента:", result1)