# https://carpedm20.github.io/emoji/all.html?enableList=enable_list_alias

import emoji
import sys

emo = input("Input: ")

print("Output:", emoji.emojize(emo, language="alias"))

