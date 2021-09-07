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
                dic[N] = [word]
            else:
                dic[N].append(word)
                
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
        if query[0] == '?':
            answer.append(trie.find(query[::-1], False))
        else:
            answer.append(trie.find(query, True))
    
    return answer