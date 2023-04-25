# #!/usr/bin/python3

lst = [1, 2, 3, 4,5,6,7,8,"a","b"]
def to_dict(lst):
    resdict = {}
    for i in range(0,len(lst), 2):
        resdict[lst[i]]=lst[i+1]
    return resdict

print(to_dict(lst))
def to_dict2(lst):
    keys = [lst[k] for k in range(len(lst)) if k%2==1]
    values = [lst[v] for v in range(len(lst)) if v%2==0]

    res_dict = {keys[i]: values[i] for i in range(len(keys))}
    return res_dict
#

print(to_dict2(lst))

