import string
lst = string.ascii_lowercase
out=[]
text = list(input().replace(" ","").lower())
key = int(input())
index = dict()
for i in range(26):
    index[lst[i]] = i
index1 = { v: k for k,v in index.items()}

for i in range(len(text)):
    x = index.get(text[i])
    print((index1.get((x+key)%26)).upper(), end="")
