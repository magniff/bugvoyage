import lzma
from hypothesis import strategies, given, settings, example


@given(
    inp_data=strategies.binary()
)
@example(b"")
@settings(max_examples=10000000)
def test_compress_decompress(inp_data):
    assert lzma.decompress(lzma.compress(inp_data)) == inp_data
