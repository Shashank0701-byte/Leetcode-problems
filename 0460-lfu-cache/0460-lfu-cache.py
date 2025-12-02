class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.freq = 1
        self.prev = None
        self.next = None

class DLL:
    def __init__(self):
        self.head = Node(None, None)
        self.tail = Node(None, None)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0

    def addHead(self, node):
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node
        self.size += 1

    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
        self.size -= 1

    def removeTail(self):
        if self.size == 0:
            return None
        tailNode = self.tail.prev
        self.remove(tailNode)
        return tailNode


class LFUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.minFreq = 0
        self.keymap = {}        # key → node
        self.freqmap = {}       # freq → DLL

    def updateFreq(self, node):
        freq = node.freq
        self.freqmap[freq].remove(node)

        if freq == self.minFreq and self.freqmap[freq].size == 0:
            self.minFreq += 1

        node.freq += 1
        newFreq = node.freq

        if newFreq not in self.freqmap:
            self.freqmap[newFreq] = DLL()

        self.freqmap[newFreq].addHead(node)

    def get(self, key: int) -> int:
        if key not in self.keymap:
            return -1

        node = self.keymap[key]
        self.updateFreq(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:
            return
        
        if key in self.keymap:
            node = self.keymap[key]
            node.value = value
            self.updateFreq(node)
            return
        
        if self.size == self.capacity:
            victim = self.freqmap[self.minFreq].removeTail()
            del self.keymap[victim.key]
            self.size -= 1

        newNode = Node(key, value)
        self.keymap[key] = newNode

        if 1 not in self.freqmap:
            self.freqmap[1] = DLL()

        self.freqmap[1].addHead(newNode)
        self.minFreq = 1
        self.size += 1

        


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)