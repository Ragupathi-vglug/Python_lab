import math
a=int(input("Enter the A's value :"))
b=int(input("Enter the B's value :"))
c=int(input("Enter the C's value :"))
s=(a+b+c)/2
area=math.sqrt(s*(s-a)*(s-b)*(s-c))
print("The Area of the Triangle is:",area)