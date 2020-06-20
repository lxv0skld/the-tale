
import unittest

from .. import constants as c


class ConstantsTest(unittest.TestCase):

    def test_constants_values(self):

        self.assertEqual(c.HERO_ABILITIES_NUMBER, 20)
        self.assertEqual(c.HERO_ABILITY_MAXIMUM, 10)
        self.assertEqual(c.HERO_FULL_ABILITIES_LEVEL, 200)
        self.assertEqual(c.QUESTS_ON_LEVEL_BASE, 1.05)
