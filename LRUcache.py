from collections import OrderedDict

class LRUCache:

    def __init__(self, capacity: int):
        self.__size = capacity
        self.__cache = OrderedDict()

    def get(self, key: int) -> int:
        if key in self.__cache:
            self.__cache.move_to_end(key)
            return self.__cache[key]
        return -1

    def put(self, key: int, value: int) -> None:
        if key not in self.__cache:
            if len(self.__cache) == self.__size:
                self.__cache.popitem(last=False)
        else:
            self.__cache.move_to_end(key)
        self.__cache[key] = value

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)