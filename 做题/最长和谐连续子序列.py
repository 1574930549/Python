# 和谐连续序列是指一个连续序列中元素的最大值和最小值之间的差值正好是1。
# 现在，给定一个整数数组，你需要在所有可能的连续子序列中找到最长的和谐连续子序列的长度。
# 输入描述:
# 一行整数数组，由空格分割
# 输出描述:
# 一行一个数字表示答案，即最长和谐连续子序列的长度
# 输入例子1:
# 1 3 2 2 5 2 3 7
# 输出例子1:
# 3
# 例子说明1:
# 最长的连续和谐子序列是：[3,2,2]
# 输入例子2:
# 1 3 2 2 1 1 2 3
# 输出例子2:
# 5
# 例子说明2:
# 最长的连续和谐子序列是：[2,2,1,1,2]
def hexie(arr):
    n = len(arr)
    if n <= 1:
        return False
    maximum, minimum = arr[0], arr[1]
    if maximum < minimum:
        maximum, minimum = minimum, maximum
    for i in range(2, n):
        if arr[i] > maximum:
            maximum = arr[i]
        elif arr[i] < minimum:
            minimum = arr[i]
    return maximum - minimum == 1


if __name__ == "__main__":
    arr = list(map(int, input().strip().split()))
    n = len(arr)
    maxLen = 0
    for left in range(n):
        for right in range(left + 1, n + 1):
            if hexie(arr[left: right]):
                maxLen = max(maxLen, right - left)
    print(maxLen)