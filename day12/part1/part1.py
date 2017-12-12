def main():
    programs = get_programs_input()
    initial_set = set()
    initial_set.add(0)
    related_programs = get_programs(programs, initial_set, 0)
    print(len(related_programs))

def get_programs(programs, in_set, program):
    for new_prog in programs[str(program)]:
        if new_prog not in in_set:
            in_set.add(new_prog)
            in_set = get_programs(programs, in_set, new_prog)
    return in_set

def get_programs_input():
    programs = {}
    with open('part1.in') as f:
        content = f.readlines()
    
    for line in content:
        line = line.split()
        programs[line[0]] = [int(x.strip(',')) for x in line[2:]]
    return programs

if __name__ == '__main__':
    main()
