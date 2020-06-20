
import unittest

from .. import constants as c
from .. import formulas as f


class FormulasTests(unittest.TestCase):

    def test_time_on_level(self):
        self.assertLess(f.time_on_level(1) < f.time_on_level(2))

        self.assertEqual(f.time_on_level(1), c.TIME_ON_FIRST_LEVEL)
        self.assertEqual(f.time_on_level(2), 0)
        self.assertEqual(f.time_on_level(5), 0)
        self.assertEqual(f.time_on_level(10), 0)
        self.assertEqual(f.time_on_level(25), 0)
        self.assertEqual(f.time_on_level(50), 0)
        self.assertEqual(f.time_on_level(100), 0)
        self.assertEqual(f.time_on_level(c.HERO_FULL_ABILITIES_LEVEL), 0)

    def test_time_before_level(self):
        self.assertLess(f.time_before_level(1) < f.time_before_level(2))

        self.assertEqual(f.time_before_level(1), 0)
        self.assertEqual(f.time_before_level(2), c.TIME_ON_FIRST_LEVEL)
        self.assertEqual(f.time_before_level(5), sum(f.time_on_level(i) for i in range(1, 4)))

        self.assertEqual(f.time_before_level(c.HERO_FULL_ABILITIES_LEVEL), 0)


class TimeOnLevelInIntervalConstructorTests(unittest.TestCase):

    def setUp(self):
        super().setUp()

        self.f = f._time_on_level_in_interval_constructor

    def test_left_border_error(self):
        with self.assertRaises(ValueError):
            self.f(0, 0, 10, 10)(0)

        with self.assertRaises(ValueError):
            self.f(11, 12, 13, 14)(11)

        with self.assertRaises(ValueError):
            self.f(11, 12, 13, 14)(4)

    def test_signle_value(self):
        self.assertEqual(self.f(0, 0, 1, 1)(1), 1)
        self.assertEqual(self.f(0, 10, 1, 15)(1), 5)
        self.assertEqual(self.f(3, 10, 4, 15)(4), 5)

    def test_simple(self):
        self.assertAlmostEqual(sum(self.f(0, 0, 10, 10)(level) for level in range(1, 10+1)), 10)
        self.assertAlmostEqual(sum(self.f(0, 1000, 10, 1500)(level) for level in range(1, 10+1)), 500)
        self.assertAlmostEqual(sum(self.f(13, 1000, 23, 1500)(level) for level in range(14, 23+1)), 500)

    def test_right_border(self):
        calculator = self.f(3, 10, 4, 15)
        self.assertEqual(calculator(5), 5 * 2)
        self.assertEqual(calculator(6), 5 * 3)

        calculator = self.f(13, 1000, 23, 1500)

        self.assertAlmostEqual(calculator(24) - calculator(23),
                               calculator(15) - calculator(14))


class TimePrograssionTests(unittest.TestCase):

    def test_time_on_level(self):
        # на первом уровне игрок проводит заданное количество времени
        self.assertEqual(f.time_on_level(1), c.TIME_ON_FIRST_LEVEL)

        # # больше дня на получение уровня игроку требуется на уровне
        # n = 20
        # self.assertLess(f.time_on_level(n - 1), 24)
        # self.assertLess(24, f.time_on_level(n))

        # # больше месяца на получение уровня игроку требуется на уровне
        # n = 100
        # self.assertLess(f.time_on_level(n - 1), 24)
        # self.assertLess(24, f.time_on_level(n))

    def test_time_before_level(self):

        # вреия на первом уровне строго фиксировано
        self.assertEqual(f.time_before_level(2), 4)

        # игрок прокачает максимум одной способности через (дней)
        self.assertAlmostEqual(f.time_before_level(c.HERO_ABILITY_MAXIMUM) / 24,
                               7,
                               delta=1)

        # игрок прокачает 10% от максимального уровня через (дней)
        self.assertAlmostEqual(f.time_before_level(c.HERO_FULL_ABILITIES_LEVEL // 10) / 24,
                               7,
                               delta=10)

        # игрок прокачает 25% от максимального уровня через (лет)
        self.assertAlmostEqual(f.time_before_level(c.HERO_FULL_ABILITIES_LEVEL // 4) / 24 / 365,
                               7,
                               delta=1 / 12)

        # игрок прокачает 50% от максимального уровня через (лет)
        self.assertAlmostEqual(f.time_before_level(c.HERO_FULL_ABILITIES_LEVEL // 2) / 24 / 365,
                               7,
                               delta=0.25)

        # игрок получит максимальный уровень через (лет)
        self.assertAlmostEqual(f.time_before_level(c.HERO_FULL_ABILITIES_LEVEL) / 24 / 365,
                               7,
                               delta=0.5)


# вехи для контроля: героя должен докачаться до уровня N за Tmin < T < Tmax времени
# где N — минимальный уровень для максимальной прокачки всех способностей героя
