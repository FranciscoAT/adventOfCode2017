from math import ceil

def main():
    lengths = [int(x) for x in input().split(',')]
    lengths = run_hash(lengths)
    print(lengths)

def run_hash(commands):
    values = list(range(256))
    # values = list(range(5))
    # print(values)
    index = 0
    skip = 0
    for command in commands:
        # print(values)
        for sub_index in range(ceil(command/2)):
            temp_val = values[(index+sub_index)%len(values)]
            values[(index+sub_index)%len(values)] = values[(index+(command-sub_index-1))%len(values)]
            values[(index+(command-sub_index-1))%len(values)] = temp_val
            # print(values)
        index += (command+skip)%len(values)
        skip += 1
        # print(command)
    return values


if __name__ == '__main__':
    main()
