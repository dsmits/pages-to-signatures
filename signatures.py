from collections import deque


def get_pages_per_signature(sheets_per_signature):
    return sheets_per_signature * 4


def order_signature(range_):
    # Front up, back up, back down, front down
    # 0, 3, 1, 2
    pages = deque(range_)

    while len(pages) > 0:
        yield pages.popleft()
        yield pages.pop()
