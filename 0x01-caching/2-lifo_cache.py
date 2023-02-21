#!/usr/bin/env python3
"""
2. LIFO Caching
"""
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """
    caching system using LIFO
    """

    def __init__(self):
        """
        parent init
        """
        super().__init__()
        self.ordre = []

    def put(self, key, item):
        """
        assign to the dictionary <self.cache_data> the <item> value
        for the key <key>
        if <key> or  <item> is None, this method should not do anything
        if the number of items in <self.cache_data> is higher than that
        <BaseCaching.Max_ITEMS>
        DISCARD the last item
        """
        if key and item:
            if len(self.cache_data) >= self.MAX_ITEMS:
                if key in self.cache_data:
                    del self.cache_data[key]
                    self.ordre.remove(key)
                else:
                    del self.cache_data[self.ordre[self.MAX_ITEMS - 1]]
                    item_discarded = self.ordre.pop(self.MAX_ITEMS - 1)
                    print("DISCARD:", item_discarded)

            self.cache_data[key] = item
            self.ordre.append(key)

    def get(self, key):
        """ 
        return the value in <self.cache_data> linked to <key>
        if <key> is  None or if the <key> doesn't exist in <sel.cache_data>
        """
        if key and key in self.cache_data.keys():
            return self.cache_data[key] 
