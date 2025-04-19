
class Trie:
    def __init__(self):
        self.root = {}
        self.end_symbol = "*"

    def add(self,word):
        current = self.root
        for char in word:
            if char not in current:
                current[char] = {}
            current = current[char]
        current[self.end_symbol] = True        
    
    def exists(self,word):
        current = self.root
        for char in word:
            if char not in current:
                return False
            current = current[char]
        return True if self.end_symbol in current else False  
    
    def search_level(self,current_level,current_prefix,words):
        if self.end_symbol in current_level:
            words.append(current_prefix)
        for char in sorted(current_level.keys()):
            if char != self.end_symbol:
                extended_prefix = current_prefix + char
                self.search_level(current_level[char],extended_prefix,words)
        return words        
                    
    def words_with_prefix(self,prefix):
        matching_words = []
        current = self.root
        for char in prefix:
            if char not in current:
                return []
            current = current[char]
        return self.search_level(current,prefix,matching_words)

    def remove(self,word):
        current = self.root
        for char in word:
            if self.end_symbol == current:
                path = current
            current = current[char]
    
    def remove_helper(self,path):
        