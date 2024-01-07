'''
	Here is a basic trie data stucture 
	The trie class has three methods 
'''

'''
	TrieNode, this represents an indiviudal node in the trie, we intially mark its children as 26 blank arrays
	then when we add a letter in as a child of the current node we can put it at the postion of the letter, this 
	basically any letter can follow any letter. Haveing it this way means we don't need to keep track of psoinot
	The isEndOfWord is used to keep track if the workd is in the tree
'''
class TrieNode(object):
	
	def __init__(self):
		self.children = [None]*26
		self.isEndOfWord = False

'''
	the trie class has 4 methods 
	__init__ this is required for every class, sets up the root as a blank tree node, the self.root variable can be accessed anywhere
	the self.root calls get_node which returns a tree node
'''

class Trie:
	
	# Trie data structure class
	def __init__(self):
		self.root = self.getNode()
	# returns a blank tree node
	def getNode(self):
		return TrieNode()

	def insert(self,key):
		# inserting in to the tree
		# always start at the root
		pCrawl = self.root
		length = len(key) # this is how many levels we descend into the tree
		for level in range(length): # for each letter 
			index = ord(key[level]) - ord('a') # gets the index of the current letter 

			# if current character is not present
			if not pCrawl.children[index]: # see if the current letter has been filled in yet as the child of the current node
				pCrawl.children[index] = self.getNode() # if the letter does not exist initalize the letter to be a blank tree node
			pCrawl = pCrawl.children[index] # go to the next level of the tree

		# mark last node as leaf
		pCrawl.isEndOfWord = True # since we are inserting the last level of the tree should be marked as the end of a word 

	def search(self, key):
		# now we are searching 
		pCrawl = self.root # start at the root 
		length = len(key) # set the lenght to be the lenght 
		for level in range(length):
			index = ord(key[level]) - ord('a') # get the index 
			if not pCrawl.children[index]: # if the child doesnt exit there is no company in here 
				return False
			pCrawl = pCrawl.children[index] # go to the next node 

		return pCrawl.isEndOfWord # if the last letter is end of word we have a tree

# driver function
def main():

	# Input keys (use only 'a' through 'z' and lower case)
	keys = ["the","a","there","anaswe","any",
			"by","their"]
	output = ["Not present in trie",
			"Present in trie"]

	# Trie object
	t = Trie()

	# Construct trie
	for key in keys:
		t.insert(key)

	# Search for different keys
	print("{} ---- {}".format("the",output[t.search("the")]))
	print("{} ---- {}".format("these",output[t.search("these")]))
	print("{} ---- {}".format("their",output[t.search("their")]))
	print("{} ---- {}".format("thaw",output[t.search("thaw")]))

if __name__ == '__main__':
	main()

# This code is contributed by Atul Kumar (www.facebook.com/atul.kr.007)

