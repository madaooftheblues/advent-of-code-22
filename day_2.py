import input

read = input.read_argv().strip()
rounds = [tuple(x.split()) for x in read.split("\n")]

elf = ["A", "B", "C"]
you = ["X", "Y", "Z"]


def score(a, b):
    ai = elf.index(a)
    bi = you.index(b)

    if ai == bi:
        return 3 + bi + 1
    if bi == (ai + 1) % 3:
        return 6 + bi + 1

    return bi + 1


def win_lose_tie(a, b):
    ai = elf.index(a)
    if b == "Y":
        return you[ai]
    if b == "Z":
        return you[(ai + 1) % 3]
    return you[(ai + 2) % 3]


def silver(rounds: list):
    sum = 0
    for round in rounds:
        sum += score(round[0], round[1])
    return sum


def gold(rounds: list):
    sum = 0
    for round in rounds:
        sum += score(round[0], win_lose_tie(round[0], round[1]))
    return sum


print(silver(rounds))
print(gold(rounds))
