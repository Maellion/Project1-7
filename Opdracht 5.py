numbers = list(range(1, 31))


for numbers in range(1, 31):
    if numbers % 3 == 0 and numbers % 5 == 0:
        print("FizzBuzz")
    elif numbers % 3 == 0:
        print("Fizz")
    elif numbers % 5 == 0:
        print("Buzz")
    else:
        print(numbers)


for i in range(1, 10):
    if i == 5:
        continue
    print(i)
    if i == 7:
        break

