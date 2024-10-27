#!/usr/bin/env python3
"""
A pagination helper function
"""

import csv
import math
from typing import Any, List, Dict


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

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict[str, Any]:
        """
        Method returs a dict with multipe key value pairs
        """
        data = self.get_page(page, page_size)
        start_index, end_index = index_range(page, page_size)
        total = math.ceil(len(self.__dataset) / page_size)
        info = {
            'page_size': len(data),
            'page': page,
            'data': data,
            'next_page': page + 1 if end_index < len(self.__dataset) else None,
            'prev_page': page - 1 if start_index > 0 else None,
            'total_pages': total
        }
        return info
