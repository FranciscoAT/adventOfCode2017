from math import ceil

def main():
    salt = input()
    num_filled = 0
    for index in range(128):
        new_salt = salt+'-'+str(index)
        num_filled += run_hash(new_salt)
    print(num_filled)

def run_hash(salt):
    salt = get_ascii(salt)
    dense_knoted_row = knot(salt)
    num_one_count = 0
    for num in dense_knoted_row:
        num_one_count += num.count('1')
    return num_one_count

def get_ascii(salt):
    ascii_salt = []
    for character in list(salt):
        ascii_salt.append(ord(character))
    ascii_salt.extend([17,31,73,47,23])
    return ascii_salt

def knot(salt):
    row = list(range(256))
    current_pos = 0
    skip = 0
    for _ in range(64):
        current_pos,skip,row = knot_hash(current_pos,skip,row,salt)
    dense_hash = generate_dense_hash(row)
    return(dense_hash)

def knot_hash(current_pos, skip, row, salt):
    for length in salt:
        for index in range(ceil(length/2)):
            temp_val = row[(current_pos+index)%len(row)]
            row[(current_pos+index)%len(row)] = row[(current_pos+(length-index-1))%len(row)]
            row[(current_pos+(length-index-1))%len(row)] = temp_val
        current_pos += (length+skip)%len(row)
        skip += 1
    return current_pos, skip, row

def generate_dense_hash(row):
    dense_hash = []
    for i in range(16):
        dense_val = 0
        for j in range(16):
            dense_val ^= row[i*16+j]
        dense_hash.append(bin(dense_val))
    return(dense_hash)

if __name__ == '__main__':
    main()