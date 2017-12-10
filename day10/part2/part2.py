from math import ceil
import binascii

def main():
    # lengths = [int(x) for x in input().split(',')]
    lengths = get_lengths()

    index = 0
    skip = 0
    values = list(range(256))
    for _ in range(64):
        values, index, skip = run_hash(values, lengths, index, skip)

    dense_hash = get_dense_hash(values)
    hex_value = convert_to_hex(dense_hash)
    print(hex_value)

def run_hash(values, commands, index, skip):
    for command in commands:
        for sub_index in range(ceil(command/2)):
            temp_val = values[(index+sub_index)%len(values)]
            values[(index+sub_index)%len(values)] = values[(index+(command-sub_index-1))%len(values)]
            values[(index+(command-sub_index-1))%len(values)] = temp_val
        index += (command+skip)%len(values)
        skip += 1
    return values, index, skip

def get_lengths():
    input_lengths = list(input())
    lengths = []
    for char in input_lengths:
        lengths.append(ord(char))
    lengths.extend((17, 31, 73, 47, 23))
    return [int(x) for x in lengths]

def get_dense_hash(values):
    dense_hash = []
    for i in range(16):
        hash_value = 0
        for j in range(16):
            hash_value ^= values[i*16+j]
        dense_hash.append(hash_value)
    return dense_hash

def convert_to_hex(dense_hash):
    for index in range(len(dense_hash)):
        dense_hash[index] = hex(dense_hash[index])
    return ''.join(dense_hash)


if __name__ == '__main__':
    main()
