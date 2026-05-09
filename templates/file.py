f = open("sample.txt", "r")
pole = []

while True:
    line = f.readline().strip()
    if line == "":
        f.close()
        break
    pole.append(line)