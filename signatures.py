from collections import deque

DEFAULT_SHEETS_PER_SIGNATURE = 4


def get_pages_per_signature(sheets_per_signature):
    return sheets_per_signature * 4


def order_signature(range_):
    '''
    Order a single signature.

    :param range_:
    :return:
    '''
    pages = deque(range_)

    switch = False

    while len(pages) > 0:
        left = pages.popleft()
        right = pages.pop()

        if switch:
            yield right
            yield left
        else:
            yield left
            yield right

        switch = not switch


def order_document(num_pages, sheets_per_signature=DEFAULT_SHEETS_PER_SIGNATURE):
    '''
    Order all pages in a document into signatures.

    :param num_pages:
    :param sheets_per_signature:
    :return:
    '''
    pages_per_signature = get_pages_per_signature(sheets_per_signature)

    for i in range(0, num_pages, pages_per_signature):
        signature = order_signature(range(i, i + pages_per_signature))

        for p in signature:
            if p < num_pages:
                yield p
            else:
                # Document might need padding at the end
                yield None
