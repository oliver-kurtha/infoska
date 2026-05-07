import sys

f = open("knihovnik.txt", "r")

knihy = []

while True:
    line = f.readline().strip()
    if line == "":
        f.close()
        break
    knihy.append(float(line))

policka = int(input("zadaj sirku policky, (min. 5): "))

policky = []
temp = []
x = 0

for i in knihy:
    if x + i <= policka:
        temp.append(i)
        x += i
        print("kniha sa zmesti do policky")
        print(temp)
    else:
        policky.append(temp)
        temp = [i]
        x = i
        print("nezmesti sa, nova policka")
        print(temp)
    
policky.append(temp)

print(policky)
sys.exit()