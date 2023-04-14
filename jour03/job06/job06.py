

chaîne = "abcdefghijklmnopqrstuvwxyz" * 10
i = 1
while i <= len(chaîne):
    print(chaîne[:i])
    chaîne = chaîne[i:]
    i += 1

# ou bien


def writeinpyramid(text):
    endpos = 1
    while len(text) > endpos:
        print(text[0:endpos:])

        text = text[endpos::]
        endpos += 1


text = "abcdefghijklmnopqrstuvwxyz" * 10

writeinpyramid(text)
