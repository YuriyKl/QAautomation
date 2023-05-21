# #!/usr/bin/python3

users = [
{'name': 'Luarvik L. Luarvik',
'age': 17},
{'name': 'Olaf Andvarafors',
'age': 18},
{'name': 'Brun Du Barnstokr',
'age': 19}
]

print([dic['name'] for dic in users for key in dic if dic["age"]>=18], sep="\n")
