def main():
    skip = int(input())
    buffer = [0]
    current_pos = 0

    for index in range(1, 2018):
        current_pos = (current_pos+skip)%len(buffer)+1
        buffer.insert(current_pos, index)
    print(buffer[buffer.index(2017)+1])

if __name__ == '__main__':
    main()