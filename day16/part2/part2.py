def main():
    sequence = input().split(',')
    programs = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p']
    program_string = ''.join(programs)
    seen = [program_string]

    for index in range(1000000000):
        for command in sequence:
            programs = run_command(programs, command)
        program_string = ''.join(programs)
        if program_string not in seen:
            seen.append(program_string)
        else:
            index_of_seen = seen.index(program_string)
            seen = seen[index_of_seen:]
            program_string = seen[(1000000000-index-1)%len(seen)]
            break
    print(program_string)

def run_command(programs, command):
    if(command[0] == 's'):
        num_to_switch = -1*int(command[1:])
        programs = programs[num_to_switch:]+programs[0:num_to_switch]
    elif(command[0] == 'x'):
        command = [int(x) for x in command[1:].split('/')]
        programs[command[0]], programs[command[1]] = programs[command[1]], programs[command[0]]
    elif(command[0] == 'p'):
        command = command[1:].split('/')
        index_1, index_2 = [programs.index(x) for x in command]
        programs[index_1], programs[index_2] = programs[index_2], programs[index_1]
    return programs

if __name__ == '__main__':
    main()