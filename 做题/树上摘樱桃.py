# 有一棵二叉树，树上的叶子节点定义为“樱桃”。现在需要找出树上有多少个满足如下子结构的“樱桃”串，即一串上刚好有两颗“樱桃”。
# 输入描述:
# 第一行两个正整数m, n，空格分开，分别代表总共有树上有多少个节点，和树上有多少条边，2<=m<=100,  1<=n<=100
# 下面有n行，每行为3个部分，用空格分割，第一个数字为某非叶子节点的id, 第二个为该边为left还是right，第三个为子节点的id
# 注意：节点id彼此不会重复，id 1为根节点
# 输出描述:
# 一个整数，标示符合要求的子结构的数量
# 输入例子1:
# 10 9
# 1 left 2
# 1 right 3
# 2 left 4
# 2 right 5
# 3 right 6
# 6 left 7
# 6 right 8
# 8 left 9
# 8 right 10
# 输出例子1:
# 2
# 例子说明1:
# 如题目说明的第一个样例图，可以看到，2-4-5子串，8-9-10子串，两个子串符合条件，所以答案为2
n=input().split()
print(type(n))
print(n[0])