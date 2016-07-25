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


@given(
    list_of_stuff=strategies.lists(
        HASHABLE_STRATEGY,
        min_size=0,
        max_size=30,
    )
)
@settings(max_examples=10000)
def test_set_contains_every_item_from_original_list(list_of_stuff):
    the_set = set(list_of_stuff)
    assert all(item in the_set for item in list_of_stuff)


@given(
    set_of_stuff=strategies.sets(
        HASHABLE_STRATEGY,
        min_size=0,
        max_size=100,
    )
)
@settings(max_examples=10000)
def test_set_intersection_with_self(set_of_stuff):
    set_copy = set_of_stuff.copy()
    assert set_of_stuff.intersection(set_of_stuff) == set_copy


@given(
    set_of_stuff=strategies.sets(
        HASHABLE_STRATEGY,
        min_size=0,
        max_size=100,
    )
)
@settings(max_examples=10000)
def test_set_intersection_update_self(set_of_stuff):
    set_copy = set_of_stuff.copy()
    set_of_stuff.intersection_update(set_of_stuff)
    assert set_of_stuff == set_copy


@given(
    set_of_stuff_a=strategies.sets(
        HASHABLE_STRATEGY,
        min_size=0,
        max_size=30,
    ),
    set_of_stuff_b=strategies.sets(
        HASHABLE_STRATEGY,
        min_size=0,
        max_size=30,
    )
)
@settings(max_examples=5000)
def test_simmetric_diff_union(set_of_stuff_a, set_of_stuff_b):
    assert (
        set_of_stuff_a.symmetric_difference(set_of_stuff_b).union(set_of_stuff_a) ==
        set_of_stuff_a.union(set_of_stuff_b)
    )
