s=int(input("Enter the Starting Value :"))
n=int(input("Enter the Ending Value :"))

print(f"\nThe Prime Numbers between {s} to {n} is: ")
for i in range(s,n):
    flag=0
    j=2
    while (j<i):
        if(i%j==0):
            flag=1
        j+=1
    if (flag==0):
        print(i)