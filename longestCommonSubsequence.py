class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        if len(text1) < len(text2):
            text1, text2 = text2, text1
        l1, l2 = len(text1), len(text2)
        curr = [0] * (l2 + 1)
        prev = [0] * (l2 + 1)
        for i in range(l1):
            for j in range(l2):
                if text1[i] == text2[j]:
                    curr[j+1] = prev[j] + 1
                else:
                    if curr[j] > prev[j+1]:
                        curr[j+1] = curr[j]
                    else:
                        curr[j+1] = prev[j+1]
            curr, prev = prev, curr
        return prev[-1]