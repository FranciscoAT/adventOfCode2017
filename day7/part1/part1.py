def main():
    with open('part1.in') as f:
        content = f.readlines()
    roots = []
    leafs = []
    for line in content:
        line = [x.strip(',') for x in line.split()]
        if len(line) > 2:
            roots.append(line[0])
            leafs.extend(line[3:])
    print(set(roots) - set(leafs))

if __name__ == '__main__':
    main()