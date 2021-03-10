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

        tr['*'] = '*'

    def search(self, word):
        tr = self.trie
        for w in word:
            if w in tr:
                tr = tr[w]
            else:
                return False
        if '*' in tr:
            return True
        return False


N, M = map(int, std().split())
trie = Trie()
for i in range(N):
    trie.add(std().rstrip())

answer = 0

for i in range(M):
    str1 = std().rstrip()
    if trie.search(str1):
        answer += 1

print(answer)
