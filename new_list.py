a=[2,4,9,16,25]
ready=[]
for i in a:
    ready.extend([pow(i,0.5)])
print(ready)

def f(a):
    return pow(a,0.5)
print(list(map(f,a)))

A=[pow(i,0.5) for i in a]
print(A)
