def main():
    programs = get_programs_input()
    checked_values = list(range(len(programs)))
    num_groups = 0

    while len(checked_values) > 0:
        num_groups += 1
        initial_set = set()
        initial_set.add(checked_values[0])
        related_programs = get_programs(programs, initial_set, checked_values[0])
        for to_remove in list(related_programs):
            checked_values.remove(to_remove)
    print(num_groups)

def get_programs(programs, in_set, program):
    for new_prog in programs[str(program)]:
        if new_prog not in in_set:
            in_set.add(new_prog)
            in_set = get_programs(programs, in_set, new_prog)
    return in_set

def get_programs_input():
    programs = {}
    with open('part2.in') as f:
        content = f.readlines()
    
    for line in content:
        line = line.split()
        programs[line[0]] = [int(x.strip(',')) for x in line[2:]]
    return programs

if __name__ == '__main__':
    main()
