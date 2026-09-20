import math
import random
import unittest
#import the vec class from the file vectors.py
from vectors import Vec  


class TestMean(unittest.TestCase):
    def test_known_value(self):
        self.assertAlmostEqual(Vec([1, 2, 3, 4]).mean(), 2.5)

    def test_single_element(self):
        self.assertAlmostEqual(Vec([7]).mean(), 7)

    def test_negative_and_float_entries(self):
        self.assertAlmostEqual(Vec([-1.5, 1.5, 3.0]).mean(), 1.0)

    def test_empty_raises(self):
        with self.assertRaises(ValueError):
            Vec([]).mean()

    def test_mean_is_between_min_and_max(self):
        v = Vec([3, -2, 8, 0.5])
        self.assertGreaterEqual(v.mean(), min(v.elements))
        self.assertLessEqual(v.mean(), max(v.elements))

    def test_mean_of_constant_vector_is_the_constant(self):
        self.assertAlmostEqual(Vec([4.2] * 6).mean(), 4.2)

    def test_scaling_property(self):
        # mean(c * v) == c * mean(v)
        v, c = Vec([1, 2, 3, 10]), 2.5
        self.assertAlmostEqual((c * v).mean(), c * v.mean(), places=4)

    def test_shift_property(self):
        # mean(v + c) == mean(v) + c
        v, c = Vec([1, 2, 3, 10]), 5
        shifted = v + Vec([c] * len(v))
        self.assertAlmostEqual(shifted.mean(), v.mean() + c, places=4)

    def test_additivity(self):
        # mean(u + v) == mean(u) + mean(v)
        u, v = Vec([1, 2, 3]), Vec([4, -5, 6])
        self.assertAlmostEqual((u + v).mean(), u.mean() + v.mean(), places=4)


class TestDemean(unittest.TestCase):
    def test_known_value(self):
        d = Vec([1, 2, 3]).demean()
        for a, b in zip(d.elements, [-1, 0, 1]):
            self.assertAlmostEqual(a, b)

    def test_returns_new_vector_and_leaves_original_unchanged(self):
        v = Vec([1, 2, 3])
        d = v.demean()
        self.assertIsNot(d, v)
        self.assertEqual(v.elements, [1, 2, 3])

    def test_same_length(self):
        v = Vec([5, 1, 9, 2, 2])
        self.assertEqual(len(v.demean()), len(v))

    def test_demeaned_vector_has_zero_mean(self):
        v = Vec([3.5, -2, 8, 0.25, 11])
        self.assertAlmostEqual(v.demean().mean(), 0.0)

    def test_zero_mean_on_random_vectors(self):
        rng = random.Random(0)
        for _ in range(20):
            v = Vec([rng.uniform(-100, 100) for _ in range(rng.randint(1, 50))])
            self.assertAlmostEqual(v.demean().mean(), 0.0)

    def test_idempotent(self):
        # demeaning an already de-meaned vector changes nothing
        d1 = Vec([4, 8, 15, 16, 23, 42]).demean()
        d2 = d1.demean()
        for a, b in zip(d1.elements, d2.elements):
            self.assertAlmostEqual(a, b)

    def test_constant_vector_becomes_zeros(self):
        d = Vec([3, 3, 3]).demean()
        for x in d.elements:
            self.assertAlmostEqual(x, 0.0)

    def test_shift_invariance(self):
        # demean(v + c) == demean(v)
        v = Vec([1, 4, 9, 16])
        shifted = v + Vec([100] * 4)
        for a, b in zip(v.demean().elements, shifted.demean().elements):
            self.assertAlmostEqual(a, b, places=4)

    def test_scaling_property(self):
        # demean(c * v) == c * demean(v)
        v, c = Vec([1, 4, 9, 16]), 3
        left = (c * v).demean().elements
        right = (c * v.demean()).elements
        for a, b in zip(left, right):
            self.assertAlmostEqual(a, b, places=4)

    def test_empty_raises(self):
        with self.assertRaises(ValueError):
            Vec([]).demean()


class TestStd(unittest.TestCase):
    def test_known_value(self):
        # classic example: population std is exactly 2
        self.assertAlmostEqual(Vec([2, 4, 4, 4, 5, 5, 7, 9]).std(), 2.0)

    def test_matches_definition(self):
        v = Vec([1, 2, 3, 4])
        m = sum(v.elements) / len(v)
        expected = math.sqrt(sum((x - m) ** 2 for x in v.elements) / len(v))
        self.assertAlmostEqual(v.std(), expected)

    def test_constant_vector_has_zero_std(self):
        self.assertAlmostEqual(Vec([5, 5, 5, 5]).std(), 0.0)

    def test_single_element_has_zero_std(self):
        self.assertAlmostEqual(Vec([42]).std(), 0.0)

    def test_non_negative(self):
        rng = random.Random(1)
        for _ in range(20):
            v = Vec([rng.uniform(-50, 50) for _ in range(10)])
            self.assertGreaterEqual(v.std(), 0.0)

    def test_shift_invariance(self):
        # std(v + c) == std(v)
        v = Vec([1, 4, 9, 16])
        shifted = v + Vec([1000] * 4)
        self.assertAlmostEqual(v.std(), shifted.std(), places=4)

    def test_scaling_property(self):
        # std(c * v) == |c| * std(v)
        v = Vec([1, 4, 9, 16])
        self.assertAlmostEqual((3 * v).std(), 3 * v.std(), places=4)
        self.assertAlmostEqual((-3 * v).std(), 3 * v.std(), places=4)

    def test_std_of_demeaned_equals_std(self):
        v = Vec([2, 7, 1, 8, 2, 8])
        self.assertAlmostEqual(v.demean().std(), v.std())

    def test_std_equals_rms_of_demeaned_vector(self):
        # std(v) = sqrt(mean of squares of demean(v))
        v = Vec([2, 7, 1, 8, 2, 8])
        d = v.demean()
        rms = math.sqrt(sum(x * x for x in d.elements) / len(d))
        self.assertAlmostEqual(v.std(), rms)

    def test_empty_raises(self):
        with self.assertRaises(ValueError):
            Vec([]).std()


if __name__ == "__main__":
    unittest.main()