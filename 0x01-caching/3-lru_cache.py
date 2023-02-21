#!/usr/bin/env python3
"""
3. LRU Caching
"""
from base_caching import BaseCaching
from collections import OrderedDict


class LRUCache(BaseCaching):
    """
    class caching system
    """

    def __init__(self):
        """
        call the parent init
        """
        super().__init__()
        self.lru = OrderedDict()

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
            self.lru[key] = item
            self.lru.move_to_end(key)
            self.cache_data[key] = item
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            discarded = next(iter(self.lru))
            del self.cache_data[discarded]
            print("DISCARD:", discarded)
        if len(self.lru) > BaseCaching.MAX_ITEMS:
            self.lru.popitem(last=False)

    def get(self, key):
        """

        """
        if key and key in self.cache_data.keys():
            return self.cache_data[key]
        return None
