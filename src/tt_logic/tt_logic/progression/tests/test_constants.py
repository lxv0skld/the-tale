
import unittest

from .. import constants as c


class ConstantsTest(unittest.TestCase):

    def test_constants_values(self):

        self.assertEqual(c.HERO_ABILITIES_NUMBER, 20)
        self.assertEqual(c.HERO_ABILITY_MAXIMUM, 10)
        self.assertEqual(c.HERO_FULL_ABILITIES_LEVEL, 200)

        self.assertEqual(c.TIME_ON_FIRST_LEVEL, 4)

        self.assertEqual(c.LEVEL_TIME_BASE_POINTS, [(1, 0 * c._hours),
                                                    (2, TIME_ON_FIRST_LEVEL * c._hours),
                                                    (10, 10 * c._days),
                                                    (20, 30 * c._days),
                                                    (50, 0.5 * _c.years),
                                                    (100, 2 * c._years),
                                                    (200, 7 * c._years)])
