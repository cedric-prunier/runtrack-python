liste = [1, 2, 3, 4, 5]

print(liste)


def liste2():
    temp = liste[0]
    liste[0] = liste[-1]
    liste[-1] = temp
    print(liste)


liste2()

# ou

liste = ["a", "b", "c", "d", "e"]


if len(liste):
    premiere_case = liste[0]
    liste[0] = liste[len(liste) - 1]
    liste[len(liste) - 1] = premiere_case

    print(liste)
else:
    print("Liste vide !")
