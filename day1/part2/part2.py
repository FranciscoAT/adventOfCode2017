def sum_half_way(list_in):
    # double_list = list_in + list_in
    list_length = len(list_in)
    total_sum = 0
    for i in range(list_length):
        halfway = int((i+list_length/2)%list_length)
        if list_in[i] == list_in[halfway]:
            total_sum += list_in[i]
    return total_sum


if __name__ == '__main__':
    val_in = [int(x) for x in list(input())]
    val_in = sum_half_way(val_in)
    print(val_in)
