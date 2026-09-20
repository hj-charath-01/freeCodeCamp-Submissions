class HashTable:
    def __init__(self):
        self.collection = {}

    def hash(self, key):
        sum = 0
        for c in key:
            sum += ord(c)
        return sum
    
    def add(self, key, value):
        hashed_key = self.hash(key)
        if hashed_key not in self.collection:
            self.collection[hashed_key] = {key : value}
        else:
            self.collection[hashed_key][key] = value

    def remove(self, key):
        hashed_key = self.hash(key)
        if hashed_key not in self.collection:
            return
        if key not in self.collection[hashed_key]:
            return
        del self.collection[hashed_key][key]

    def lookup(self, key):
        hashed_key = self.hash(key)
        if hashed_key not in self.collection:
            return None
        if key not in self.collection[hashed_key]:
            return None
        return self.collection[hashed_key][key]

