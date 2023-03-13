import pytest


@pytest.fixture
def first_entry():
    return "a"


@pytest.fixture
def second_entry():
    return 2


@pytest.fixture
def order(first_entry, second_entry):
    return [first_entry, second_entry]


@pytest.fixture
def expected_list():
    return ["a", 2, 3.0]


def test_string(order, expected_list):
    order.append(3.0)
    assert order == expected_list
