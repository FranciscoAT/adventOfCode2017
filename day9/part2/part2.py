def main():
    stream = list(input())
    garbage_count = parse_stream(stream)
    print(garbage_count)

def parse_stream(stream):
    garbage_count = 0
    index = 0
    in_garbage = False
    while index < len(stream):
        character = stream[index]
        if not in_garbage:
            if character == '<':
                in_garbage = True
        else:
            if character == '!':
                index += 1
            elif character == '>':
                in_garbage = False
            else:
                garbage_count += 1
        index += 1
    return garbage_count

if __name__ == '__main__':
    main()