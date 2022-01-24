# Dictionary downloaded from
#   https://raw.githubusercontent.com/redbo/scrabble/master/dictionary.txt
with open("dictionary.txt") as file:
    lines = file.readlines()

f = open("5letterwords.txt", "w")

for line in lines:
    if len(line.strip()) == 5:
        f.write(line.strip().lower() +"\n")
f.close()
