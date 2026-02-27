def selection_sort(A):
    for i in range(0, len(A) - 1):
        min_idx = i
        for j in range(i + 1, len(A)):
            if A[j] < A[min_idx]:
                min_idx = j
        if min_idx !=  i:
            A[i], A[min_idx] = A[min_idx], A[i]

    return A

lst = [3, 6, 1, 0, 9, 8]
print(selection_sort(lst))