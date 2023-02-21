#!/usr/bin/env python3
"""
4. MRU Caching
"""
from base_caching import BaseCaching
from collections import OrderedDict


class MRUCache(BaseCaching):
    """
    class caching system
    """

    def __init__(self):
        """
        Initialize the parent init method
        """
        super().__init__()
        self.mru = OrderedDict()

    def put(self, key, item):
        """
        assign to the dictionary <self.cache_data> the <item> value
        for the key <key>
        if <key> or  <item> is None, this method should not do anything
        if the number of items in <self.cache_data> is higher than that
        <BaseCaching.Max_ITEMS>
        DISCARD the last item
        """
        if key is None or item is None:
            pass
        else:
            length = len(self.cache_data)
            if length >= BaseCaching.MAX_ITEMS and key not in self.cache_data:
                print("DISCARD: {}".format(self.usage[-1]))
                del self.cache_data[self.usage[-1]]
                del self.usage[-1]
            if key in self.usage:
                del self.usage[self.usage.index(key)]
            self.usage.append(key)
            self.cache_data[key] = item 

    def get(self, key):
        """Retrieves an item by key"""
        if key is not None and key in self.cache_data.keys(): 
            del self.usage[self.usage.index(key)]
            self.usage.append(key)
            return self.cache_data[key]
            return None
