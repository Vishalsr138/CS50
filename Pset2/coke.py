due = 50
while due > 0:
    print("Amount Due:", due)
    deposit = int(input("Insert Coin:"))
    if deposit in (25, 10, 5):
        due = due - deposit


print("Change Owed:",abs(due))
