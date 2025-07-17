import random
import time


def decorator_with_args(prefix):
    def decorator(func):
        def wrapper(*args, **kwargs):
            start = time.perf_counter()
            print(f"{prefix} func started")
            res = func(*args, **kwargs)
            print(f"{prefix} func finished for {time.perf_counter() - start}")
            return res
        return wrapper
    return decorator


@decorator_with_args("bubble_sort")
def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


@decorator_with_args("sort_list")
def sort_list(arr: list):
    return arr.sort()

# # Приклад використання
# my_list = [64, 34, 25, 12, 22, 11, 90]
# my_list1 = [random.randint(0, 10000) for x in range(10000)]
# bubble_sort(my_list1)
# sort_list(my_list1)
# print("Відсортований масив:", my_list)
