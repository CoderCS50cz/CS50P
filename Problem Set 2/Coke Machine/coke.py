amount_due = 50
print("Amount Due:", amount_due)

while amount_due > 0:
    coin = int(input("Insert coin: "))
    if coin == 25 or coin == 10 or coin == 5:
        amount_due = amount_due - coin
    if amount_due > 0:
        print("Amount Due:", amount_due)
if amount_due < 0:
    print("Change Owed:", -amount_due)
else:
    print("Change Owed:", amount_due)
