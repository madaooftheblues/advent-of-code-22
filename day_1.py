import input

read = input.read_argv()
elf_cals = [elf.strip().split("\n") for elf in read.split("\n\n")]

for elf in elf_cals:
    for i in range(len(elf)):
        elf[i] = int(elf[i].strip())


def silver(ec: list):
    max = 0
    for elf in ec:
        cal_sum = sum(elf)
        if cal_sum > max:
            max = cal_sum

    return max


def gold(ec: list):
    first = second = third = 0
    for elf in ec:
        cal_sum = sum(elf)

        if cal_sum > first:
            third = second
            second = first
            first = cal_sum
        elif cal_sum > second:
            third = second
            second = cal_sum
        elif cal_sum > third:
            third = cal_sum

    return first + second + third


print(silver(elf_cals))
print(gold(elf_cals))
