#!/usr/bin/env python3
"""
A pagination helper function
"""

import csv
import math
from typing import List


def index_range(page, page_size):
    """
    A paganation helper function
    """
    if (page < 1) or (page_size < 1):
        return (None, None)
    y = page * page_size

    if page == 1:
        x = 0
    else:
        x = y - page_size
    return (x, y)


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """
        Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Method that gets a page
        """
        assert (isinstance(page, int) and isinstance(page_size, int))
        assert ((page > 0) and (page_size > 0))
        assert (page != 0 and page_size != 0)

        index = index_range(page, page_size)
        self.dataset()
        if self.__dataset:
            data = self.__dataset[index[0]:index[1]]
        else:
            data = []
        return data