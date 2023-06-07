from src.keyboard import KeyBoard

if __name__ == '__main__':
    kb = KeyBoard('Dark Project KD87A', 9600, 5)
    assert str(kb) == "Dark Project KD87A"

    assert str(kb.KeyLang) == "EN"

    kb.change_lang()
    assert str(kb.KeyLang) == "RU"

    # Сделали RU -> EN -> RU
    kb.change_lang().change_lang()
    assert str(kb.KeyLang) == "RU"

    kb.KeyLang = 'CH'
    # AttributeError: property 'language' of 'KeyBoard' object has no setter
