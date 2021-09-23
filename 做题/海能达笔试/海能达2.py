def pipei(str1):
    while '()' in str1 or "[]" in str1 or "{}" in str1:
        str1 = str1.replace("()", "").replace("[]", "").replace("{}", "")
    return len(str1) == 0


str1 = "((()))"
str2 = "({({})})"
str3 = "[{([{{()}}])}]"
str4 = "((({{{[[[}}}]]])))"
print(pipei(str1))
print(pipei(str2))
print(pipei(str3))
print(pipei(str4))
