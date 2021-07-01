def solution(words, queries):
    answer = []

    class Trie:
        def __init__(self):
            self.pre_trie = {}
            self.post_trie = {}
            self.len_trie = {}

        def addlen(self, l):
            k = self.len_trie
            if l not in k:
                k[l] = 1
            else:
                k[l] += 1

        def add(self, word, pre):
            l_word = len(word)
            if pre:
                tr = self.pre_trie
            else:
                tr = self.post_trie
            for w in word:
                if w not in tr:
                    tr[w] = {}
                tr = tr[w]

                if not l_word in tr:
                    tr[l_word] = [word]
                else:
                    tr[l_word].append(word)

        def findpre(self, word, pre):
            if pre:
                tr = self.pre_trie
            else:
                tr = self.post_trie
            l_word = len(word)
            for w in word:
                if w != "?" and w not in tr:
                    return 0

                if w == "?":
                    if l_word in tr:
                        return len(tr[l_word])
                    else:
                        return 0
                tr = tr[w]

        def all_question(self, l):
            tr = self.len_trie
            if l in tr:
                return tr[l]
            return 0

    trie = Trie()
    for word in words:
        trie.addlen(len(word))
        trie.add(word, True)
        trie.add(word[::-1], False)

    for q in queries:
        if q[0] == "?" and q[-1] == "?":
            answer.append(trie.all_question(len(q)))
        elif q[0] == "?":
            answer.append(trie.findpre(q[::-1], False))
        else:
            answer.append(trie.findpre(q, True))
    return answer
