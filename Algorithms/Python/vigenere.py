import string
lst = string.ascii_lowercase
text = list(input().replace(" ","").lower())
key = list(input().replace(" ","").lower())
index = dict()
for i in range(26):
    index[lst[i]] = i

key1 = list(key[i%len(key)] for i in range(len(text)))

index1 = { v: k for k,v in index.items()}
for i in range(len(text)):
    x = index.get(text[i])
    y = index.get(key1[i])
    print(index1.get((x+y)%26).upper(), end="")
