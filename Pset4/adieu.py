def main():
    x = []
    while True:
        try:
            name = input()
            x.append(name)
        except EOFError:
            break

    adieu(x)

def adieu(names):

    print("Adieu, adieu, to ", end="")

    if len(names) == 1:
        print(names[0])
    elif len(names) == 2:
        print (names[0]+" and "+names[1])
    else:
        for index, name in enumerate(names):
            if index == len(names) - 1:
                print(f"and {name}")
            else:
                print(f"{name}, ", end="")


main()