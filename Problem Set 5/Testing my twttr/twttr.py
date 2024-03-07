def main():
    word = input("Input: ")

    print("Output:", shorten(word))


def shorten(word):
    shorten_word = ""
    for character in word:
        if character not in ["A", "E", "I", "O", "U", "a", "e", "i", "o", "u"]:
            shorten_word = shorten_word + character
    return shorten_word


if __name__ == "__main__":
    main()
