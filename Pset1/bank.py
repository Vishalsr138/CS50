def main():
    greet = input("Greeting: "). strip().lower()
    process(greet)

def process(x):
    first_word = x.split()[0]
    if first_word.startswith("hello"):
        print("$0")
    elif first_word.startswith("h"):
        print("$20")
    else:
        print("$100")

main()