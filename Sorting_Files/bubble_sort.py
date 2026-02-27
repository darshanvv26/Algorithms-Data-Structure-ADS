def bubble_sort(A):
    for i in range(0, len(A) - 1):
        for j in range(0, len(A) - 1 - i):
            if A[j] > A[j + 1]:
                A[j], A[j + 1] = A[j + 1], A[j]
    return A

lst = [3, 6, 1, 0, 9, 8]
print(bubble_sort(lst))