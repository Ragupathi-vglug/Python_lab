def fib(n):
    if (n==0 or n==1):
        return n
    else:
        val=fib(n-1)+fib(n-2)
        return(val)
n=int(input("Enter how many terms of fibonacci series to be print:"))
print("\nFibonacci series :")
for i in range(n):
    result=fib(i)
    print(result)