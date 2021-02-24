# You'll write your own hash table and hash function that uses string keys. 
# Your table will store strings in buckets by their first two letters, according to formula:

# Hash Value = (ASCII Value of First Letter * 100) + ASCII Value of Second Letter 

# You can assume that the string will have at least two letters, and the first two characters 
# are uppercase letters (ASCII values from 65 to 90). 
# You can use the Python function ord() to get the ASCII value of a letter, 
# and chr() to get the letter associated with an ASCII value.

# Remember to store lists at each bucket, and not just the string itself. 
# For example, you can store "UDACITY" at index 8568 as ["UDACITY"].

"""Write a HashTable class that stores strings in a hash table, where keys are calculated using 
the first two letters of the string."""
# table = { hashValue1: ['word1', word2], hashValue2: ['word3'], ... }

class HashTable(object):
    def __init__(self):
        self.table = {}

    def store(self, word):
        """Input a string that's stored in the table."""
        hash_value = self.calculate_hash_value(word)
        if hash_value in self.table:
            self.table[hash_value].append(word)
        else:
            self.table[hash_value] = [word]  

    def lookup(self, word):
        """Return the hash value if the string is already in the table.
        Return -1 otherwise."""
        hash_value = self.calculate_hash_value(word)
        if hash_value in self.table:
            arr = self.table[hash_value]
            if word in arr:       
                return hash_value
        return -1

    def calculate_hash_value(self, word):
        """Helper function to calulate a hash value from a string."""
        hash_value = (ord(word[0]) * 100) + ord(word[1]) 
        return hash_value
    
# Setup
hash_table = HashTable()

# Test calculate_hash_value
print(hash_table.calculate_hash_value('UDACITY'))   # Should be 8568

# Test lookup edge case
print(hash_table.lookup('UDACITY'))    # Should be -1

# Test store
hash_table.store('UDACITY')
print(hash_table.lookup('UDACITY'))    # Should be 8568

# Test store edge case
hash_table.store('UDACIOUS')
print(hash_table.lookup('UDACIOUS'))   # Should be 8568
