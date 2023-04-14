def chiffrement_cesar(message, decalage):
    message_chiffre = ""
    for lettre in message:
        if lettre.isalpha():
            nouvelle_lettre = chr((ord(lettre) - 97 + decalage) % 26 + 97)
            message_chiffre += nouvelle_lettre
        else:
            message_chiffre += lettre
    return message_chiffre


print(chiffrement_cesar("Bonjour les amis", 3))
