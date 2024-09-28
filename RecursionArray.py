def firstArray(arr,size,val,i):
    if i == size:
        return -1
    if arr[i]==val:
        return i
    return firstArray(arr,size,val,i+1)

def main():
    arr=[4,5,2,6,10]
    size=5
    i=0
    val=int(input("Enter the value to find:"))
    index=firstArray(arr,size,val,i)
    if i != -1:
        print(f"The {val} is found at index {index}")
    else:
        print("Not found at any index")
main()
