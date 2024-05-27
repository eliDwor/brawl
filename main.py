import csv

#open the file
file = open("brawl_deck.txt", "r")

#store each line in a list excluding the newline character, commander, and deck
lines = []

for line in file:
    if line != "Commander\n" and line != "Deck\n" and line != "\n":
        #remove the leading number and whitespace
        line = line[2:]
        #remove all text after the ( symbol
        line = line.split("(")[0]
        lines.append(line.strip())

print(lines)

#close the file
file.close()
cards = {}

with open("cards.csv", encoding='latin-1') as f:
    reader = csv.reader(f)
    #skip the header
    next(reader)
    for row in reader:
        cards[row[1]] = int(row[3])

score = 0

for line in lines:
    if line in cards:
        print(line, cards[line])
        score += cards[line]


print(f"you deck score: {score}")