print()
# 1. open() with context manager

# f = open("file.txt", "r")
# f.close()


with open("/Users/manoj/Downloads/red.txt", "w") as f:
    f.write("Hey Bruh hows going")

with open("/Users/manoj/Downloads/red.txt", "r") as f:
    data = f.read()
    print(data)
