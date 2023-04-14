string = "je suis le plus cool de tout le quartier"


def mots_plus_longs(chaine, n):

    mots = chaine.split()
    mots_plus_longs = []
    for mot in mots:
        if len(mot) > n:
            mots_plus_longs.append(mot)
    return mots_plus_longs


print(mots_plus_longs(string, 3))
