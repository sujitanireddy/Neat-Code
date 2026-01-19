#Building Tries in Python

"""
Example Tree:
{
	"h": {
		"e": {
			"l": {
				"l": {
					"o": {
						"*": True
					}
				},
				"p": {
					"*": True
				}
			}
		},
		"i": {
			"*": True
		}
	}
}
"""

class Trie:

    #method to check if the given word exists in the tree
    def exists(self,word):

        current_dict = self.root

        for c in word:
            if c not in current_dict:
                return False
            
            current_dict = current_dict[c]
            
            if self.end_symbol in current_dict:
                return True
            
            else:
                return False


    #method to insert into a tree
    def insert(self,word):

        current_level = self.root

        for c in word:
            if c not in current_level:
                current_level[c] = {}
                current_level = current_level[c]
        
        current_level[self.end_symbol] = True


    def __init__(self):
        self.root = {}
        self.end_symbol = '*'


    #This function collects all complete words starting from the current trie level. It takes the current dictionary level, the accumulated prefix so far, and the collection of words found.
    def search_level(self, current_level, current_prefix, words):

        if self.end_symbol in current_level:
            words.append(current_prefix)

        current_level_keys = current_level.keys()
        sorted_current_level_keys = sorted(current_level_keys)
        
        for char in sorted_current_level_keys:

            if char == self.end_symbol:
                continue

            new_current_prefix = current_prefix + char

            self.search_level(current_level[char], new_current_prefix, words)

        return words
            
    #his finds all words in the trie that begin with a given prefix.
    def words_with_prefix(self, prefix):

        matching_words = []

        current_level = self.root

        for c in prefix:

            if c not in current_level:
                return matching_words

            current_level = current_level[c]

        return self.search_level(current_level, prefix, matching_words)
    
    #function to find substring matches with advance matching (including variations)
    def advanced_find_matches(self, document, variations):
        matches = set()
        for i in range(len(document)):
            level = self.root
            for j in range(i, len(document)):
                ch = document[j]

                if ch in variations:
                    ch = variations[ch]
                
                if ch not in level:
                    break
                    
                level = level[ch]
                if self.end_symbol in level:
                    matches.add(document[i : j + 1])
        return matches
    

    #Functions to find the longest common prefix of a list of words
    def longest_common_prefix(self):
        current = self.root
        prefix = ""
        while True:
            children = []
            for key in current.keys():
                if key == self.end_symbol:
                    break
                children.append(key)
            if len(children) == 1:
                prefix += children[0]
                current = current[children[0]]
            else:
                break
        return prefix