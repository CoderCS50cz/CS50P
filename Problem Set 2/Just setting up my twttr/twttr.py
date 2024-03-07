tweet = input("Input: ")

print("Output: ", end="")
for c in tweet:
    if c not in ["A", "E", "I", "O", "U", "a", "e", "i", "o", "u"]:
        print(c, end="")
print()
