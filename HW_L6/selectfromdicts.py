# #!/usr/bin/python3

users = [
{'name': 'Luarvik L. Luarvik',
'age': 17},
{'name': 'Olaf Andvarafors',
'age': 18},
{'name': 'Brun Du Barnstokr',
'age': 19}
]

for user in users:
    if user["age"] >= 18:
        print([user["name"]])

#Solution #2
print(*[user['name'] for user in users if user["age"]>=18], sep="\n")