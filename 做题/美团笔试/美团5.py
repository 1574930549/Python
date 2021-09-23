n=int(input())
s=''
for i in range(n-1):
    s=s+'1'
# s = '111111'
# print(s)
dp = [0] * (len(s)+1)
dp[0] = 1
dp[1] = 1
s1 = s[::-1]
# print(s1)
for i in range(2, len(s)+1):
    if i > 2:
        if s1[i-3:i][::-1] in ['111']:
            dp[i] += dp[i-3]
        if s1[i-4:i][::-1] in ['1111']:
            dp[i] += dp[i-3]
        if s1[i-5:i][::-1] in ['11111']:
            dp[i] += dp[i-3]
        if s1[i-6:i][::-1] in ['111111']:
            dp[i] += dp[i-3]
        if s1[i-2:i][::-1] in ['11']:
            dp[i] += dp[i-2]
        dp[i] += dp[i-1]
    elif i > 1:
        if s1[i-2:i][::-1] in ['10', '11']:
            dp[i] += dp[i-2]
        dp[i] += dp[i-1]
# print(dp)
print(dp[-1]%(2**32))