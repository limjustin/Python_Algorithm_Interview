class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:

        banned.append('')
        paragraph = list(paragraph)
        wordlist = []
        for x in range(len(paragraph)) :
            if not paragraph[x-1].isalnum() and not paragraph[x].isalnum() :
                pass
            if not paragraph[x].isalnum() :
                wordlist.append(" ")
            elif paragraph[x].isalnum() :
                wordlist.append(paragraph[x])

        wordlist = (''.join(wordlist).lower()).split(' ')

        wordcount = dict()

        for x in range(len(wordlist)) :
            wordcount[wordlist[x]] = wordlist.count(wordlist[x])

        wordcount = dict(sorted(wordcount.items(), key = lambda x : x[1], reverse = True))

        for keys in list(wordcount.keys()) :
            if keys in banned :
                del wordcount[keys]

        res = ""

        # print(wordcount.values())

        # print(wordcount)
        
        for keys in list(wordcount.keys()) :
            # print(keys)
            # print(wordcount[keys])
            if wordcount[keys] == max(wordcount.values()) :
               res = keys 
        
        return res