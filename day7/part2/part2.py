def main():
    with open('part2.in') as f:
        content = f.readlines()
    roots = []
    leafs = []
    tree_dict = {}
    for line in content:
        line = [x.strip(',()') for x in line.split()]
        tree_dict[line[0]] = {'weight': int(line[1]), 'children': line[3:], 'tree_weight': -1}
    # A little cheating here from part 1 :P
    root = 'uownj'

    layer = []
    for branches in tree_dict[root]['children']:
        layer.append((calculate_weight(branches, tree_dict), branches))

    layer_odd = is_layer_odd(layer)

    while(layer_odd):
        next_layer_key = get_odd_key(layer)
        next_layer = generate_layer(next_layer_key, tree_dict)
        layer_odd = is_layer_odd(next_layer)
        if(layer_odd):
            layer = next_layer
    odd_key = get_odd_key(layer)
    difference = get_non_odd_value(odd_key, layer) - tree_dict[odd_key]['tree_weight']
    updated_value = tree_dict[odd_key]['weight'] + difference

    print('Problem key: "{}" / value: {} / updated value: {}'.format(odd_key, tree_dict[odd_key]['weight'], updated_value))

def calculate_weight(key, dict):
    value = dict[key]['weight']
    for branches in dict[key]['children']:
        value += calculate_weight(branches, dict)
    dict[key]['tree_weight'] = value
    return value

def is_layer_odd(layer):
    return len(set(int(x[0]) for x in layer)) == 2

def generate_layer(key, dict):
    new_layer = []
    for branch in dict[key]['children']:
        new_layer.append((dict[branch]['tree_weight'], branch))
    return new_layer

def get_odd_key(layer):
    layer = sorted(layer, key=lambda x: x[0])
    if(layer[0][0] != layer[1][0]):
        return layer[0][1]
    else:
        return layer[-1][1]

def get_non_odd_value(key, layer):
    for root in layer:
        if root[1] != key:
            return root[0]
    return -1

if __name__ == '__main__':
    main()
