my_arr = [1, 2, [3, [4, 5]], 6]

def my_flatten(arr, res=None):
    if res==None:
        res=[]
    for item in arr:
        if type(item) == int:
            res.append(item)
        else:
           my_flatten(item, res)
    return res

print(my_flatten([1, 2, [3, [4, 5]], 6]))
print(my_flatten([1, 2, [3, [4, 5]], 6]))
