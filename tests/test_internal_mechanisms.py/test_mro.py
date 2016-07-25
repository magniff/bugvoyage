from hypothesis import strategies, given, settings



def merge(seqs):
    res = []; i=0
    while 1:
      nonemptyseqs=[seq for seq in seqs if seq]
      if not nonemptyseqs: return res
      i+=1; 
      for seq in nonemptyseqs: # find merge candidates among seq heads
          cand = seq[0]; 
          nothead=[s for s in nonemptyseqs if cand in s[1:]]
          if nothead: cand=None #reject candidate
          else: break
      if not cand: raise "Inconsistent hierarchy"
      res.append(cand)
      for seq in nonemptyseqs: # remove cand
          if seq[0] == cand: del seq[0]


def mro(C):
    "Compute the class precedence list (mro) according to C3"
    return merge([[C]]+list(map(mro,C.__bases__))+[list(C.__bases__)])


# @given(
#     list_of_stuff=strategies.lists(
#         HASHABLE_STRATEGY,
#         min_size=0,
#         max_size=30,
#     )
# )
# @settings(max_examples=10000)
# def test_set_contains_every_item_from_original_list(list_of_stuff):
#     the_set = set(list_of_stuff)
#     assert all(item in the_set for item in list_of_stuff)
