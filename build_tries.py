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
    
    #function to find substring matches.
    def find_matches(self, document):
        
        matched_words = set()

        for i in range(len(document)):

            current_level = self.root

            for j in range(i, len(document)):

                if document[j] not in current_level:
                    break

                else:
                    current_level = current_level[document[j]]

                if self.end_symbol in current_level:

                    substring = document[i:j + 1]

                    matched_words.add(substring)

        return matched_words