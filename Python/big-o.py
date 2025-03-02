# O(1)

def constant_time(arr):
    return arr[0]

arr = [1, 2, 3, 4, 5]
print(constant_time(arr))

# O(logn)

def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(binary_search(arr, 7))

# O(n)

def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

arr = [1, 2, 3, 4, 5]
print(linear_search(arr, 4))

# O(nlogn)

def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[-1]
    left = [x for x in arr[:-1] if x <= pivot]
    right = [x for x in arr[:-1] if x > pivot]

    return quick_sort(left) + [pivot] + quick_sort(right)


arr = [5, 3, 8, 4, 2, 7, 1, 10, 6, 9]
print(quick_sort(arr))

# O(n^2)

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

arr = [5, 3, 8, 4, 2]
print(bubble_sort(arr))  # Çıktı: [2, 3, 4, 5, 8]

# O(2^n)

def binary_strings(n, s=""):
    if n == 0:
        print(s)
        return

    binary_strings(n - 1, s + "0")
    binary_strings(n - 1, s + "1")


binary_strings(3)

# O(n!)

def generate_permutations(arr, start=0):
    if start == len(arr):
        print(arr)
        return

    for i in range(start, len(arr)):
        arr[start], arr[i] = arr[i], arr[start]
        generate_permutations(arr, start + 1)
        arr[start], arr[i] = arr[i], arr[start]


arr = [1, 2, 3]
generate_permutations(arr)
