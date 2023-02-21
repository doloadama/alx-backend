#!/usr/bin/env python3
"""
1. FIFO caching
"""
from base_caching import BaseCaching
from collections import OrderedDict


class FIFOCache(BaseCaching):
    """
    caching system
    FIFO
    """

    def __init__(self):
        """
        call the parent init
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
        """
        if key is None or item is None:
            pass
        else:
            length = len(self.cache_data)
            if length >= BaseCaching.MAX_ITEMS and key not in self.cache_data:
                print("DISCARD: {}".format(self.ordre[0]))
                del self.cache_data[self.ordre[0]]
                del self.ordre[0]
            self.ordre.append(key)
            self.cache_data[key] = item

    def get(self, key):
        """
        return the value in <self.cache_data> linked to <key>
        if <key> is  None or if the <key> doesn't exist in <sel.cache_data>
        """
        if key is not None and key in self.cache_data.keys():
            return self.cache_data[key]
        return None
