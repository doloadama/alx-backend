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
        self.cache_data[key] = item 
        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            discarded = self.ordre.pop(0)
            del self.cache_data[ordre]
        self.cache_data[key] =  item
        self.indexed.append(key)

    def get(self, key):
        """
        return the value in <self.cache_data> linked to <key>
        if <key> is  None or if the <key> doesn't exist in <sel.cache_data>
        """
        if key is not None and key in self.cache_data.keys():
            return self.cache_data[key]
        return None
