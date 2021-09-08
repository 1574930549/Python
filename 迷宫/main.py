# encoding:utf-8
from Maze import Maze
from Player import Player
from Controller import Controller
import turtle
turtle.tracer(False)
maze_list = [
  [1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1],
  [1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1],
  [1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1],
  [1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1],
  [1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1],
  [1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1],
  [1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1],
  [1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1],
  [1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1],
  [1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1],
  [1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 0, 0, 1],
  [1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1],
  [1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1]
]

Maze(maze_list)
#0,5表示玩家起始的位置；12,7表示终点的位置
player = Player(maze_list, 0, 5, 12, 7)
Controller(player.go_up, player.go_down, player.go_left, player.go_right)
turtle.exitonclick()
