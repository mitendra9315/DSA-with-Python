"""def fibo(n):
    if n<=1:
        return 1
    else:
        return fibo(n-1)+fibo(n-2)
def main():
    n=int(input("Enter the number elements in the series: "))
    if n<0:
        print("Please enter the valid number")
    else:
        for i in range(n):
            print(fibo(i))
main()
"""

# Recursive Fibonacci with memoization and linear time complexity
def fibo_memo(n, memo={}):
    if n <= 1:
        return 1
    if n not in memo:
        memo[n] = fibo_memo(n-1, memo) + fibo_memo(n-2, memo)
    return memo[n]

def main_memo():
    n = int(input("Enter the number of elements in the series: "))
    if n < 0:
        print("Please enter a valid number")
    else:
        fib_series = [str(fibo_memo(i)) for i in range(n)]
        print(" ".join(fib_series))

# Test the linear time complexity function
main_memo()



"""
n = int(input("Enter the number of elements in the series: "))
if n < 0:
    print("Please enter a valid number")
else:
    a, b = 1, 1
    for i in range(n):
        print(a, end=" ")  # Print the current Fibonacci number
        a, b = b, a + b    # Move to the next number in the sequence
"""