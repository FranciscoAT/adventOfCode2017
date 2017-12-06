def main():
    memory_banks = [int(x) for x in input().split()]
    realloc_till_loop = reallocate_banks(memory_banks)
    print(realloc_till_loop)

def reallocate_banks(banks):
    realloc_count = 0
    unique_banks = set()
    current_bank_config = '-'.join(str(x) for x in banks)
    while (current_bank_config not in unique_banks):
        unique_banks.add(current_bank_config)
        banks = reallocate(banks)
        realloc_count += 1
        current_bank_config = '-'.join(str(x) for x in banks)
    return realloc_count

def reallocate(banks):
    max_value_index = banks.index(max(banks))
    memory_to_reallocate = banks[max_value_index]
    banks[max_value_index] = 0
    while(memory_to_reallocate > 0):
        max_value_index = int((max_value_index+1)%len(banks))
        banks[max_value_index] += 1
        memory_to_reallocate -= 1
    return banks

if __name__ == '__main__':
    main()