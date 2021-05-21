class Node():
    def __init__(self):
        self.key = 0
        self.val = 0
        self.prev = None
        self.next = None

class LRUCache:

    def _remove_node(self, node):
        prev = node.prev
        nxt = node.next

        prev.next = nxt
        nxt.prev = prev

    def _add_node(self, node):
        node.prev = self.head
        node.next = self.head.next

        self.head.next.prev = node
        self.head.next = node

    def _move_to_head(self, node):
        self._remove_node(node)
        self._add_node(node)

    def _pop_tail(self):
        tail = self.tail.prev
        self._remove_node(tail)
        return tail

    def __init__(self, capacity: int):
        self.cap = capacity
        self.size = 0
        self.head, self.tail = Node(), Node()
        self.cache = dict()

        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        node = self.cache.get(key)

        if not node:
            return -1

        self._move_to_head(node)

        return node.val

    def put(self, key: int, value: int) -> None:
        node = self.cache.get(key, None)

        if not node:
            new_node = Node()
            new_node.key = key
            new_node.val = value

            self.cache[key] = new_node
            self._add_node(new_node)

            self.size += 1

            if self.size > self.cap:
                tail = self._pop_tail()
                del self.cache[tail.key]
                self.size -= 1
        else:
            node.val = value
            self._move_to_head(node)




# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
