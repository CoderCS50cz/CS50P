import emoji

inp = input("Input: ")

em = emoji.emojize(inp, language="alias")

print(f"Output: {em}")
