def cote(a, b, c):
    if a + b > c and a + c > b and c + b > a:

        if a * a + b * b == c * c or a * a + c * c == b * b or c * c + b * b == a * a:
            return "ce triangle est rectangle"
        elif a == b == c:
            return "ce triangle est équilatéral"
        elif a == b or b == c or b == a:
            if a * a + b * b == c * c or a * a + c * c == b * b or c * c + b * b == a * a:
                return "ce triangle est rectangle isocèle"
            else:
                return "Triangle isocèle"
        else:
            return "triangle quelconque"
    else:
        return "impossible de construire un triangle"


print(cote(10, 10, 10))
