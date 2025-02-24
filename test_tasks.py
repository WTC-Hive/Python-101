import pytest
from tasks import (
    get_user_info,
    calculate_bmi,
    create_shopping_list,
    count_word_frequency,
    check_number,
    sum_even_numbers,
    find_first_negative,
    analyze_text,
)

def test_get_user_info(monkeypatch):
    inputs = ["Alice", "25", "Blue"]
    monkeypatch.setattr("builtins.input", lambda _: inputs.pop(0))
    result = get_user_info()
    assert result == {"name": "Alice", "age": "25", "favorite_color": "Blue"}

def test_calculate_bmi():
    assert calculate_bmi(70, 1.75) == 22.86
    assert calculate_bmi(60, 1.65) == 22.04

def test_create_shopping_list():
    assert create_shopping_list(["apple", "banana", "apple"]) == {"apple": 2, "banana": 1}
    assert create_shopping_list(["milk", "bread", "bread", "eggs"]) == {"milk": 1, "bread": 2, "eggs": 1}

def test_count_word_frequency():
    assert count_word_frequency("hello world hello") == {"hello": 2, "world": 1}
    assert count_word_frequency("the quick brown fox") == {"the": 1, "quick": 1, "brown": 1, "fox": 1}

def test_check_number():
    assert check_number(10) == "Positive"
    assert check_number(-5) == "Negative"
    assert check_number(0) == "Zero"

def test_sum_even_numbers():
    assert sum_even_numbers([1, 2, 3, 4, 5, 6]) == 12
    assert sum_even_numbers([10, 15, 20, 25]) == 30

def test_find_first_negative():
    assert find_first_negative([1, 2, -3, 4, -5]) == -3
    assert find_first_negative([1, 2, 3, 4]) is None

def test_analyze_text():
    assert analyze_text("Hello world") == {"word_count": 2, "vowel_count": 3}
    assert analyze_text("Python is fun") == {"word_count": 3, "vowel_count": 3}
