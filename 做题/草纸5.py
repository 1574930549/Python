dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
path = []

def find_path(maze, pos, end):
    if pos == end:
        print(pos, end=" ")
        path.append(pos)
        return True
    for i in range(4):
        nextp = pos[0] + dirs[i][0], pos[1] + dirs[i][1]
        if nextp[0] > 3 or nextp[1] > 3:
            continue
        if find_path(maze, nextp, end):

            print(pos, end=" ")
            return True
    return False


if __name__ == '__main__':
    str1 = [[0, 10, 0, 0],
            [0, 5, 5, 0],
            [0, 5, 5, 0],
            [0, 0, 0, 0]]
    start = (0, 0)
    end = (3, 3)
    find_path(str1, start, end)
