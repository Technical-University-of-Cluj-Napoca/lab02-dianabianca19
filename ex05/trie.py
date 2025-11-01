class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
        self.count = 0

    def insert(self, word):
        node = self.root
        for ch in word.lower():
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
        if not node.is_end:
            node.is_end = True
            self.count += 1

    def build_from_list(self, words):
        for w in words:
            self.insert(w.strip())

    def starts_with(self, prefix):
        #true if there's any word starting with prefix
        node = self.root
        for ch in prefix.lower():
            if ch not in node.children:
                return False
            node = node.children[ch]
        return True

    def search(self, word):
        #true if word exists in Trie
        node = self.root
        for ch in word.lower():
            if ch not in node.children:
                return False
            node = node.children[ch]
        return node.is_end
