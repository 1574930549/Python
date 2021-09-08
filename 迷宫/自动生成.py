# encoding:utf-8
from random import randint, choice
from enum import Enum




class MAP_ENTRY_TYPE(Enum):
    MAP_EMPTY = 0,
    MAP_BLOCK = 1,


class WALL_DIRECTION(Enum):
    WALL_LEFT = 0,
    WALL_UP = 1,
    WALL_RIGHT = 2,
    WALL_DOWN = 3,


class Map():
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.map = [[0 for x in range(self.width)] for y in range(self.height)]

    def resetMap(self, value):
        for y in range(self.height):
            for x in range(self.width):
                self.setMap(x, y, value)

    def setMap(self, x, y, value):
        if value == MAP_ENTRY_TYPE.MAP_EMPTY:
            self.map[y][x] = 0
        elif value == MAP_ENTRY_TYPE.MAP_BLOCK:
            self.map[y][x] = 1

    def isVisited(self, x, y):
        return self.map[y][x] != 1

    def showMap(self):
        for row in self.map:
            s = ''
            list1 = []
            for entry in row:
                if entry == 0:
                    s += ' 0'
                    list1.append(0)
                    # s +='\033[0;32m' + "#" + " " + '\033[0m'
                elif entry == 1:
                    s += ' 1'
                    list1.append(1)
                    # s += '\033[0;;40m' + " " * 2 + '\033[0m'
                else:
                    s += ' X'
                # print(list1)
            list2.append(list1)
            # print(s)


# 查找四个可能的条目的未访问的相邻条目
# 然后将其中一个随机添加到检查表中，并将其标记为已访问
def checkAdjacentPos(map, x, y, width, height, checklist):
    directions = []
    if x > 0:
        if not map.isVisited(2 * (x - 1) + 1, 2 * y + 1):
            directions.append(WALL_DIRECTION.WALL_LEFT)

    if y > 0:
        if not map.isVisited(2 * x + 1, 2 * (y - 1) + 1):
            directions.append(WALL_DIRECTION.WALL_UP)

    if x < width - 1:
        if not map.isVisited(2 * (x + 1) + 1, 2 * y + 1):
            directions.append(WALL_DIRECTION.WALL_RIGHT)

    if y < height - 1:
        if not map.isVisited(2 * x + 1, 2 * (y + 1) + 1):
            directions.append(WALL_DIRECTION.WALL_DOWN)

    if len(directions):
        direction = choice(directions)
        # print("(%d, %d) => %s" % (x, y, str(direction)))
        if direction == WALL_DIRECTION.WALL_LEFT:
            map.setMap(2 * (x - 1) + 1, 2 * y + 1, MAP_ENTRY_TYPE.MAP_EMPTY)
            map.setMap(2 * x, 2 * y + 1, MAP_ENTRY_TYPE.MAP_EMPTY)
            checklist.append((x - 1, y))
        elif direction == WALL_DIRECTION.WALL_UP:
            map.setMap(2 * x + 1, 2 * (y - 1) + 1, MAP_ENTRY_TYPE.MAP_EMPTY)
            map.setMap(2 * x + 1, 2 * y, MAP_ENTRY_TYPE.MAP_EMPTY)
            checklist.append((x, y - 1))
        elif direction == WALL_DIRECTION.WALL_RIGHT:
            map.setMap(2 * (x + 1) + 1, 2 * y + 1, MAP_ENTRY_TYPE.MAP_EMPTY)
            map.setMap(2 * x + 2, 2 * y + 1, MAP_ENTRY_TYPE.MAP_EMPTY)
            checklist.append((x + 1, y))
        elif direction == WALL_DIRECTION.WALL_DOWN:
            map.setMap(2 * x + 1, 2 * (y + 1) + 1, MAP_ENTRY_TYPE.MAP_EMPTY)
            map.setMap(2 * x + 1, 2 * y + 2, MAP_ENTRY_TYPE.MAP_EMPTY)
            checklist.append((x, y + 1))
        return True
    else:
        # 如果没有找到任何未访问的相邻条目
        return False


# random-prim算法
def randomPrim(map, width, height):
    startX, startY = (randint(0, width - 1), randint(0, height - 1))
    # print("start(%d, %d)" % (startX, startY))
    map.setMap(2 * startX + 1, 2 * startY + 1, MAP_ENTRY_TYPE.MAP_EMPTY)

    checklist = []
    checklist.append((startX, startY))
    while len(checklist):
        # 从检查表中随机选择一个条目
        entry = choice(checklist)
        if not checkAdjacentPos(map, entry[0], entry[1], width, height, checklist):
            # 该条目没有未访问的相邻条目，因此请将其从检查表中删除
            checklist.remove(entry)


def doRandomPrim(map):
    # 将地图的所有条目设置为墙
    map.resetMap(MAP_ENTRY_TYPE.MAP_BLOCK)
    randomPrim(map, (map.width - 1) // 2, (map.height - 1) // 2)


def mark(maze, pos):  # 给迷宫maze的位置pos标"2"表示“倒过了”
    maze[pos[0]][pos[1]] = 2


def passable(maze, pos):  # 检查迷宫maze的位置pos是否可通行
    # print(maze[pos[0]][pos[1]])
    return maze[pos[0]][pos[1]] == 0


def find_path(maze, pos, end):
    mark(maze, pos)
    if pos == end:
        print("已到达出口",pos, end=" ")  # 已到达出口，输出这个位置。成功结束
        path.append(pos)
        return True
    for i in range(4):  # 否则按四个方向顺序检查
        nextp = pos[0] + dirs[i][0], pos[1] + dirs[i][1]
        # print(nextp)
        # 考虑下一个可能方向
        # print(passable(maze, nextp))
        if passable(maze, nextp):  # 不可行的相邻位置不管
            if find_path(maze, nextp, end):  # 如果从nextp可达出口，输出这个位置，成功结束
                # print(pos, end=" ")
                path.append(pos)
                return True
    return False


def see_path(maze, path):  # 使寻找到的路径可视化
    # print("ttt")
    for i, p in enumerate(path):
        # print('i',i,p)
        if i == 0:
            maze[p[0]][p[1]] = "E"
        elif i == len(path) - 1:
            maze[p[0]][p[1]] = "S"
        else:
            maze[p[0]][p[1]] = 3
    print()
    for r in maze:
        for c in r:
            if c == 3:
                print('\033[0;31m' + "*" + " " + '\033[0m', end="")
            elif c == "S" or c == "E":
                print('\033[0;34m' + c + " " + '\033[0m', end="")
            elif c == 2:
                print('\033[0;32m' + "#" + " " + '\033[0m', end="")
            elif c == 1:
                print('\033[0;;40m' + " " * 2 + '\033[0m', end="")
            else:
                print(" " * 2, end="")
        print()


def run():
    WIDTH = 9
    HEIGHT = 9
    map = Map(WIDTH, HEIGHT)
    doRandomPrim(map)
    map.showMap()
    start = (1, 1)
    end = (HEIGHT - 2, WIDTH - 2)
    find_path(list2, start, end)
    see_path(list2, path)


if __name__ == "__main__":
    for i in range(1,10):
        list1 = []
        list2 = []
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # 当前位置四个方向的偏移量
        path = []  # 存找到的路径
        run()
