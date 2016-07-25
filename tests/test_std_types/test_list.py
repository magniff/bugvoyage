from hypothesis import strategies, given, settings


@given(
    inp_list=(
        strategies.lists(strategies.text()) |
        strategies.lists(strategies.integers()) |
        strategies.lists(strategies.floats()) |
        strategies.lists(strategies.booleans())
    )
)
@settings(max_examples=300000)
def test_sort_sorted(inp_list):
    copy_list = inp_list.copy()
    inp_list.sort()
    assert inp_list == list(sorted(copy_list))


@given(
    inp_list=(
        strategies.lists(strategies.text()) |
        strategies.lists(strategies.integers()) |
        strategies.lists(strategies.floats()) |
        strategies.lists(strategies.booleans())
    )
)
@settings(max_examples=300000)
def test_reverse_reversed(inp_list):
    copy_list = inp_list.copy()
    assert inp_list[::-1] == list(reversed(copy_list))
