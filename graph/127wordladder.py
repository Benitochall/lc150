
class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        def differbyone(l, currword):
            words = []
            for word in l:
                if len(word) != len(currword):
                    continue
                else:
                    diffcount = 0

                    for l1, l2 in zip(word, currword):
                        if l1 != l2:
                            diffcount += 1
                        if diffcount > 1:
                            break
                    if diffcount == 1:
                        words.append(word)
            return words

        word_set = set(wordList)

        if endWord not in word_set:
            return 0

        queue = [(beginWord, 1)]

        while queue:
            current_word, length = queue.pop(0)
            if current_word == endWord:
                return length

            differs = differbyone(word_set, current_word)
            for word in differs:
                if word in word_set:
                    queue.append((word, length + 1))
                    word_set.remove(word)

        return 0

# Test the Solution class
if __name__ == '__main__':
    s = Solution()
    beginWord = "hit"
    endWord = "cog"
    wordList = ["hot", "dot", "dog", "lot", "log", "cog"]
    print(s.ladderLength(beginWord, endWord, wordList))
