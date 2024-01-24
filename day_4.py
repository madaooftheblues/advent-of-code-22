import input
import runtime

lines = input.gen_line()


def get_ranges(line):
    r = [r.split("-") for r in line.strip().split(",")]
    ranges = [[int(x) for x in li] for li in r]
    return ranges


def is_overlap(x1, x2, y1, y2, subset=False):
    if subset:
        if x1 <= y1 and x2 >= y2:
            return True
        elif y1 <= x1 and x2 <= y2:
            return True

    else:
        if y1 <= x2 and x2 <= y2:
            return True
        elif x1 <= y2 and y2 <= x2:
            return True

    return False


@runtime.runtime
def silver(lines):
    overlaps = 0
    for line in lines:
        a, b = get_ranges(line)
        if is_overlap(a[0], a[1], b[0], b[1], subset=True):
            overlaps += 1
    return overlaps


@runtime.runtime
def gold(lines):
    overlaps = 0
    for line in lines:
        a, b = get_ranges(line)
        if is_overlap(a[0], a[1], b[0], b[1]):
            overlaps += 1
    return overlaps


print(silver(lines))
lines = input.gen_line()
print(gold(lines))
