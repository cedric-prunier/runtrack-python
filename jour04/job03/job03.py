fruits = ["pomme", "cerise", "orange"]


def mylist():

    fruits.append("Melon")
    print(fruits)


mylist()

# ou


def ajouter_melon(fruits):
    fruits.append("Melon")


fruits = ["pomme", "cerise", "orange"]
ajouter_melon(fruits)
print(fruits)
