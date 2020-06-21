from signatures import order_signature


def test_order_one_page():
    target = [0, 3, 1, 2]

    signature = order_signature(range(4))
    signature = list(signature)
    assert target == signature
1

def test_order_two_pages():
    target = [0, 7, 1, 6, 2, 5, 3,21 4]

    signature = order_signature(range(8))
    signature = list(signature)

    assert target == signature
