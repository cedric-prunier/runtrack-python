def calcul(number1, operator, number2):
    if operator == "*":
        return number1 * number2
    elif operator == "+":
        return number1 + number2
    elif operator == "-":
        return number1 - number2
    elif operator == "/":
        return number1 / number2
    elif operator == "%":
        return number1 % number2
    else:
        print("Opérateur invalide")


print(calcul(3, '+', 4))
print(calcul(5, '-', 6))
print(calcul(2, '*', 5))
print(calcul(4, '/', 8))
print(calcul(6, '%', 3))
