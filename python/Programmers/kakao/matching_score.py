import re


def solution(word, pages):
    answer = 0
    word = word.lower()
    # 기본점수, 외부 링크 수, 링크 점수, 매칭점수(기본 + 링크)

    class Node:
        def __init__(self, index, external):
            self.index = index
            self.external = external
            self.basicScore = 0
            self.linkScore = 0

        def setBasicScore(self, score):
            self.basicScore = score

        def addLinkScore(self, score):
            self.linkScore += score

        def printer(self):
            print(self.index, self.external, self.basicScore, self.linkScore)

    node = {}
    urlParser = re.compile('<a href="(\S+)"')

    for i, page in enumerate(pages):
        urls = urlParser.findall(page)
        pageUrl = re.findall(
            '<meta property="og:url" content="(\S+)"', page)[0]
        node[pageUrl] = Node(i, urls)
        filterList = list(filter(lambda x: len(x) >= len(
            word), re.compile('[a-zA-Z]+').findall(page)))
        cnt = 0
        for w in filterList:
            if w.lower() == word:
                cnt += 1
        node[pageUrl].setBasicScore(cnt)

    ans = []
    for key in node:
        ex = node[key].external
        for e in ex:
            if e in node:
                linkScore = node[key].basicScore / len(node[key].external)
                node[e].addLinkScore(linkScore)

    for key in node:
        ans.append(
            (node[key].index, node[key].basicScore + node[key].linkScore))

    ans = sorted(ans, key=lambda x: (-x[1], x[0]))

    return ans[0][0]
