class Leaf:
    def __init__(self):
        self.nodes = [None] * 26
        self.end = False
class PrefixTree:
    def __init__(self):
        self.root = Leaf()
    def insert(self, word: str) -> None:
        cur = self.root
        for c in word:
            i = ord(c) - ord('a')
            if cur.nodes[i] == None:
                cur.nodes[i] = Leaf()
            cur = cur.nodes[i]
        cur.end = True

    def search(self, word: str) -> bool:
        cur = self.root
        for c in word:
            i = ord(c) - ord('a')
            if cur.nodes[i] == None:
                return False
            cur = cur.nodes[i]
        return cur.end
    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        for c in prefix:
            i = ord(c) - ord('a')
            if cur.nodes[i] == None:
                return False
            cur = cur.nodes[i]
        return True
        
        