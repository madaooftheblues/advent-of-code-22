import input
import runtime

lines = input.gen_line()


def find_position(an: int, a1: int, d: int):
    """Find the position of a term in an arithmetic progression"""
    return ((an - a1) // d) + 1


def parse_crates(lines):
    data = []
    for line in lines:
        if line == "\n":
            break
        data.append(line)

    crates = {}
    crate_numbers = data[-1]

    for i, c in enumerate(crate_numbers):
        if c.isdecimal():
            crates.setdefault(int(c), [])
    for line in data[-1::-1]:
        for i, c in enumerate(line):
            if c.isalpha():
                crates[find_position(i, 1, 4)].append(c)

    return crates


def parse_qsd(line: str):
    q, s, d = [int(x) for x in line.strip().split() if x.isdecimal()]
    return (q, s, d)


def move_crates(quantity: int, source: list, dest: list, retain=False):
    items = []
    for i in range(quantity):
        items.append(source.pop())

    if retain:
        items.reverse()
    dest.extend(items)


def top_items(crates):
    # Asserts that crates are placed in the order they were added
    top = ""
    for crate in crates.values():
        top += crate.pop()
    return top


def process_crates(lines, retain=False):
    crates = parse_crates(lines)
    for line in lines:
        q, s, d = parse_qsd(line)
        move_crates(q, crates[s], crates[d], retain=retain)
    return top_items(crates)


@runtime.runtime
def silver():
    return process_crates(lines)


@runtime.runtime
def gold():
    return process_crates(lines, retain=True)


print("silver:", silver())
lines = input.gen_line()
print("gold:", gold())
