import pytest

def add(a, b):
    return a + b

def test_add_positive_numbers():
    # 2 + 3은 5여야 한다는 것을 테스트합니다
    assert add(2, 3) == 5, "2 + 3은 5여야 합니다."