import input

line = input.gen_line()


def first_marker(n: int, line: str) -> int:
    """
    Finds the characters it take to discover n non-repeating characters

    Args:
        n: An integer that specifies the number of non-repeating characters
        line: A string that is to be parsed

    Returns:
        An integer that is the number of characters consumed
        to complete a non-repeating sequence or -1 if no such sequence
        is found
    """
    seen: set[str] = set()
    for i in range(len(line)):
        if i + n > len(line):
            break
        seen.clear()
        for j in range(i, i + n):
            if line[j] in seen:
                break
            seen.add(line[j])
        else:
            return i + n

    return -1


def silver():
    return first_marker(4, next(line))


def gold():
    return first_marker(14, next(line))


print(silver())
line = input.gen_line()
print(gold())
