
import unittest

from .. import constants as c


class ConstantsTest(unittest.TestCase):

    def test_constants_values(self):

        self.assertEqual(c.HERO_ABILITIES_NUMBER, 20)
        self.assertEqual(c.HERO_ABILITY_MAXIMUM, 10)
        self.assertEqual(c.HERO_FULL_ABILITIES_LEVEL, 200)

        self.assertEqual(c.TIME_ON_FIRST_LEVEL, 4)

        self.assertEqual(c.LEVEL_TIME_BASE_POINTS, [(1, 0 * c._hours),
                                                    (2, c.TIME_ON_FIRST_LEVEL * c._hours),
                                                    (10, 10 * c._days),
                                                    (20, 30 * c._days),
                                                    (50, 0.5 * c._years),
                                                    (100, 2 * c._years),
                                                    (200, 7 * c._years)])

        self.assertEqual(c.EXPERIENCE_PER_QUEST_FRACTION, 0.8)
        self.assertEqual(c.EXPERIENCE_PER_COMPANION_FRACTION, 0.1)
        self.assertAlmostEqual(c.EXPERIENCE_PER_RITAUL_FRACTION, 0.1)

        self.assertEqual(c.EXPERIENCE_PER_QUEST, 100)

        self.assertEqual(c.EXPERIENCE_ARTIFACT_SMALL_BONUS, 0.02)
        self.assertEqual(c.EXPERIENCE_ARTIFACT_NORMAL_BONUS, 0.1)
        self.assertEqual(c.EXPERIENCE_HERO_ABILITY_BONUS, 0.2)

        self.assertEqual(c.EXPERIENCE_PER_QUEST_MAX_MULTIPLIER, 1.3)

    def test_experience_fractions_consistency(self):
        self.assertAlmostEqual(c.EXPERIENCE_PER_QUEST_FRACTION +
                               c.EXPERIENCE_PER_COMPANION_FRACTION +
                               c.EXPERIENCE_PER_RITAUL_FRACTION, 1)
