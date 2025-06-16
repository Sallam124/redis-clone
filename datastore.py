# The DataStore class implements a simple in-memory key-value store.
class DataStore:
    def __init__(self):
        # Dictionary to hold key-value data
        self.store = {}

    def set(self, key, value):
        # Store the value with the given key. Overwrites if key exists.
        self.store[key] = value
        return "OK"  # Return OK like Redis does on SET

    def get(self, key):
        # Return the value for the given key, or '(nil)' if not found
        return self.store.get(key, "no find key")

    def delete(self, key):
        # If key exists, delete it and return 1; otherwise return 0
        if key in self.store:
            del self.store[key]
            return 1
        return 0
