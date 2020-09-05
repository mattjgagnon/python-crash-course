user_0 = {
    'username': 'whatever',
    'first': 'sdgsdfg',
    'last': 'sgfje ghfg',
    }

for key, value in user_0.items():
    print(f"\nKey: {key}")
    print(f"Value: {value}")

print("\n")

# print all the keys in a dict
for key in user_0.keys():
    print(key)

print("\n")

# print all the values in a dict
for value in user_0.values():
    print(value)

print("\n")

for key in sorted(user_0.keys()):
    print(f"{key}")

print("\n")

# a set is a collection in which each item must be unique
for key in set(user_0.values()):
    print(key)


