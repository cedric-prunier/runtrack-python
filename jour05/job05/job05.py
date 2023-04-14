def distance_toilettes(marches, hauteur):
    hauteur_m = hauteur / 100
    distance_jour = hauteur_m * marches * 2 * 5
    distance_semaine = distance_jour * 7
    resultat = distance_semaine
    resultat = "Pour {} marches de {} cm, le gardien parcours {} m par semaine.".format(
        marches, hauteur_m, resultat)
    print(resultat)


distance_toilettes(100, 20)
