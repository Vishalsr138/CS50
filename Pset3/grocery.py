def main():
    items = {}

    add_items(items)

    for i in sorted(items):
        print(items[i], i.upper())

def add_items(items):
    while True:
        try:
            x = input().title()
            if x in items:
                items[x] += 1
            else:
                items[x] = 1
        except EOFError:
            return

main()