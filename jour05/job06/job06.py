def arrondir_notes(notes):
    arrondies = []
    for note in notes:
        if note < 40:
            arrondies.append(note)
        else:
            multiple_5 = ((note + 2)//5)*5
            if multiple_5 - note < 3:
                arrondies.append(multiple_5)
            else:
                arrondies.append(note)

    print(arrondies)


notes = [10, 47, 54, 83, 82]


arrondir_notes(notes)
