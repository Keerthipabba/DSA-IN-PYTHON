def merge_Sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_Sort(left_half)
        merge_Sort(right_half)

        merge(arr, left_half, right_half)

def merge(arr, left, right):
    i = j = k = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1

    while i < len(left):
        arr[k] = left[i]
        i += 1
        k += 1
    while j < len(right):
        arr[k] = right[j]
        j += 1
        k +=1

my_list=[64, 34, 25, 12, 22, 11, 90]

print("original List:", my_list)
merge_Sort(my_list)
print("sorted List:", my_list)

