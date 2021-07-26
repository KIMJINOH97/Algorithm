def solution(words):
    answer = 0

    class Trie:
        def __init__(self):
            self.dic = {}

        def add(self, word):
            dic = self.dic

            for w in word:
                if w not in dic:
                    dic[w] = {}
                dic = dic[w]
            dic['*'] = word

        def find(self, word):
            dic = self.dic

            index, cnt = 0, 1
            for i, findChar in enumerate(word):
                dic = dic[findChar]
                if len(dic) != 1:
                    cnt = i + 1
                    if cnt < len(word):
                        cnt += 1

            return cnt

    tri = Trie()
    for word in words:
        tri.add(word)

    for word in words:
        answer += tri.find(word)

    return answer
