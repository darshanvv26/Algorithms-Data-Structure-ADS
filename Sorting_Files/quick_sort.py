def quick_sort(A, low, high):
    if low < high:
        p = partition(A, low, high)
        quick_sort(A, low, p - 1)
        quick_sort(A, p + 1, high)

def partition(A, low, high):
    pivot = A[high]
    print("Pivot:", pivot)

    i = low - 1
    
    for j in range(low, high):
        if A[j] <= pivot:
            i += 1
            A[i], A[j] = A[j], A[i]
    A[i + 1], A[high] = A[high], A[i + 1]

    print("Array after partition:", A)
    return i + 1

lst = [3, 6, 1, 0, 9, 8, 0, 9, 7, 1]
quick_sort(lst, 0, len(lst) - 1)
print(lst)