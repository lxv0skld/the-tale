
import unittest

from .. import constants as c


class ConstantsTest(unittest.TestCase):

    def test_constants_values(self):

        self.assertEqual(c.TURN_DELTA, 10)
        self.assertEqual(c.TURNS_IN_HOUR, 360)

        self.assertEqual(c.BATTLE_LENGTH, 16)
        self.assertEqual(c.INTERVAL_BETWEEN_BATTLES, 3)

        self.assertEqual(c.BATTLES_BEFORE_HEAL, 8)

        self.assertEqual(c.MOVE_TURNS_IN_ACTION_CYCLE, 24)

        self.assertEqual(c.HEAL_TIME_FRACTION, 0.2)
        self.assertEqual(c.HEAL_STEP_FRACTION, 0.2)

        self.assertEqual(c.BATTLES_LINE_LENGTH, 149)

        self.assertEqual(c.BATTLES_PER_TURN, 0.25)

        self.assertEqual(c.HEAL_LENGTH, 29)

        self.assertEqual(c.ACTIONS_CYCLE_LENGTH, 178)

        self.assertAlmostEqual(c.CYCLES_IN_HOUR, 2.0224719101123596)

        self.assertAlmostEqual(c.MOVE_TURNS_IN_HOUR, 48.53932584269663)

        self.assertAlmostEqual(c.BATTLES_PER_HOUR, 16.179775280898877)

        self.assertAlmostEqual(c.ACTION_IDLE_MINIMUM_TURNS, 90)
        self.assertAlmostEqual(c.ACTION_IDLE_TURNS_TO_LEVEL, 6)

        self.assertAlmostEqual(c.HERO_SPEED_BASE, 0.1)

        self.assertAlmostEqual(c.HERO_SPEED_ARTIFACT_SMALL_BONUS, 0.02)
        self.assertAlmostEqual(c.HERO_SPEED_ARTIFACT_NORMAL_BONUS, 0.1)

        self.assertAlmostEqual(c.HERO_SPEED_COMPANION_SMALL_BONUS, 0.1)
        self.assertAlmostEqual(c.HERO_SPEED_COMPANION_NORMAL_BONUS, 0.15)
        self.assertAlmostEqual(c.HERO_SPEED_COMPANION_LARGE_BONUS, 0.2)

        self.assertAlmostEqual(c.HERO_SPEED_ABILITY_BONUS, 0.15)

        self.assertAlmostEqual(c.HERO_SPEED_MAX, 0.145)

        self.assertAlmostEqual(c.QUEST_TURNS, 145)

        self.assertAlmostEqual(c.QUESTS_IN_DAY, 15.666666666666668)

    def test_hero_speed_max(self):
        self.assertAlmostEqual(c.HERO_SPEED_MAX,
                               c.HERO_SPEED_BASE * (1 +
                                                    c.HERO_SPEED_ARTIFACT_NORMAL_BONUS +
                                                    c.HERO_SPEED_COMPANION_LARGE_BONUS +
                                                    c.HERO_SPEED_ABILITY_BONUS))
