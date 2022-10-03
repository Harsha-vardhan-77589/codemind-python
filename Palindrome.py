n=int(input())
s=n
rev=0
while s>0:
    r=s%10
    rev=rev*10+r
    s=s//10
if n==rev:
        print('True')
else:
         print('False')
