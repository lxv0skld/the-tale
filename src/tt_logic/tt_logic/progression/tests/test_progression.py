
import unittest

from .. import constants as c
from .. import formulas as f


class PrograssionTests(unittest.TestCase):

    # проверяем, что кусочная функция прогрессии хотя бы теоретически может иметь монотонную производную
    # это необходимо для гарантии того. что количество опыта для следующего уровня всегда будет больше, чем для предыдущего
    def test_progression_derivative_is_monotonous(self):
        deltas = []

        start = c.LEVEL_TIME_BASE_POINTS[0]

        for stop in c.LEVEL_TIME_BASE_POINTS[1:]:
            delta = (stop[1] - start[1]) / (stop[0] - start[0])
            deltas.append(delta)

            start = stop

        self.assertEqual(deltas, sorted(deltas))

    # проверяем, что функция монотонно возрастает
    def test_time_on_level_always_increasing(self):
        old_value = 0

        for level in range(1, c.HERO_FULL_ABILITIES_LEVEL * 2):
            new_value = f.time_on_level(level)

            self.assertLess(old_value, new_value)

            old_value = new_value

    def test_base_points(self):

        def time_before_level(level):
            return sum(f.time_on_level(i) for i in range(1, level))

        self.assertEqual(time_before_level(1), 0)

        # на первом уровне игрок проводит заданное количество времени
        self.assertEqual(time_before_level(2), c.TIME_ON_FIRST_LEVEL * c._hours)

        for level, time in c.LEVEL_TIME_BASE_POINTS:
            self.assertAlmostEqual(time_before_level(level), time)
