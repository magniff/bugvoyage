import math
from hypothesis import strategies, given, settings, assume


NONDIGIT_TEXT = (
    strategies.text(max_size=100).
    filter(len).
    map(lambda string: "".join(filter(str.isalpha, string)))
)


NONDIGIT_TEXT_LOWER = NONDIGIT_TEXT.map(str.lower)


@given(
    float_num=strategies.integers().map(float),
)
@settings(max_examples=100000)
def test_is_integer(float_num):
    assert float.is_integer(float_num)


@given(
    float_num=strategies.integers().map(float),
)
@settings(max_examples=5000000)
def test_as_rational_num(float_num):
    a, b = float.as_integer_ratio(float_num)
    assert a/b == float_num


@given(
    float_num=strategies.floats()
)
@settings(max_examples=200000)
def test_hex_from_hex(float_num):
    assume(not math.isnan(float_num) and not math.isinf(float_num))
    assert float.fromhex(float_num.hex()) == float_num



# upper.lower test doesnt hold