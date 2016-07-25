import sys
from hypothesis import strategies, given, settings, assume


if sys.version_info.major == 3 and sys.version_info.minor >= 5:
    @given(
        binary_data=strategies.binary().map(bytearray),
    )
    @settings(max_examples=100000)
    def test_is_integer(binary_data):
        assert bytearray.fromhex(bytearray.hex(binary_data)) == binary_data
