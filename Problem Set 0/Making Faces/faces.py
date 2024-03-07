def main():
    faces = input()
    output = convert(faces)
    print(output)

def convert(faces):
    faces = faces.replace(":)", "🙂").replace(":(", "🙁")
    return faces

main()
