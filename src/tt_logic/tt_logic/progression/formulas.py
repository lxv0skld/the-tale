
from . import constants as c


def _time_on_level_in_interval_constructor(start_level: int, start_time: float,
                                           stop_level: int, stop_time: float) -> float:

    time_delta = stop_time - start_time
    levels_delta = stop_level - start_level

    k = 2 * time_delta / (levels_delta * (levels_delta + 1))

    def f(level: int):
        if level <= start_level:
            raise ValueError(f'can not calculate time for level {level} in interval ({start_level}, {stop_level}]')

        return k * (level - start_level)

    return f


def _time_on_level_calculators():
    start = c.LEVEL_TIME_BASE_POINTS[0]

    calculators = []

    for stop in c.LEVEL_TIME_BASE_POINTS[1:]:
        calculator = _time_on_level_in_interval_constructor(*start, *stop)

        calculators.append((start[0], calculator))

    calculators.reverse()

    return calculators


_TIME_ON_LEVEL = _time_on_level_calculators()


def time_on_level(level: int) -> float:

    for test_level, calculator in _TIME_ON_LEVEL:
        if test_level <= level:
            return calculator(level)

    raise NotImplementedError()


def time_before_level(level: int) -> float:
    return sum(time_on_level(i) for i in range(1, level))


# def exp_on_lvl(lvl: int) -> int:
#     return int(c.EXP_PER_HOUR * time_on_lvl(lvl))  # опыт, который игрок должен заработать на одном уровне


# def turns_on_lvl(lvl: int) -> int:
#     return int(hours_to_turns(time_on_lvl(lvl)))  # количество ходов, которое герой проведёт на уровне


# def total_time_for_lvl(lvl: int) -> float:
#     return sum(time_on_lvl(x) for x in range(1, lvl))  # общее время, затрачиваемое героем на достижение уровня (с 1-ого)


# def total_exp_to_lvl(lvl: int) -> int:
#     return sum(exp_on_lvl(x) for x in range(1, lvl + 1))  # общий опыт, получаемые героем для стижения уровня (с 1-ого)


# def lvl_after_time(time: float) -> int:
#     total_exp = c.EXP_PER_HOUR * time
#     level = 1
#     while total_exp > exp_on_lvl(level):
#         total_exp -= exp_on_lvl(level)
#         level += 1
#     return level


# def experience_for_quest__real(max_path_length: float) -> float:
#     MAGIC_QUEST_MULTIPLIER = 0.7
#     return path_to_turns(max_path_length) / c.TURNS_IN_HOUR * c.EXP_PER_HOUR * MAGIC_QUEST_MULTIPLIER


# def experience_for_quest(max_path_length: float) -> float:
#     return int(math.ceil(experience_for_quest__real(max_path_length) * random.uniform(1.0 - c.EXP_PER_QUEST_FRACTION,
#                                                                                       1.0 + c.EXP_PER_QUEST_FRACTION)))
