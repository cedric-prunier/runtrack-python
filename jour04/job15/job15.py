L = [22.4, 4.0, 16.22, 9.10, 11.00, 12.22, 14.20, 5.20, 17.50]


arrondis = []
for i in L:
    arrondis.append(round(i))

print(arrondis)


def tri_selection(liste):
    n = len(liste)
    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            if liste[j] < liste[min_index]:
                min_index = j
        liste[i], liste[min_index] = liste[min_index], liste[i]
    return liste


print(tri_selection(arrondis))
