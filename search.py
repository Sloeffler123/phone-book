
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
                self.search_level(current_level[char],current_prefix + char,words)
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
        if not self.exists(word):
            return
        self.remove_helper(self.root,word,0)
    
    def remove_helper(self,current_node,word,index):
        if index == len(word):
            if self.end_symbol in current_node:
                del current_node[self.end_symbol]
            return len(current_node) == 0
        char = word[index]

        should_delete_current_node = self.remove_helper(current_node[char],word,index + 1)
        if should_delete_current_node:
            del current_node[char]
            return len(current_node) == 0 and self.end_symbol not in current_node
        return False    
        