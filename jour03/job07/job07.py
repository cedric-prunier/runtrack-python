chaîne = "nikana"
print(chaîne)

chaîne2 = chaîne[::-1]
print(chaîne2)

# ou

original = "nikana"
inverse = ""

for char in original:
    inverse = char + inverse
print(inverse)
