
n = 33
k = 5

total = 2
f = [0,1]
for i in range(2,n+1):
    f.append( (f[i-2] * k) + f[i-1]  )

print(f)
