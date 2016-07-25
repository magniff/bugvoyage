import math
from hypothesis import strategies, given, settings
import pickle


@given(
    data=strategies.lists(
        strategies.binary() |
        strategies.integers() |
        strategies.floats().filter(math.isfinite) |
        strategies.text()
    )
)
@settings(max_examples=300000)
def test_pickle_unpickle(data):
    assert pickle.loads(pickle.dumps(data)) == data
