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
        self.cache_data = OrderedDict()

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
            return
        if key not in self.cache_data:
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                mru, _ = self.cache_data.popitem(False)
                print("DISCARD:", mru)
            self.cache_data[key] = item
        else:
            self.cache_data[key] = item

    def get(self, key):
        """Retrieves an item by key"""
        if key is None and key not in self.cache_data.keys():
            return None
        return self.cache_data[key]
