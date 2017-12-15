def main():
    a_factor = 16807
    b_factor = 48271
    divider = 2147483647
    a = int(input().split()[4])
    b = int(input().split()[4])
    judge_count = 0

    for _ in range(40000000):
        a = (a * a_factor) % divider
        b = (b * b_factor) % divider
        a_bin = '{0:b}'.format(a).zfill(16)
        b_bin = '{0:b}'.format(b).zfill(16)
        if a_bin[-16:] == b_bin[-16:]:
            judge_count += 1
    print(judge_count)

if __name__ == '__main__':
    main()