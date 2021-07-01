def solution(begin, target, words):
    answer = 0
    check = [0 for i in range(len(words))]

    def bfs():
        q = []
        q.append((begin, 0))
        while len(q) != 0:
            w, c = q.pop(0)
            if target == w:
                return c
            for i, word in enumerate(words):
                if check[i]:
                    continue
                count = 0
                for j in range(len(word)):
                    if count >= 2:
                        break
                    if word[j] != w[j]:
                        count += 1
                if count == 1:
                    check[i] = 1
                    q.append((word, c+1))
        return 0

    return bfs()
