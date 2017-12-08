def solve_square_range(num_to_find):
    curr_range = [2,9]
    curr_index = 0

    while(curr_range[1] < num_to_find):
        curr_index += 1
        curr_range[0] = curr_range[0]+(8*curr_index)
        curr_range[1] = curr_range[1]+(8*(curr_index+1))

    return (curr_range, curr_index)

def find_position(square_range, square_index, num_to_find):
    square_length = ((8*(square_index+1))/4)-1

    if(num_to_find < square_range[0]+square_length):
        return num_to_find-square_range[0]
    elif(num_to_find == square_range[0]+square_length):
        return -1
    elif(num_to_find <= square_range[0]+square_length*2):
        return num_to_find-(square_range[0]+square_length+1)
    elif(num_to_find == square_range[0]+square_length*2+1):
        return -1
    elif(num_to_find <= square_range[0]+square_length*3+1):
        return num_to_find-(square_range[0]+square_length*2+2)
    elif(num_to_find == square_range[0]+square_length*2+2):
        return -1
    elif(num_to_find <= square_range[0]+square_length*4+2):
        return num_to_find-(square_range[0]+square_length*4)
    elif(num_to_find == square_range[1]):
        return -1

def main(num_to_find):
    values = solve_square_range(num_to_find)
    square_index = values[1]
    square_range = values[0]
    square_length = ((8*(square_index+1))/4)-1

    position = int(find_position(square_range, square_index, num_to_find))

    if(position == -1):
        return 2*(square_index+1)
    else:
        modified_pos = abs(int((square_length-1)/2-position))
        if(modified_pos == 0):
            return square_index+1
        else:
            return (square_index+1-modified_pos)+2*modified_pos


if __name__ == '__main__':
    input_num = int(input())
    output = main(input_num)
    print(output)
