from pyfiglet import Figlet
import sys
import random

x = Figlet()

if len(sys.argv) == 1:
    text = input("Input: ")
    fonts = x.getFonts() # gets all the fonts
    x.setFont(font=random.choice(fonts)) #random.choice chooses random font from fonts
    print(x.renderText(text))

elif len(sys.argv) == 3 and sys.argv[1] in ["-f", "--font"]:
    try:
        x = Figlet(font = sys.argv[2])
        text = input()
        print(x.renderText(text))
    except:
        sys.exit(1)

else:
    sys.exit(1)
