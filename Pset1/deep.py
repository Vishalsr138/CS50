def main():
    num = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ").strip()
    check(num)

def check(x):
    x = x.lower().replace("-", " ")
    if x == "42" or x == "forty two":
        print("Yes", end = "")
    else:
        print("No", end = "")

main()