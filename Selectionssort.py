def SelectionSort(arr):
    for i in range(len(arr)- 1):
        min_index = i
        for j in range(i + 1, len(arr)):
            if arr[min_index] > arr[j]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]


arr = [45,52,42,45,5,10,8]
SelectionSort(arr)
print(arr)