#!/usr/bin/python3
# Solution 1
pets_aliases = ('Murzik', 'Barsik', 'Pantera')
print(pets_aliases[0], end=", ")
print(pets_aliases[1], end=", ")
print(pets_aliases[2])
# Solution 2
for alias in pets_aliases:
    if alias != pets_aliases[-1]:
        print(alias, end=", ")
    else:
        print(alias)