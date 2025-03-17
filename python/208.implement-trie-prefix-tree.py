#
# @lc app=leetcode id=208 lang=python3
#
# [208] Implement Trie (Prefix Tree)
#
# @lc code=start
class Node:
    def __init__(self):
        self.children = [None] * 26
        self.end = False


class Trie:
    def __init__(self):
        self.root = Node()

    def insert(self, word: str) -> None:
        node = self.root
        for c in word:
            o = ord(c) - 97
            if node.children[o] == None:
                node.children[o] = Node()

            node = node.children[o]

        node.end = True

    def search(self, word: str, end=True) -> bool:
        node = self.root
        for c in word:
            o = ord(c) - 97
            if node.children[o] == None:
                return False

            node = node.children[o]

        return node.end if end else True

    def startsWith(self, prefix: str) -> bool:
        return self.search(prefix, False)


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
# @lc code=end
