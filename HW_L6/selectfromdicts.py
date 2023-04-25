# #!/usr/bin/python3


users = [
{'name': 'Luarvik L. Luarvik',
'age': 17},
{'name': 'Olaf Andvarafors',
'age': 18},
{'name': 'Brun Du Barnstokr',
'age': 19}
]


print(users[0])

print(*[key for i in users for key in i.keys()], sep = "\n")

# res = {'name':v, for ('name',v) in users.items() if val>=18}
# res = {'name':v, 'age':val for ('name',v) in users.items() for ('age',val) in users.items() if val>=18}
# print(res)
# newdata = {}
# for entry in users:
#     name = entry.pop('name') #remove and return the name field to use as a key
#     newdata[name,age] = entry

# print(newdata)
# users2 = {item['name']:item for item in users}
# users2 =dict(users[0])
# print(users2)
# print()
# users3 = dict(users[0])
# print(users3)
# d = [dict(users[i] for )]
# for name,age in users2.items():
#     print('{0} corresponds to {1}'.format(name, age))
#
#
# res = list({name:age for (name, age) in users2.items() })
# print(res)