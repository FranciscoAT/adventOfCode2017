def main():
    stream = list(input())
    score = parse_stream(stream)
    print(score)

def parse_stream(stream):
    score = 0
    depth = 0
    index = 0
    in_garbage = False
    while index < len(stream):
        character = stream[index]
        if not in_garbage:
            if character == '{':
                depth += 1
            elif character == '<':
                in_garbage = True
            elif character == '}':
                score += depth
                depth -= 1
        else:
            if character == '!':
                index += 1
            elif character == '>':
                in_garbage = False
        index += 1
    return score

if __name__ == '__main__':
    main()