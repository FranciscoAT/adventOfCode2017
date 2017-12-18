def main():
    sequence = input().split(',')
    programs = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p']

    for command in sequence:
        programs = run_command(programs, command)
    print(''.join(programs))

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