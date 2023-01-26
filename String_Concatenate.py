s=input()
j=input()
x=s+j


li = []
l = len(x)
for i in range (0,l):
	li.append(x[i])


for i in range(0,l):
	for j in range(0,l):
		if li[i]<li[j]:
			li[i],li[j]=li[j],li[i]
j=""

for i in range(0,l):
	j = j+li[i]

print(j)
