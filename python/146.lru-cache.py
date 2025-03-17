#
# @lc app=leetcode id=146 lang=python3
#
# [146] LRU Cache
#


# @lc code=start
class LRUCache:
    class Node(object):
        key = None
        value = None
        prev = None
        next = None

    def __init__(self, capacity: int):
        self.cap = capacity
        self.m = {}
        self.head, self.tail = self.Node(), self.Node()
        self.head.next = self.tail
        self.tail.prev = self.head

    def insert_node(self, node: "Node", insert_node=None):
        insert_node = insert_node or self.head
        _next = insert_node.next
        node.next = _next
        node.prev = insert_node
        insert_node.next = node
        _next.prev = node

    def remove_node(self, node: "Node"):
        _prev = node.prev
        _next = node.next
        _prev.next = _next
        _next.prev = _prev

    def get(self, key: int) -> int:
        if key not in self.m:
            return -1

        node = self.m[key]
        self.remove_node(node)
        self.insert_node(node)

        return node.value

    def put(self, key: int, value: int) -> None:
        if key in self.m:
            node = self.m[key]
            node.value = value
            del self.m[key]
            self.remove_node(node)

        if len(self.m) == self.cap:
            del self.m[self.tail.prev.key]
            self.remove_node(self.tail.prev)

        node = self.Node()
        node.key = key
        node.value = value
        self.m[key] = node
        self.insert_node(node)


class LRUCacheInnoDB(LRUCache):
    class Node(LRUCache.Node):
        hit = 0
        midpoint = 0

    def __init__(self, capacity: int, old_blocks_pct: int = 37, head_hit: int = 0):
        self.old_bpct = old_blocks_pct
        self.head_hit = head_hit
        self.total = 0
        self.mid_node = None
        super().__init__(capacity=capacity)

    def deviation_mid(self):
        """Handle LRU Pollution."""
        midpoint = int(self.total * (self.old_bpct / 100))
        if not self.mid_node:
            self.mid_node = self.head
            self.mid_node.midpoint = midpoint
        else:
            devi = midpoint - self.mid_node.midpoint
            for _ in range(0, abs(devi)):
                self.mid_node = getattr(self.mid_node, "next" if devi > 0 else "prev")

    def insert_node(self, node: "Node"):
        self.total += 1
        self.deviation_mid()
        head_node = self.head
        if node.hit <= self.head_hit:
            head_node = self.mid_node

        super().insert_node(node, head_node)

    def remove_node(self, node: "Node"):
        self.total -= 1
        self.deviation_mid()
        super().remove_node(node)

    def get_or_set(self, key: int, value: int):
        value = self.get(key)
        if value == -1:
            self.put(key, value)
        else:
            self.m[key].hit += 1

        return value


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
# @lc code=end
