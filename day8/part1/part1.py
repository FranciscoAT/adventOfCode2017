import operator
def main():
    ops = { 'inc': operator.add, 
            'dec': operator.sub,
            '<':   operator.lt,
            '>':   operator.gt,
            '>=':  operator.ge,
            '<=':  operator.le,
            '==':  operator.eq,
            '!=':  operator.ne}
    register_dict = {}
    instructions = get_instructions('part1.in')

    for instruction in instructions:
        register_dict = parse_instruction(instruction, register_dict, ops)

    highest_register_value = -1
    for register, value in register_dict.items():
        if value > highest_register_value:
            highest_register_value = value
    print(highest_register_value)

def parse_instruction(instruction, register_dict, ops):
    instruction = instruction.split()
    if instruction[0] not in register_dict:
        register_dict[instruction[0]] = 0
    if instruction[4] not in register_dict:
        register_dict[instruction[4]] = 0
    if ops[instruction[5]](register_dict[instruction[4]], int(instruction[6])):
        register_dict[instruction[0]] = ops[instruction[1]](register_dict[instruction[0]], int(instruction[2]))
    return register_dict

def get_instructions(file_name):
    with open(file_name) as f:
        content = f.readlines()
    return content

if __name__ == '__main__':
    main()