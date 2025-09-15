s=input("Enter the string :")

word=s.split()

count=0
num_count=0
sym_count=0

for a in s:
    if a.isalpha():
        count+=1
    elif a.isdigit():
        num_count+=1
    elif not(a.isalnum() or a.isspace()):
        sym_count+=1
up=s.upper()
low=s.lower()

print("The Number of words in a String is :",len(word))
print("The Number of Alphabets in a String is :",count)
print("The number of Digits in a String is :",num_count)
print("The Number of Special characters in a String is :",sym_count)
print("The convertion of Uppercase:",up)
print("The convertion of Lowercase:",low)
