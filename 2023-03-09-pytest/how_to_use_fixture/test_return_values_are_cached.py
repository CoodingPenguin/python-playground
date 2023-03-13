import pytest


@pytest.fixture
def first_entry():
    return "a"


@pytest.fixture
def order():
    return []


@pytest.fixture
def append_first(order, first_entry):
    return order.append(first_entry)


def test_string_only(append_first, order, first_entry):
    assert order == [first_entry]