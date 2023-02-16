#!/usr/bin/env python3
"""
0. Simple helper function
"""
from typing import Tuple


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
