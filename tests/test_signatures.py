from signatures import order_signature, order_document


def test_order_one_sheet():
    target = [0, 3, 2, 1]

    signature = order_signature(range(4))
    signature = list(signature)
    assert target == signature


def test_order_two_sheets():
    target = [0, 7, 6, 1, 2, 5, 4, 3]

    signature = order_signature(range(8))
    signature = list(signature)

    assert target == signature


def test_order_two_two_sheet_signatures():
    target = [0, 7, 6, 1, 2, 5, 4, 3, 8, 15, 14, 9, 10, 13, 12, 11]

    result = order_document(16, 2)
    result = list(result)

    assert target == result


def test_order_document_pads_pages():
    num_pages = 14
    target = [0, 7, 6, 1, 2, 5, 4, 3, 8, None, None, 9, 10, 13, 12, 11]

    result = order_document(num_pages, 2)
    result = list(result)

    assert target == result
