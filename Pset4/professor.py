import random


def main():
        level = get_level()
        x = generate_integer(level)
        y = generate_integer(level)
        score = 0
        for i in range(10):
                wrong = 0
                while wrong < 3: 
                        answer = int(input(f"{x} + {y} = "))
                        if answer == x+y:
                                score += 1
                                break
                        else:
                              print("EEE")
                              wrong += 1
                              if wrong == 3:
                                print(f"Correct Answer: {x+y}")
                                break

                x = generate_integer(level)
                y = generate_integer(level)

        print(score)

def get_level():
        while True:
                try:
                    x = int(input("Level: "))
                    if x in range(1,4):
                        break
                    else:
                        continue
                except ValueError:
                       pass

        return x


def generate_integer(level):
        if level == 1:
            return random.randint(0, 9)
        elif level == 2:
            return random.randint(10, 99)
        else:
            return random.randint(100, 999)



if __name__ == "__main__":
       main()
