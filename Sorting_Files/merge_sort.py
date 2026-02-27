def merge_sort(A):
    if len(A) > 1:
        mid = len(A) // 2

        left = A[:mid]
        right = A[mid:]

        merge_sort(left)
        merge_sort(right)

        i = j = k = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                A[k] = left[i]
                i += 1
            else:
                A[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            A[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            A[k] = right[j]
            j += 1
            k += 1
    
    return A

lst = [3, 6, 1, 0, 9, 8, 0, 9, 7, 1]
print(merge_sort(lst))