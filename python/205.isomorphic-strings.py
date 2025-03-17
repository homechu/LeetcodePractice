#
# @lc app=leetcode id=205 lang=python3
#
# [205] Isomorphic Strings
#


# @lc code=start
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        mmap = {}
        for i, c in enumerate(s):
            if c in mmap:
                if mmap[c] != t[i]:
                    return False

            elif t[i] in mmap.values():
                return False

            mmap[c] = t[i]

        return True


# @lc code=end
