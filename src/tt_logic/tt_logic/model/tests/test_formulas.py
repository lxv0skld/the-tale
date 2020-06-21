import unittest

from .. import constants as c
from .. import formulas as f


class IDLEOnLevelTest(unittest.TestCase):

    def test(self):
        self.assertEqual(f.idle_on_level(1), c.ACTION_IDLE_MINIMUM_TURNS)
        self.assertEqual(f.idle_on_level(2), c.ACTION_IDLE_MINIMUM_TURNS + c.ACTION_IDLE_TURNS_TO_LEVEL)
        self.assertEqual(f.idle_on_level(100), c.ACTION_IDLE_MINIMUM_TURNS + 99 * c.ACTION_IDLE_TURNS_TO_LEVEL)

        self.assertEqual(f.idle_on_level(1000), 6084)
