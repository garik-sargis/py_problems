from problems.product_of_numbers import *

__author__ = 'Garegin Sargsyan, Gevorg Soghomonyan'


def verify(xs, expected_ys):
    ys = product(xs)
    assert ys == expected_ys


def test_product_empty_list():
    verify([], [])


def test_product_singleton():
    verify([5], [1])


def test_product_two_elems():
    verify([2, 3], [3, 2])


def test_product_three_nums():
    verify([1, 2, 3], [6, 3, 2])


def test_product_four_nums():
    verify([2, 4, 1, 5], [20, 10, 40, 8])
