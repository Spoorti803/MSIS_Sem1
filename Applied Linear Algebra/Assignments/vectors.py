import math
import sys
from typing import Self


"""
A custom vector class implementation for educational purposes.
"""

class Vec:
    def __init__(self, src=None) -> Self:
        if src is None:
            self.elements = []
        else:
            elements = list(src)
            for x in elements:
                if not isinstance(x, (int, float)):
                    raise TypeError(f"Scalar must be a number: {type(x)}")
            self.elements = elements

    def __add__(self, t: Self) -> Self:
        if not isinstance(t, Vec):
            raise TypeError(f"Expected Vec: {type(t)}")
        if len(self.elements) != len(t):
            raise TypeError(f"Type error - vectors must be of same dimensions")

        return Vec([round(x + y, 5) for x, y in zip(self.elements, t.elements)])


    def __rmul__(self, scalar: int | float) -> Self:
        if not isinstance(scalar, (int, float)):
            raise TypeError(f"Vector multiplication with invalid type: {type(scalar)}")
        #
        return Vec([round(x * scalar, 5) for x in self.elements])

    def __imul__(self, scalar: int | float) -> Self:
        if not isinstance(scalar, (int, float)):
            raise TypeError(f"Vector multiplication with invalid type: {type(scalar)}")

        for i, val in enumerate(self.elements):
            self.elements[i] = round(val * scalar, 5)
        #
        return self

    def __repr__(self) -> str:
        return repr(self.elements)

    def __len__(self) -> int:
        return len(self.elements)

    def __sub__(self, t: Self) -> Self:
        raise RuntimeError("vec subtraction unimplemented")

    def __neg__(self) -> Self:
        raise RuntimeError("vec negation unimplemented")

    def __radd__(self, other):
        raise RuntimeError("vec _radd_ unimplemented")

    def __iadd__(self, other):
        raise RuntimeError("vec _iadd_ unimplemented")

    # return a vector of @n zeroes. precondition: @n > 0
    @staticmethod
    def zeros(n: int) -> Self:
        raise RuntimeError("zeros unimpleented")

    # return a vector of @n. precondition: @n > 0
    @staticmethod
    def ones(n: int) -> Self:
        raise RuntimeError("ones unimpleented")

    # return a vector of @n uniformly distributed numbers in [0, 1]. precondition: @n > 0
    @staticmethod
    def uniform(n: int) -> Self:
        raise RuntimeError("random unimpleented")

    # Calculates the Euclidean norm (L2 norm) of the vector.
    # sqrt(e[0]^2 + e[1]^2 + e[2]^2 + ... + e[n-1]^2)
    def norm(self) -> float:
        raise RuntimeError("norm unimpleented")

    # Returns the mean of the entries: (sum of entries) / (number of entries).
    # Raises ValueError for an empty vector, since the mean is undefined.
    def mean(self) -> float:
        n = len(self.elements)
        if n == 0:
            raise ValueError("mean of an empty vector is undefined")
        return sum(self.elements) / n

    # Returns a NEW vector where the mean of self has been subtracted from
    # every entry. The original vector is left unchanged.
    def demean(self) -> Self:
        m = self.mean()
        return Vec([x - m for x in self.elements])

    # Returns the (population) standard deviation: the square root of the
    # average of the squared deviations from the mean. Uses demean().
    def std(self) -> float:
        d = self.demean()
        return math.sqrt(sum(x * x for x in d.elements) / len(d))


if sys.version_info < (3, 8):
    sys.exit("Error: This script requires Python 3.8 or higher.")

if __name__ == "__main__":
    #z1 = Vec.zeros(10)
    v1 = Vec([0, 1, 1.03])
    print(v1)
    v3 = 2.2 * v1
    v3 *= 5
    # v3 = 1 + v3
    print(v3)
    v2 = v1 + v3
    print(v1 + v3)
    #print(-(v1 + v3))