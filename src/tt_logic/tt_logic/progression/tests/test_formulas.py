
import unittest

from .. import constants as c
from .. import formulas as f


class FormulasTests(unittest.TestCase):

    def test_time_on_level(self):
        self.assertLess(f.time_on_level(1), f.time_on_level(2))

        self.assertEqual(f.time_on_level(1), c.TIME_ON_FIRST_LEVEL * c._hours)
        self.assertEqual(f.time_on_level(2), 0.990162037037037)
        self.assertEqual(f.time_on_level(5), 1.1950231481481481)
        self.assertEqual(f.time_on_level(10), 1.5909090909090908)
        self.assertEqual(f.time_on_level(25), 4.304435483870968)
        self.assertEqual(f.time_on_level(50), 8.31985294117647)
        self.assertEqual(f.time_on_level(100), 13.777846534653465)
        self.assertEqual(f.time_on_level(c.HERO_FULL_ABILITIES_LEVEL), 22.8125)


class TimeOnLevelInIntervalConstructorTests(unittest.TestCase):

    def setUp(self):
        super().setUp()

        self.f = f._time_on_level_in_interval_constructor

    def test_left_border_error(self):
        with self.assertRaises(ValueError):
            self.f(0, 0, 10, 10)(-1)

        with self.assertRaises(ValueError):
            self.f(11, 12, 13, 14)(10)

    def test_signle_value(self):
        self.assertEqual(self.f(0, 0, 1, 1)(0), 1)
        self.assertEqual(self.f(0, 10, 1, 15)(0), 5)
        self.assertEqual(self.f(3, 10, 4, 15)(3), 5)

    def test_simple(self):
        self.assertAlmostEqual(sum(self.f(0, 0, 10, 10)(level) for level in range(0, 10)), 10)
        self.assertAlmostEqual(sum(self.f(0, 1000, 10, 1500)(level) for level in range(0, 10)), 500)
        self.assertAlmostEqual(sum(self.f(13, 1000, 23, 1500)(level) for level in range(13, 23)), 500)

    def test_right_border(self):
        calculator = self.f(3, 10, 4, 15)

        calculator = self.f(13, 1000, 23, 1500)

        self.assertAlmostEqual(calculator(24) - calculator(23),
                               calculator(15) - calculator(14))

        self.assertAlmostEqual(calculator(101) - calculator(100),
                               calculator(15) - calculator(14))


class TimeOnLevelTests(unittest.TestCase):

    def test_wrong_level(self):
        with self.assertRaises(ValueError):
            f.time_on_level(0)

        with self.assertRaises(ValueError):
            f.time_on_level(-1)
