#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
import math
from typing import List, Dict


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
        self.__indexed_dataset = None

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

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """
        The goal here is that if between two queries, certain rows are removed
        from the dataset, the user does not miss items from dataset when
        changing page
        """
        data = self.indexed_dataset()
        assert (index is not None and index >= 0 and index <= max(data.keys()))
        page_info = []
        count = 0
        next_index = None
        if index:
            start_index = index
        else:
            start_index = 0

        for i, item in data.items():
            if i >= start_index and count < page_size:
                page_info.append(item)
                count += 1
                continue
            if count == page_size:
                next_index = i
                break
        return {
            "index": index,
            "next_index": next_index,
            "page_size": len(page_info),
            'data': page_info,
        }
