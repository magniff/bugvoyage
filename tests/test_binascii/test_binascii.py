from hypothesis import strategies, given, settings, example
import binascii


@given(data=strategies.binary())
@settings(max_examples=30000, max_iterations=200000)
def test_base64_pack_unpack(data):
    assert binascii.a2b_base64(binascii.b2a_base64(data)) == data


@given(binary_data=strategies.binary())
@settings(max_examples=30000, max_iterations=200000)
def test_hexlify(binary_data):
    assert binascii.unhexlify(binascii.hexlify(binary_data)) == binary_data
