import os, sys
from PIL import Image, ImageOps

if len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")
elif not sys.argv[1].lower().endswith(".jpg") and not sys.argv[1].lower().endswith(".jpeg") and not sys.argv[1].lower().endswith(".png"):
    sys.exit("Invalid input")
elif not sys.argv[2].lower().endswith(".jpg") and not sys.argv[2].lower().endswith(".jpeg") and not sys.argv[2].lower().endswith(".png"):
    sys.exit("Invalid input")
elif os.path.splitext(sys.argv[1])[1].lower() != os.path.splitext(sys.argv[2])[1].lower():
    sys.exit("Input and output have a different extinsions")


try:
    photo = Image.open(sys.argv[1])
    shirt = Image.open("shirt.png")
    size = shirt.size
    photo = ImageOps.fit(photo, size)
    photo.paste(shirt, shirt)
    photo.save(sys.argv[2])

except FileNotFoundError:
    sys.exit("Input does not exist")
