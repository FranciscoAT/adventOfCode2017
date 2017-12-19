# import operator
def main():
    with open('part1.in') as f:
        instructions = f.readlines()

    registers = {}
    last_played = 0

    # initialize registers
    for command in instructions:
        command = command.split()[1:]
        for register in command:
            if (not register.isdigit() and register not in registers and not register[1:].isdigit()):
                registers[register] = 0

    print(registers)

    index = 0
    while index < len(instructions):
        if (index < 0):
            break
        print(instructions[index], end="")
        command = instructions[index].split()
        if (command[0] == 'snd'):
            last_played = SND(command[1:], registers)
        elif (command[0] == 'set'):
            registers = SET(command[1:], registers)
        elif (command[0] == 'add'):
            registers = ADD(command[1:], registers)
        elif (command[0] == 'mul'):
            registers = MUL(command[1:], registers)
        elif (command[0] == 'mod'):
            registers = MOD(command[1:], registers)
        elif (command[0] == 'rcv'):
            if (registers[command[1]] != 0):
                break
        elif (command[0] == 'jgz'):
            if (registers[command[1]] > 0):
                index += JGZ(command[2], registers)
        print(registers)
        index += 1
    print(last_played)

def SND(command, registers):
    if(command[0] not in registers):
        return int(command[0])
    return registers[command[0]]

def SET(command, registers):
    if(command[1] not in registers):
        registers[command[0]] = int(command[1])
    else:
        registers[command[0]] = registers[command[1]]
    return registers

def ADD(command, registers):
    if(command[1] not in registers):
        registers[command[0]] += int(command[1])
    else:
        registers[command[0]] += registers[command[1]]
    return registers

def MUL(command, registers):
    if(command[1] not in registers):
        registers[command[0]] *= int(command[1])
    else:
        registers[command[0]] *= registers[command[1]]
    return registers

def MOD(command, registers):
    if(command[1] not in registers):
        registers[command[0]] %= int(command[1])
    else:
        registers[command[0]] %= registers[command[1]]
    return registers

def JGZ(command, registers):
    if (command not in registers):
        skip_val = int(command)
    else:
        skip_val = registers[command]
    return skip_val - 1

if __name__ == '__main__':
    main()