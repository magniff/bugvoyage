import struct
import math
from hypothesis import strategies, given, settings, example, assume


@given(
    int_number=strategies.integers(min_value=0, max_value=4294967295)
)
@example(0)
@example(4294967295)
@settings(max_examples=20000)
def test_ints(int_number):
    assert struct.unpack("<I", struct.pack("<I", int_number))[0] == int_number
    assert struct.unpack(">I", struct.pack(">I", int_number))[0] == int_number
    assert struct.unpack("@I", struct.pack("@I", int_number))[0] == int_number
    assert struct.unpack("=I", struct.pack("=I", int_number))[0] == int_number
    assert struct.unpack("!I", struct.pack("!I", int_number))[0] == int_number


@given(
    number=strategies.integers(min_value=0, max_value=65535)
)
@example(0)
@example(65535)
@settings(max_examples=50000)
def test_unsigned_shorts(number):
    assert struct.unpack("<H", struct.pack("<H", number))[0] == number
    assert struct.unpack(">H", struct.pack(">H", number))[0] == number
    assert struct.unpack("@H", struct.pack("@H", number))[0] == number
    assert struct.unpack("=H", struct.pack("=H", number))[0] == number
    assert struct.unpack("!H", struct.pack("!H", number))[0] == number


@given(
    number=strategies.integers(min_value=-32768, max_value=32767)
)
@example(0)
@example(-32768)
@example(32767)
@settings(max_examples=50000)
def test_signed_shorts(number):
    assert struct.unpack("<h", struct.pack("<h", number))[0] == number
    assert struct.unpack(">h", struct.pack(">h", number))[0] == number
    assert struct.unpack("@h", struct.pack("@h", number))[0] == number
    assert struct.unpack("=h", struct.pack("=h", number))[0] == number
    assert struct.unpack("!h", struct.pack("!h", number))[0] == number


@given(
    number=strategies.integers(min_value=-2**63, max_value=-1 + 2**63)
)
@example(0)
@example(-2**63)
@example(-1 + 2**63)
@settings(max_examples=200000)
def test_long_long(number):
    assert struct.unpack("<q", struct.pack("<q", number))[0] == number
    assert struct.unpack(">q", struct.pack(">q", number))[0] == number
    assert struct.unpack("@q", struct.pack("@q", number))[0] == number
    assert struct.unpack("=q", struct.pack("=q", number))[0] == number
    assert struct.unpack("!q", struct.pack("!q", number))[0] == number


@given(
    number=strategies.floats()
)
@example(0.0)
@settings(max_examples=200000)
def test_floats(number):
    assume(not math.isinf(number) and not math.isnan(number))
    assert struct.unpack("<d", struct.pack("<d", number))[0] == number
    assert struct.unpack(">d", struct.pack(">d", number))[0] == number
    assert struct.unpack("@d", struct.pack("@d", number))[0] == number
    assert struct.unpack("=d", struct.pack("=d", number))[0] == number
    assert struct.unpack("!d", struct.pack("!d", number))[0] == number
