def solution(words, queries):
    answer = []

    class Trie:
        def __init__(self):
            self.frontDic = {}
            self.backDic = {}

        def add(self, word, isFront):
            dic = self.frontDic
            if not isFront:
                dic = self.backDic

            N = len(word)
            if N not in dic:
                dic[N] = 1
            else:
                dic[N] += 1

            for w in word:
                if w not in dic:
                    dic[w] = {}
                dic = dic[w]
                if N in dic:
                    dic[N].append(word)
                else:
                    dic[N] = [word]

        def find(self, word, isFront):
            dic = self.frontDic
            if not isFront:
                dic = self.backDic

            N = len(word)
            for w in word:
                if w == '?':
                    break

                if w not in dic:
                    return 0

                dic = dic[w]

            return len(dic[N]) if N in dic else 0

    trie = Trie()
    for word in words:
        trie.add(word, True)
        trie.add(word[::-1], False)

    for query in queries:
        if query[0] == '?' and query[-1] == '?':
            dic = trie.frontDic
            answer.append(dic[len(query)] if len(query) in dic else 0)
        elif query[0] == '?':
            answer.append(trie.find(query[::-1], False))
        else:
            answer.append(trie.find(query, True))

    return answer

# 이분탐색으로 품


def solution(words, queries):
    answer = []

    words = sorted(words, key=lambda x: (len(x), x))
    reverseWords = []

    for word in words:
        reverseWords.append(word[::-1])

    reverseWords = sorted(reverseWords, key=lambda x: (len(x), x))

    lenDic = {}

    index = 0
    preLen, wLen = len(words[0]), 0

    for i, word in enumerate(words):
        wLen = len(word)
        if preLen != wLen:
            lenDic[preLen] = (index, i-1)
            preLen, index = wLen, i

    lenDic[wLen] = (index, len(words) - 1)

    def binSearch(left, right, key, isFront):
        li = words
        if not isFront:
            li = reverseWords

        end = 0
        for i in range(len(key)):
            if key[i] == '?':
                end = i
                break

        key = key[:end]
        l, r = left, right

        while left <= right:
            mid = (left + right) // 2
            if key <= li[mid][:end]:
                right = mid - 1
            else:
                left = mid + 1

        while l <= r:
            mid = (l + r) // 2
            if key < li[mid][:end]:
                r = mid - 1
            else:
                l = mid + 1

        return l - left

    for query in queries:
        qLen = len(query)
        if qLen not in lenDic:
            answer.append(0)
            continue

        start, end = lenDic[qLen]

        if query[0] == '?' and query[-1] == '?':
            answer.append(end - start + 1)
            continue

        if query[0] == '?':
            answer.append(binSearch(start, end, query[::-1], False))
        else:
            answer.append(binSearch(start, end, query, True))

    return answer
