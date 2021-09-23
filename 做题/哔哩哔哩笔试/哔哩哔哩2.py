import datetime


def times(timea, s):
    if s[len(s)-1] in ['W', 'w']:
        if s[0] == '+':
            ti = timea + datetime.timedelta(days=7 * int(s[1:len(s)-1]))
        else:
            ti = timea - datetime.timedelta(days=7 * int(s[1:len(s)-1]))
    elif s[len(s)-1] in ['d', 'D']:
        if s[0] == '+':
            ti = timea + datetime.timedelta(days=1 * int(s[1:len(s)-1]))
        else:
            ti = timea - datetime.timedelta(days=1 * int(s[1:len(s)-1]))
    elif s[len(s)-1] in ['H', 'h']:
        if s[0] == '+':
            ti = timea + datetime.timedelta(hours=1 * int(s[1:len(s)-1]))
        else:
            ti = timea - datetime.timedelta(hours=1 * int(s[1:len(s)-1]))
    elif s[len(s)-1] in ['M', 'm']:
        if s[0] == '+':
            ti = timea + datetime.timedelta(minutes=1 * int(s[1:len(s)-1]))
        else:
            ti = timea - datetime.timedelta(minutes=1 * int(s[1:len(s)-1]))
    elif s[len(s)-1] in ['S', 's']:
        if s[0] == '+':
            ti = timea + datetime.timedelta(seconds=1 * int(s[1:len(s)-1]))
        else:
            ti = timea - datetime.timedelta(seconds=1 * int(s[1:len(s)-1]))
    return ti


t = input()
str1 = input().split()

time1 = datetime.datetime.strptime(t, '%Y-%m-%d %H:%M:%S')

time2 = time1
for i in str1:
    time2 = times(time2, i)
print(time2)
