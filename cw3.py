names = [
    ["a","b","c"]
    ["d","e","f"]
    ["g","h","i"]
]

print(list2s[0][0])
# -> a

for name in names:
    for i in range(len names[0]):
        print(name[0][i-1])