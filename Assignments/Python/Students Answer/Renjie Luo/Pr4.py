class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0: return ""
        minLen = sys.maxsize
        for s in strs:
            minLen = min(minLen, len(s))
        for i in range(minLen):
            for j in range(len(strs) - 1):
                if strs[j][i] != strs[j + 1][i]:
                    return strs[j][:i] if i != 0 else ""
        return strs[0][:minLen]
            