def binarySearch(a,left,right,item):
    if right>=left:
        mid=(left+right)//2
        if a[mid]==item:
            return mid + 1
        elif a[mid] < item:
            return binarySearch(a,mid+1,right,item)
        else:
            return binarySearch(a,left,mid-1,item)
    else:
        return -1
def main():
    a=[1,5,8,7,10,15,20,25]
    item=15
    left=0
    right=(len(a)-1)
    re=binarySearch(a,left,right,item)
    print(re)
main()