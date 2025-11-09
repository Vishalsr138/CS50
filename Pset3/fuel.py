def main():
    while True:
        try:
            frac = input("Fraction: ")
            x = int(frac.split("/")[0])
            y = int(frac.split("/")[1])

            if x > y or x < 0 or y < 0:
                continue

            per = (x/y) * 100
            break

        except ValueError or ZeroDivisionError:
            continue

    if per <= 1:
        print("E")
    elif per >= 99:
        print("F")
    else:
        print(f"{round(per)}%")

main()