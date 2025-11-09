tweet = input("Input: ")
vowles = "aeiou"
for i in tweet:
    if i.lower() not in vowles:
        print(i, end = "")
