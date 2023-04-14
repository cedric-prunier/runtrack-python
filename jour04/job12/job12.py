liste = [8, 24, 27, 48, 2, 16, 9, 102, 7, 84, 91]


def tri_selection(liste):
    n = len(liste)
    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            if liste[j] < liste[min_index]:
                min_index = j
        liste[i], liste[min_index] = liste[min_index], liste[i]
    return liste


print(tri_selection(liste))
