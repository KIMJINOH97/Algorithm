from sys import stdin

std = stdin.readline


class Trie:
    def __init__(self):
        self.trie = {}

    def add(self, word):
        tr = self.trie
        for w in word:
            if w not in tr:
                tr[w] = {}
            tr = tr[w]
        tr['*'] = word

    def search(self, word):
        tr = self.trie
        for w in word:
            if w in tr:
                tr = tr[w]
            else:
                return False
        if tr['*'] == word:
            return True


trie = Trie()
