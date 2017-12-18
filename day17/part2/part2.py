def main():
    skip = int(input())
    current_pos = 0
    after_zero = 0

    for index in range(1, 50000000):
        current_pos = (current_pos+skip)%index+1
        if current_pos == 1:
            after_zero = index
    print(after_zero)

if __name__ == '__main__':
    main()