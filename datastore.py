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
    def exists(self, key):
        # Return 1 if key exists, 0 if not
        return 1 if key in self.store else 0

    def incr(self, key):
        # Increment the integer value of a key by 1
        if key not in self.store:
            self.store[key] = "1"
            return 1
        try:
            val = int(self.store[key])
            val += 1
            self.store[key] = str(val)
            return val
        except ValueError:
            return "ERR value is not an integer"
