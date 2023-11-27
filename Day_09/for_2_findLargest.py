x = [0,9,7,1,8,10,11,23,55]

x.sort()

print(x[len(x)-1])

max = 0
for i in x:
    if(i > max):
        max = i
print(max)