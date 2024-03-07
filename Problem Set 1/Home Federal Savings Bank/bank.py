bank = input("Greetings: ").strip().lower()

if bank.startswith("hello"):
    print("$0")
elif bank.startswith("h"):
    print("$20")
else:
    print("$100")
