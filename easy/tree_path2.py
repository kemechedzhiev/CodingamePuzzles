#  TODO homework

def get_path(target, path_to_target):
    global structure, target_index, lines_count
    counter = 0
    if counter == lines_count:
        return
    if target == target_index:
        return path_to_target
    else:
        counter += 1
        return 'Left ' + get_path(structure[target]['left'], path_to_target)
        return 'Right ' + get_path(structure[target]['right'], path_to_target)


if __name__ == '__main__':
    structure = dict()
    path = ''
    nodes, target_index, lines_count = int(input()), int(input()), int(input())
    curr = target_index
    for i in range(lines_count):
        [parent, left, right] = [int(x) for x in input().split(' ')]
        structure[parent] = dict(left=left, right=right)
    get_path(target_index, path)
    if path == '':
        path = 'Root'
    print(path.strip())
