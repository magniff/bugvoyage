from hypothesis import strategies, given, settings, assume


NONDIGIT_TEXT = (
    strategies.text(max_size=100).
    filter(len).
    map(lambda string: "".join(filter(str.isalpha, string)))
)


NONDIGIT_TEXT_LOWER = NONDIGIT_TEXT.map(str.lower)


@given(
    text=strategies.text(),
)
@settings(max_examples=300000)
def test_encode_decode(text):
    assert text.encode().decode() == text


@given(
    text0=strategies.text(),
    text1=strategies.text(),
    text2=strategies.text()
)
@settings(max_examples=300000)
def test_in(text0, text1, text2):
    big_text = text0+text1+text2
    assert text0 in big_text
    assert text1 in big_text
    assert text2 in big_text


@given(
    text0=strategies.text(),
    text1=strategies.text(),
    text2=strategies.text()
)
@settings(max_examples=300000)
def test_find(text0, text1, text2):
    big_text = text0+text1+text2
    assert big_text.find(text0) != -1
    assert big_text.find(text1) != -1
    assert big_text.find(text2) != -1
