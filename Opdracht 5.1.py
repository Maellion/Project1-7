numbers = list(range(1, 101))

for number in numbers:
    priemgetal = True

    for deler in numbers:
        if number == 1:
            priemgetal = False
            break
        if number > deler > 1:
            if number % deler == 0:
                priemgetal = False
                break
    if priemgetal:
        print(number)
