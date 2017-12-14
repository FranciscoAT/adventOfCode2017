def main():
    with open('part2.in') as f:
        content = f.readlines()

    firewall = [0]*(int(content[-1].split(':')[0])+1)
    for wall in content:
        wall = wall.split(':')
        firewall[int(wall[0])] = int(wall[1].strip())

    delay = 0
    valid = False
    while not valid:
        valid = True
        for time in range(len(firewall)):
            if (firewall[time] != 0):
                if ((time+delay)%((firewall[time]-1)*2) == 0):
                    valid = False
                    delay += 1
                    break
    print(delay)

if __name__ == '__main__':
    main()
