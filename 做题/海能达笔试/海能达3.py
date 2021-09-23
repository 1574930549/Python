def isMatch(s,p):
    lp=len(p)
    ls=len(s)
    dp=[set()for i in range(lp+1)]
    dp[0].add(-1)
    for i in range(lp):
        if p[i]=='?':
            for x in dp[i]:
                if x+1<ls:
                    dp[i+1].add(x+1)
        elif p[i]=='*':
            minx=ls
            for x in dp[i]:minx=min(minx,x)
            while minx<ls:
                dp[i+1].add(minx)
                minx+=1
        else:
            for x in dp[i]:
                if x+1<ls and s[x+1]==p[i]:
                    dp[i+1].add(x+1)
        if ls-1 in dp[-1]:
            return True
        return False
print(isMatch('aa','a'))