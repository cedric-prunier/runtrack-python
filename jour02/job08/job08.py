def fleg(type, saison):
    if type == "fruits" and saison == "hiver":
        print("orange, mandarine et kiwi")
    if type == "fruits" and saison == "ete":
        print("Poire, fraise, cassis")
    if type == "legume" and saison == "hiver":
        print("carotte, topinambour, endive")
    if type == "legume" and saison == "ete":
        print("artichaut, aubergine, navet")


fleg("fruits", "hiver")
fleg("fruits", "ete")
fleg("legume", "hiver")
fleg("legume", "ete")
