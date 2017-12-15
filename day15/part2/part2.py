def main():
    divider = 2147483647
    a = int(input().split()[4])
    b = int(input().split()[4])
    judge_count = 0

    for _ in range(5000000):
        a = generate_a_value(a, divider)
        b = generate_b_value(b, divider)
        a_bin = '{0:b}'.format(a).zfill(16)
        b_bin = '{0:b}'.format(b).zfill(16)
        if a_bin[-16:] == b_bin[-16:]:
            judge_count += 1
    print(judge_count)

def generate_a_value(initial, divider):
    factor = 16807
    initial = (initial * factor) % divider
    while (initial % 4 != 0):
        initial = (initial * factor) % divider
    return initial

def generate_b_value(initial, divider):
    factor = 48271
    initial = (initial * factor) % divider
    while (initial % 8 != 0):
        initial = (initial * factor) % divider
    return initial

if __name__ == '__main__':
    main()