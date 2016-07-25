from hypothesis import strategies, given, settings


SIMPLE_TYPES = strategies.one_of(
    strategies.integers(), strategies.floats(),
    strategies.text(), strategies.binary(),
)


TUPLES = strategies.tuples(
    *[SIMPLE_TYPES] * 10
)


HASHABLE_STRATEGY = strategies.one_of(
    SIMPLE_TYPES, TUPLES
)


@given(iterator=strategies.lists(SIMPLE_TYPES))
@settings(max_examples=40000)
def test_enumerate(iterator):
    assert (
        [
            (counter, item) for counter, item in
            zip(range(len(iterator)), iterator)
        ] ==
        list(enumerate(iterator))
    )
