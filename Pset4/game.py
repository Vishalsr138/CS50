import random

def main():
    level = get_level()
    num = random.randint(1,level)

    while True:
        guess = get_guess()

        if guess <= 0:
             continue
        elif guess < num:
             print("Too small!")
        elif guess > num:
             print("Too large!")
        else:
             print("Just right!")
             break


def get_level():
        while True:
                try:
                    x = int(input("Level: "))
                    if x in range(1,99):
                        break
                    else:
                        continue
                except ValueError:
                       pass
        return x


def get_guess():
     while True:
          try:
               g = int(input("Guess:"))
               if g > 0:
                    return g
          except ValueError:
               continue


main()

