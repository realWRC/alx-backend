#!/usr/bin/env python3
"""
A pagination helper function
"""


def index_range(page, page_size):
    """
    A paganation helper function
    """
    if page < 1 or page_size < 1:
        return (None, None)
    y = page * page_size

    if page == 1:
        x = 0
    else:
        x = y - page_size
    return (x, y)
