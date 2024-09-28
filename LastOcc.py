def findValueIndex(arr, i, val):
	if i == -1:
    	    return -1  

	if arr[i] == val:
    	    return i  
	return findValueIndex(arr, i -1, val)

def main():
    arr = [1, 2, 3, 4,1,5]
    size = len(arr)
    val = int(input("Enter the value to find: "))

    index = findValueIndex(arr, size-1, val)

    if index != -1:
	    print(f"The value {val} is found at index {index}.")
    else:
	    print(f"The value {val} is not in the array.")
main()