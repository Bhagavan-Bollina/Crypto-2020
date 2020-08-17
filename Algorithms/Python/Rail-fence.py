text = list(input().lower().replace(" ",""))
key = int(input())
sl=[]
for i in range(0, key):
    for j in range(i,len(text),key):
        sl.append(text[j])
for i in sl:
    print(i.upper(), end="")
