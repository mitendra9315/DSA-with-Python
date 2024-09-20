def bubbleSort(arr):
    n=len(arr)
    for i in range(n):
        swapped = False
        for j in range (0,n-i-1):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
                swapped = True
        if not swapped:
            break
    return arr

def main():
    arr=[12,45,85,78,52]
    print("Array before sorting:",arr)
    sorted_arr=bubbleSort(arr)
    print("After sorting",sorted_arr)
main()    