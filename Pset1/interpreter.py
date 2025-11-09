def main():
    eq = input("Enter the expression: ").strip()
    interpreter(eq)

def interpreter(x):
    parts = x.split()
    first_num = float(parts[0])
    exp = parts[1]
    second_num = float(parts[2])

    if exp == "+":
        print(first_num + second_num)
    elif exp == "-":
        print(first_num - second_num)
    elif exp == "*":
        print(first_num * second_num)
    elif exp == "/":
        print(first_num / second_num)

main()