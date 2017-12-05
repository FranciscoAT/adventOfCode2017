def main():
    with open('part2.in') as f:
        content = f.readlines()
    content = [int(x.strip()) for x in content]

    num_steps = traverse_list(content)
    print(num_steps)

def traverse_list(maze):
    index = 0
    num_steps = 0
    while (index > -1 and index < len(maze)):
        new_index = index + maze[index]
        if maze[index] < 3:
            maze[index] += 1
        else:
            maze[index] -= 1
        num_steps += 1
        index = new_index
    return num_steps

if __name__ == '__main__':
    main()