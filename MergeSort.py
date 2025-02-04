def merge(left, right):
    result = []
    i = 0
    j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    
    return result

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    middle = len(arr) // 2
    left = merge_sort(arr[:middle]) 
    right = merge_sort(arr[middle:]) 

    return merge(left, right)

arr = [5, 2, 4, 7, 1, 3, 2, 6]
sorted_arr = merge_sort(arr)
print("Sorted Array:", sorted_arr)
