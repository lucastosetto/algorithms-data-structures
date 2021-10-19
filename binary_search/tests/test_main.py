import pytest
from binary_search.src.main import binary_search


arr = [1, 3, 6, 10, 14, 25]


def test_should_find_14_in_arr():
    index = binary_search(arr, 14)

    assert index == 4


def test_should_find_1_in_arr():
    index = binary_search(arr, 1)

    assert index == 0


def test_not_should_find_2_in_arr():
    index = binary_search(arr, 2)

    assert index == None


def test_not_should_find_40_in_arr():
    index = binary_search(arr, 40)

    assert index == None