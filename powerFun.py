def Power(x,n):
    if n !=0:
        return x*Power(x,n-1)
    else:
        return 1
def main():
    n = int(input("Enter the exponent (n): "))
    x = float(input("Enter the base (x): "))
    result=Power(x,n)
    print(f"{x} raised to the power {n} is {result}")
    print(result)
main()