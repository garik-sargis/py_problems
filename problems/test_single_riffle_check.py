from problems.single_riffle_check import *

__author__ = 'Garegin Sargsyan, Gevorg Soghomonyan'


def test_empty_riffled_once():
    xs = []
    assert riffled_once(xs)


def test_pair_riffled_once():
    xs = [1, 2]
    assert riffled_once(xs)


def test_desc_pair_riffled_once():
    xs = [2, 1]
    assert riffled_once(xs)


def test_triplet_not_riffled_once():
    xs = [3, 2, 1]
    assert not riffled_once(xs)


def test_triplet_riffled_once():
    xs = [1, 3, 2]
    assert riffled_once(xs)


def test_four_card_not_riffled_once():
    xs = [1, 4, 3, 2]
    assert not riffled_once(xs)


def test_four_card_riffled_once():
    xs = [3, 4, 1, 2]
    assert riffled_once(xs)
