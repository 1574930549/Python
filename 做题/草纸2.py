def test(que,m):
    str1 = 'ABCDEFGHIJKLM'
    str2 = 'ZYXWVUTSRQPON'
    que1 = que
    arr = {}
    for i in range(len(str1)):
        arr[str1[i]] = i
        arr[str2[i]] = i + 1
    ans = []
    now = arr[que[0]]
    ans2 = 0
    ans3 = 0
    for i in que:
        ans.append(abs(arr[i] - now))
        ans2 = ans2 + abs(arr[i] - now)
        ans3 = ans3 + abs(arr[i] - now)
        now = arr[i]
    ans1 = []
    for i in ans:
        if i >= 2:
            ans1.append(i)
    ans1 = sorted(ans1)
    if m > 0:
        for i in range(m):
            if que1 == que1[::-1]:
                ans3 = ans3 + 1
                que1 = que1[0:len(que1) - 2]
                continue
            else:
                ans3 = ans3 + 1
                ans3 = ans3 - ans1[len(ans1) - 1 - i]
                del ans1[len(ans1) - 1 - i]
    if ans2 + len(que) > ans3 + len(que):
        return ans3 + len(que)
    else:
        return ans2 + len(que)

cin = input().split()
que = cin[0]
m = int(cin[1])
print(test(que,m))