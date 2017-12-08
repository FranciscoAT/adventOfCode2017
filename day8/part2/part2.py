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
    instructions = get_instructions('part2.in')
    highest_register_value = 0

    for instruction in instructions:
        register_dict,highest_register_value = parse_instruction(instruction, register_dict, ops, highest_register_value)
    print(highest_register_value)

def parse_instruction(instruction, register_dict, ops, highest_register_value):
    instruction = instruction.split()
    if instruction[0] not in register_dict:
        register_dict[instruction[0]] = 0
    if instruction[4] not in register_dict:
        register_dict[instruction[4]] = 0
    if ops[instruction[5]](register_dict[instruction[4]], int(instruction[6])):
        register_dict[instruction[0]] = ops[instruction[1]](register_dict[instruction[0]], int(instruction[2]))
        if register_dict[instruction[0]] > highest_register_value:
            highest_register_value = register_dict[instruction[0]]
    return register_dict, highest_register_value

def get_instructions(file_name):
    with open(file_name) as f:
        content = f.readlines()
    return content

if __name__ == '__main__':
    main()