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

