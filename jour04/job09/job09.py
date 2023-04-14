L = [8, 24, 27, 48, 2, 16, 9, 102, 7, 84, 91]
max = L[0]
min = L[0]
for i in L:
    if i < min:
        min = i
    elif i > max:
        max = i
    else:
        None


print(min, max)
