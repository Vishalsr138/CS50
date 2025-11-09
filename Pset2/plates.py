def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    flag=0
    if not 2 <= len(s) <= 6:
        return False
    if not (s[0].isalpha() and s[1].isalpha()):
        return False
    for i in s[2:]:
        if not i.isalnum():
            return False
        if i.isdigit() and flag==0:
            if i=='0':
                return False
            flag=1
        elif i.isalpha():
            if flag==1:
                return False
    return True


main()