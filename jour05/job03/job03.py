def rectangle(width, height):
    for i in range(1, width + 1):
        for j in range(1, height + 1):
            if j == 1 or j == height:
                if i == width or i == j == 1 or i == 1 and j == height:
                    print("+", end="")
                else:
                    print("|", end="")
            elif i == 1 or i == width:
                print("-", end="")
            elif i + j == height + 1:
                print(" ", end="")
            else:
                print("#", end="")

        print()


rectangle(10, 10)
