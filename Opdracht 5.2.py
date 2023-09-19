# Opdracht 1
import random

bingo_number_total = 4 ** 2
numbers_all = list(range(1, 100))
random.shuffle(numbers_all)
bingo_numbers = numbers_all[:bingo_number_total]

print(bingo_numbers)

bingo_lijst = [[], [], [], []]

counter = 0
lijst_nummer = 0
for bingo_getal in bingo_numbers:
    if counter == 4:
        lijst_nummer += 1
        counter = 0
    counter += 1

    bingo_lijst[lijst_nummer].append(bingo_getal)

print("---------------------------------------------------------------------")

print(bingo_lijst[0])
print(bingo_lijst[1])
print(bingo_lijst[2])
print(bingo_lijst[3])


# Opdracht 2

getrokken_nummers = 50
getrokken_nummers_aantal = list(range(1, 100))
random.shuffle(getrokken_nummers_aantal)
trekken = getrokken_nummers_aantal[:getrokken_nummers]

for nummer in trekken:
    for lijn in range(counter):
        for kolom in range(lijst_nummer + 1):
            if bingo_lijst[lijn][kolom] == nummer:
                bingo_lijst[lijn][kolom] = 0

print("---------------------------------------------------------------------")

print(bingo_lijst[0])
print(bingo_lijst[1])
print(bingo_lijst[2])
print(bingo_lijst[3])

# Opdracht 3





print("---------------------------------------------------------------------")

