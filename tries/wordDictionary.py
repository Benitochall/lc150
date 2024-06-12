class TrieNode(object):
    
    def __init__(self):
        self.children = [None] * 26
        self.isEndOfWord = False
        self.maxEnd = 0

    def setMaxEnd(self, val):
        self.maxEnd = val
    

class WordDictionary(object):
    def __init__(self):
        self.root = self.getNode()

    def getNode(self):
        return TrieNode()

    def addWord(self, word):
        """
        :type word: str
        :rtype: None
        """
        word.lower()
        tree = self.root
        for i, letter in enumerate(word):
            letter_pos = ord(letter) - ord('a')
            if not tree.children[letter_pos]:
                tree.children[letter_pos] = self.getNode()
            tree.children[letter_pos].setMaxEnd(len(word)-i)
            tree = tree.children[letter_pos]

        tree.isEndOfWord = True

    def search(self, word):
        """
        :type word: str
        :rtype: bool
        """
        tree = self.root
        length = len(word)
        for i, letter in enumerate(word):
            if letter == ".":
                l = [x for x in tree.children if x and x.maxEnd == length-i]
                p = [x for x in tree.children if x and x.isEndOfWord == True]

                if p and length == 1:
                    return True
                # all the children of the correct length 
                if not l:
                    return False
                
                if l and i == length -1 and l[0].isEndOfWord == True:
                    return True
                
                # now we have the case where we need to check the next letter
                
                for child in l:
                    if word[i+1] == ".":
                        tree = child
                        break
                    letter_pos = ord(word[i+1]) - ord('a')
                    if child.children[letter_pos]:
                        tree = child
                        break
                    tree = child
            else:
                letter_pos = ord(letter) - ord('a')
                if tree.children[letter_pos]:
                    if tree.children[letter_pos].isEndOfWord and i == length -1:
                        return True
                    tree = tree.children[letter_pos]  
                else:
                    return False
        return False 

def main():
    wordDictionary = WordDictionary()

    # wordDictionary.addWord("at")
    # wordDictionary.addWord("and")
    # wordDictionary.addWord("an")
    # wordDictionary.addWord("add")
    # # wordDictionary.addWord("adssad")
    # # assert wordDictionary.search("ad..ad") == True
    # assert wordDictionary.search("a") == False
    # assert wordDictionary.search(".at") == False
    # wordDictionary.addWord("bat")
    # assert wordDictionary.search(".at") == True
    # assert wordDictionary.search("an.") == True
    # assert wordDictionary.search("a.d.") == False
    # assert wordDictionary.search("b.") == False
    # assert wordDictionary.search("a.d") == True
    # assert  wordDictionary.search(".") == False

    # ["WordDictionary","addWord","addWord","search","search","search","search","search","search"]
    # ["a"],["a"],["."],["a"],["aa"],["a"],[".a"],["a."]
    wordDictionary.addWord("a")
    wordDictionary.addWord("ab")
    assert wordDictionary.search(".") == True
    assert wordDictionary.search("..") == True
    # assert wordDictionary.search("aa") == False
    # assert wordDictionary.search("a") == True
    # assert wordDictionary.search(".a") == False
    # assert wordDictionary.search("a.") == False


    pass
	

if __name__ == '__main__':
	main()

