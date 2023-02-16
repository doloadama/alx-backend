#!/usr/bin/env python3
"""
1. Simple pagination
"""
import csv
from typing import List, Tuple, Dict
import math


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """_summary_

    Args:
        page (_type_): _description_
        page_size (_type_): _description_

    Returns:
        Tuple[int, int]: _description_
    """
    debut, fin = 0, 0
    for i in range(page):
        debut = fin
        fin += page_size
    return (debut, fin)

class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Implement a method named get_page that takes two
        integer arguments page with
        default value 1 and page_size with default value 10.
        Use assert to verify that both arguments are
        integers greater than 0.
        Use index_range to find the correct indexes to paginate
        the dataset correctly and
        return the appropriate page of the dataset
        (i.e. the correct list of rows).
        If the input arguments are out of range for the dataset,
        an empty list should be returned.
        """
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0
        start, end = index_range(page, page_size)
        dataset = self.dataset()
        if start >= len(dataset):
            return []

        return dataset[start:end]


    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        """
        Implement a get_hyper method that takes the same arguments
        (and defaults) as get_page and returns a dictionary containing
        the following key-value pairs:
        page_size: the length of the returned dataset page
        page: the current page number
        data: the dataset page (equivalent to return from previous task)
        next_page: number of the next page, None if no next page
        prev_page: number of the previous page, None if no previous page
        total_pages: the total number of pages in the dataset as an integer
        Make sure to reuse get_page in your implementation.
        """
        dataset = self.dataset()
        total_pages = len(self.dataset()) // page_size + 1
        data = self.get_page(page, page_size)
        informations = {
            "page_size": page_size if page_size <= len(data) else len(data),
            "page": page,
            "data": data,
            "next_page": page + 1 if page + 1 <= total_pages else None,
            "prev_page": page - 1 if page > 1 else None,
            "total_pages": total_pages,
        }
        return informations
