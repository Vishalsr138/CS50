def main():
    time = input("What is the time: ").strip()

    a = convert(time)
    if 7 <= a <= 8:
        print("breakfast time")
    elif 12 <= a <= 13:
        print("lunch time")
    elif 18 <= a <= 19:
        print("dinner time")

def convert(x):
    time = x.split(":")
    hr = int(time[0])
    min = int(time[1])

    t = hr + min/60

    return t


if __name__ == "__main__":
    main()