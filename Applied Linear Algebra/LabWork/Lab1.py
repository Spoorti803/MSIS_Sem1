class vector:
    def __init__(self, vals: list):
        if isinstance(vals, list):
            self.vals = vals
        else:
            self.vals = list(vals)


def test_non_empty_vector_contents():
    v = vector([1, 2, 3])
    assert v.vals == [1, 2, 3]

def test_empty_vectors():
    v = vector([])
    assert len(v.vals) ==0

def test_vector_ctor():
    v = vector([1, 2, 3])
    assert v.vals == []