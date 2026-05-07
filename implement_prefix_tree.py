class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEndOfWord = False


class PrefixTree:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        curr = self.root
        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode()
            curr = curr.children[char]
        curr.isEndOfWord = True

    def search(self, word):
        curr = self.root

        for char in word:
            if char in curr.children:
                curr = curr.children[char]
            else:
                return False
        if curr.isEndOfWord:
            return True

    def startsWith(self, prefix):
        curr = self.root

        for char in prefix:
            if char in curr.children:
                curr = curr.children[char]
            else:
                return False
        return True
