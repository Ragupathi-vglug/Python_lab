marks=[45,50,60,70,80,90,76,98]
k=int(input("Enter the k Value :"))
len=len(marks)
for i in range(len):
    for j in range(i+1,len):
        if(marks[i]<marks[j]):
            temp=marks[i]
            marks[i]=marks[j]
            marks[j]=temp
result=marks[k-1]
print(marks)
marks.sort(reverse=True)
print("Decending order of the list :",marks)
print(f"{k} Largest number is {result}")