def main():
    name = input("camelCase: ")
    snake_case(name)

def snake_case(case):
    for i in case:
        if i == i.upper():
            print(f"_{i.lower()}", end="")
        else:
            print(i, end="")

main()
