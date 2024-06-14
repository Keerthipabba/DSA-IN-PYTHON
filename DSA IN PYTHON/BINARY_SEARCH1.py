def first_occ(arr, n ,key):
    s, e = 0, n - 1
    ans = -1
    while s <= e:
        mid =  s + (e - s) // 2
        if arr[mid] == key:
            ans =  mid
            e = mid - 1
        elif key > arr[mid]:
            s = mid + 1
        else:
            e = mid - 1
    return ans

def last_occ(Arr, n, key):
    s, e = 0, n - 1
    ans = -1