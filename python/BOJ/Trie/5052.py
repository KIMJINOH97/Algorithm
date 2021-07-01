from sys import stdin

std = stdin.readline

T = int(std())


class Trie:
    def __init__(self):
        self.trie = {}
        self.ok = True

    def add(self, word):
        tr = self.trie
        for w in word:
            if '*' in tr:
                self.ok = False
            if w not in tr:
                tr[w] = {}
            tr = tr[w]
        tr['*'] = '*'


while T > 0:
    T -= 1
    N = int(std())
    trie = Trie()
    li = []
    for i in range(N):
        li.append(std().rstrip())
    li = sorted(li, key=lambda x: len(x))
    for l in li:
        trie.add(l)
    if trie.ok:
        print('YES')
    else:
        print('NO')
