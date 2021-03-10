from sys import stdin

std = stdin.readline

N = int(std())


class Trie:
    def __init__(self):
        self.trie = {}

    def add(self, data):
        tr = self.trie
        for d in data:
            if d not in tr:
                tr[d] = {}
            tr = tr[d]
        #tr['*'] = '*'


trie = Trie()
for i in range(N):
    info = list(std().split())[1:]
    trie.add(info)


def dfs(t, depth):
    if len(t) == 0:
        return

    t = dict(sorted(t.items()))
    # print(t)
    for key in t:
        for i in range(depth):
            print("--", end="")
        print(key)
        dfs(t[key], depth+1)


dfs(trie.trie, 0)
