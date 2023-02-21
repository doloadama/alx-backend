#!/usr/bin/env python3
"""
0. Basic dictionary
"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """
     class BasicCache that inherits from BaseCaching
    and is a caching system
    """

    def __init__(self):
        """Initializes the class using the parent class
        """
        BaseCaching.__init__(self)

    def put(self, key, item):
        """
        Assign to the dictionary <self.cache_data> the item value
        for the key <key>
        if <key> or <item> is None, this method should not not
        anything
        """
        if key is None or item is None:
            pass
        else:
            self.cache_data[key] = item

    def get(self, key):
        """
        return the value in <self.cache_data> linked to <key>
        if <key> is None or if the <key> doesn't exist in <sel.cache_data>
        return None
        """
        if key is not None and key in self.cache_data.keys():
            return self.cache_data[key]
        return None
