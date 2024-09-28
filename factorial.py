def Fact(n):
    if n>1:
        return n*Fact(n-1)
    else:
        return 1
def main():
    n=int(input("Enter the Number: "))
    result=Fact(n)
    print(f"Factorial of  {n} is {result}")
main()