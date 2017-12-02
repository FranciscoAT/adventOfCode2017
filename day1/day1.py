#pylint: disable=C0111,C0325

def next_sum(in_arr):
    current_sum = 0
    for index in range(0, len(in_arr)-1):
        if (in_arr[index] == in_arr[index+1]):
            current_sum += in_arr[index]
    if (in_arr[len(in_arr)-1] == in_arr[0]):
        current_sum += in_arr[0]
    return current_sum

# test input
# for i in range(1, int(input())+1):
#     arr = [int(x) for x in input().split(' ')]
#     returned_sum = next_sum(arr)
#     print(returned_sum)

if __name__ == '__main__':
    value_in = [int(x) for x in list(input())]
    value_in = next_sum(value_in)
    print(value_in)

