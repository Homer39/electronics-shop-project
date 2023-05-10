from src.keyboard import Keyboard
import pytest


@pytest.fixture()
def kb():
    return Keyboard('Dark Project KD87A', 9600, 5)


def test_str(kb):
    assert str(kb) == "Dark Project KD87A"
    assert str(kb.keylang) == "EN"


def test_change_lang(kb):
    kb.change_lang()
    assert str(kb.keylang) == "RU"
    kb.change_lang().change_lang()
    assert str(kb.keylang) == "RU"
