a=["one","two","three","one","five","six","one","three","six"]
freq={}
for i in a:
    freq[i]=freq.get(i,0)+1
print(a)
print("The Number of Occurances in the list is :\n",freq)