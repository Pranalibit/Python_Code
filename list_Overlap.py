import random
x = []
y = []
c = y
j=1
k=1
while j!=13:
    i = random.randrange(0,100)
    x.append(i)
    j+=1
print(x)
while k!=20:
    i = random.randrange(0,100)
    y.append(i)
    k+=1
print(y)

for i in x:
    if i not in c:
        c.append(i)
print(c)
