s=input()
j=0
for ch in s:
    if (ch >= '0' and ch <= '9'):
        j+=int(ch)
print(j)