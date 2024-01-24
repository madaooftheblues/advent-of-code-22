import input
import runtime

lines = input.gen_line()


def get_priority(a: str):
    return ord(a) - (96 if a.islower() else 38)


def get_halves(line: str):
    half = len(line) // 2
    first, second = line[:half], line[half:]
    return (first, second)


def get_intersection(first, *second):
    return tuple(set(first).intersection(*[set(x) for x in second]))[0]


@runtime.runtime
def silver(lines):
    sum = 0
    for line in lines:
        first, second = get_halves(line)
        sum += get_priority(get_intersection(first, second))
    return sum


@runtime.runtime
def gold(lines):
    sum = 0
    group = []
    for i, line in enumerate(lines):
        group.append(line.strip())
        if (i + 1) % 3 != 0:
            continue
        sum += get_priority(get_intersection(group[0], *group[1:]))
        group.clear()
    return sum


print(silver(lines))
lines = input.gen_line()
print(gold(lines))
