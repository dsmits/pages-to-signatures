from signatures import order_signature, order_document


def test_order_one_sheet():
    target = [0, 3, 1, 2]

    signature = order_signature(range(4))
    signature = list(signature)
    assert target == signature


def test_order_two_sheets():
    target = [0, 7, 1, 6, 2, 5, 3, 4]

    signature = order_signature(range(8))
    signature = list(signature)

    assert target == signature


def test_order_two_two_sheet_signatures():
    target = [0, 7, 1, 6, 2, 5, 3, 4, 8, 15, 9, 14, 10, 13, 11, 12]

    result = order_document(16, 2)
    result = list(result)

    assert target == result


def test_order_document_pads_pages():
    num_pages = 14
    target = [0, 7, 1, 6, 2, 5, 3, 4, 8, None, 9, None, 10, 13, 11, 12]

    result = order_document(num_pages, 2)
    result = list(result)

    assert target == result
