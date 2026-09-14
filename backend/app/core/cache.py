from time import time

class TTLCache:
    def __init__(self, ttl_seconds: int = 300):
        self.ttl_seconds = ttl_seconds
        self._data = {}

    def get(self, key):
        item = self._data.get(key)
        if not item:
            return None
        value, expires = item
        if time() >= expires:
            self._data.pop(key, None)
            return None
        return value

    def set(self, key, value):
        self._data[key] = (value, time() + self.ttl_seconds)

repo_cache = TTLCache()
