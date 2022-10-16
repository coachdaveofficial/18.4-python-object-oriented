"""Word Finder: finds random words from a dictionary."""

from random import choice

class WordFinder:
    def __init__(self,path):
        self.word_count = 0 
        word_file = open(path)
        self.word_count = self.parse(word_file)
        print(self.word_count, " words read")
    
    def count(self, word_file):
        for line in word_file:
            self.word_count += 1
        return self.word_count

    def random(self):
        self.file = open(self.path).read().splitlines()
        return choice(self.file)
       


# 
class SpecialWordFinder:
    def __init__(self,path):
        super().__init__(self,path)
    
    def count(self, word_file):
        for line in word_file:
            self.word_count += 1
        return self.word_count

    
    # def random(self):
    #     super.random(self)
    #     while True:
    #         if self.random_choice.startswith('\n') or self.random_choice.startswith('#'):
    #             self.random_choice = choice(self.file)
    #         break
    #     print(self.random_choice)
    