class Solution:
    def lengthOfLongestSubstring(self, s):

        if len(s) == 0:
            return 0
        else:
            length = 0
            arr = {}
            num = 0
            p = 0
            for i in range(len(s)):
                if (s[i] in arr and arr[s[i]] >= p):
                    p = arr[s[i]] + 1
                num = i - p + 1
                arr[s[i]] = i
                length = max(length, num)
        return length


s = Solution()
print(s.lengthOfLongestSubstring('abcabcbb'))
