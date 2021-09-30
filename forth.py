a = [1,2,3,5,13,4,34,22,12,10, 1]
b = [ 1, 2, 5, 14, 16, 22, 1, 2]
l = []
f= []

for i in a:
    for j in b:
        if i == j:
            l.append(i)
for k in l:
    if k not in f:
        f.append(k)
print(f)