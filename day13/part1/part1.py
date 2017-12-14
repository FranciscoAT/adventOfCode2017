def main():
    with open('part1.in') as f:
        content = f.readlines()

    firewall = [0]*(int(content[-1].split(':')[0])+1)
    for wall in content:
        wall = wall.split(':')
        firewall[int(wall[0])] = int(wall[1].strip())

    severity = 0
    for time in range(len(firewall)):
        severity += get_severity(firewall, time)
    print(severity)

def get_severity(firewall, time):
    severity = 0
    if (firewall[time] != 0):
        if (0 == time%((firewall[time]-1)*2)):
            severity =  time*firewall[time]
    return severity

if __name__ == '__main__':
    main()
