def main():
    directions = input().split(',')

    x = 0
    y = 0
    z = 0

    for direction in directions:
        if direction == 'n':
            y += 1
            z -= 1
        elif direction == 'ne':
            x += 1
            z -= 1
        elif direction == 'se':
            y -= 1
            x += 1
        elif direction == 's':
            y -= 1
            z += 1
        elif direction == 'sw':
            z += 1
            x -= 1
        elif direction == 'nw':
            y += 1
            x -= 1
    print(max(abs(x),abs(y),abs(z)))

if __name__ == '__main__':
    main()
