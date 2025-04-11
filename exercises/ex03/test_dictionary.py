"""Exercise 03 TEST"""

__author__: str = "730470881"


import pytest
from exercises.ex03.dictionary import invert, favorite_color, count, bin_len


# Tests for invert!
def test_invert_use1():
    assert invert({"a": "b", "c": "d"}) == {"b": "a", "d": "c"}


def test_invert_use2():
    assert invert({"apple": "fruit"}) == {"fruit": "apple"}


def test_invert_edge():
    with pytest.raises(KeyError):
        my_dictionary = {"kris": "jordan", "michael": "jordan"}
        invert(my_dictionary)


# Tests for count!
def test_count_use1():
    assert count(["apple", "banana", "apple", "orange", "banana", "banana"]) == {
        "apple": 2,
        "banana": 3,
        "orange": 1,
    }


def test_count_use2():
    assert count(["apple", "apple", "apple"]) == {"apple": 3}


def test_count_edge():
    assert count([]) == {}


# Tests for favorite_color!
def test_favorite_color_use1():
    assert (
        favorite_color({"Alice": "blue", "Bob": "green", "Charlie": "blue"}) == "blue"
    )


def test_favorite_color_use2():
    assert (
        favorite_color({"Alice": "blue", "Bob": "green", "Charlie": "green"}) == "green"
    )


def test_favorite_color_edge():
    assert favorite_color({}) == ""


# Tests for bin_len!
def test_bin_len_use1():
    assert bin_len(["the", "quick", "fox"]) == {3: {"the", "fox"}, 5: {"quick"}}


def test_bin_len_use2():
    assert bin_len(["dog", "cat", "bat"]) == {3: {"dog", "cat", "bat"}}


def test_bin_len_edge():
    assert bin_len(["apple", "banana", "apple", "grape"]) == {
        5: {"apple", "grape"},
        6: {"banana"},
    }
