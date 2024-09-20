def linearSearch(a,item):
    for i in range(len(a)):
        if a[i]==item:
            return f" Found at index {i+1}"
    return False
def main():
    a=[4,45,75,17,4,25]
    item=4
    result= linearSearch(a,item)
    print(result)

main()