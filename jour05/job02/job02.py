def rectangle(width, height):
    for i in range(1, width + 1):
        for j in range(1, height + 1):
            if j == 1 or j == height:
                print("|", end="")
            elif i == 1 or i == width:
                print("-", end="")
            else:
                print(" ", end="")
        print()


rectangle(10, 10)
