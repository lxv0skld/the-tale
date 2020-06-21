
# расчёт скорсоти прогрессии происходит по следующим принципам:
#
# скорость прогрессии определяется через скорость получения уровней в единицу времени
# так как это определяет пльзовательский опыт
#
# прогрессия подгоняется так, чтобы:
# - скорость получения 1-ого уровня была фиксированной константой
# - график получения уровней проходил через фиксированные точки
#
# прогнозы проверяются в тестах, там же смотри пояснение
#
# для нужд баланса внутри игры скорость переводится в «уровней / квест»
# так как выполнение задания является единицей глобальной активности героя в игре
#
# исходя из скорости в заданиях, определяется опыт за одно задание

HERO_ABILITIES_NUMBER: int = 20
HERO_ABILITY_MAXIMUM: int = 10

HERO_FULL_ABILITIES_LEVEL: int = HERO_ABILITIES_NUMBER * HERO_ABILITY_MAXIMUM

TIME_ON_FIRST_LEVEL: float = 4  # часов


# размерности, для перевода значений в дни
_hours: float = 1 / 24
_days: float = 1
_years: float = 365

# количество времени на каждый уровень считаем по кусочно-заданной функции (это проще, чем подбирать удобную формулу)
# на каждом интервале время на каждый следующий уровень должно возрастать (то есть на интервале функция должна быть нелинейной)
# после максимального интервала прогрессия продолжается по правилам последнего интервала
# формат точки: <уровень, через какое суммарное время должен достигаться>
LEVEL_TIME_BASE_POINTS = [(1, 0 * _hours),
                          (2, TIME_ON_FIRST_LEVEL * _hours),
                          (HERO_ABILITY_MAXIMUM, 10 * _days),
                          (int(0.1 * HERO_FULL_ABILITIES_LEVEL), 30 * _days),
                          (int(0.25 * HERO_FULL_ABILITIES_LEVEL), 0.5 * _years),
                          (int(0.5 * HERO_FULL_ABILITIES_LEVEL), 2 * _years),
                          (HERO_FULL_ABILITIES_LEVEL, 7 * _years)]

# весь опыт приходит из нескольких источников:
# - задания
# - ритуалы в честь хранителя

EXPERIENCE_PER_QUEST_FRACTION: float = 0.85
EXPERIENCE_PER_COMPANION_SAY_WISDOM_FRACTION: float = 0.05
EXPERIENCE_PER_RITAUL_FRACTION: float = 0.1

# опыт за задание оцениваем исходя из
# - эвристической оценёнки количества выполняемых заданий в единицу времени (см. оценку и границы в model.tests.test_formulas)
# - желаемой формы роста награды за задание (см. tests.test_formulas)
EXPERIENCE_PER_QUEST: int = 100

# модификаторы опыта
EXPERIENCE_ARTIFACT_SMALL_BONUS: float = 0.02
EXPERIENCE_ARTIFACT_NORMAL_BONUS: float = 0.1
EXPERIENCE_HERO_ABILITY_BONUS: float = 0.2

EXPERIENCE_PER_QUEST_MAX_MULTIPLIER: float = (1 +
                                              EXPERIENCE_ARTIFACT_NORMAL_BONUS +
                                              EXPERIENCE_HERO_ABILITY_BONUS)



# # опыт за убийство моба (особенность черт)
# EXP_FOR_KILL: int = 10  # средний опыт за убийство монстра
# EXP_FOR_KILL_DELTA: float = 0.3  # разброс опыта за убийство

# _KILLS_IN_HOUR: float = TURNS_IN_HOUR / ACTIONS_CYCLE_LENGTH * BATTLES_BEFORE_HEAL

# # вероятность получить опыт за убийство моба
# EXP_FOR_KILL_PROBABILITY: float = (0.1 * EXP_PER_HOUR) / (EXP_FOR_KILL * _KILLS_IN_HOUR)

# # опыт за события от черт
# HABIT_EVENT_EXPERIENCE: int = int(0.05 * (24.0 * EXP_PER_HOUR) / (HABIT_EVENTS_IN_DAY * HABIT_EVENT_EXPERIENCE_PRIORITY / _HABIT_EVENT_TOTAL_PRIORITY))
# HABIT_EVENT_EXPERIENCE_DELTA: float = 0.5  # разброс опытаHABIT_EVENT_EXPERIENCE: int = int(0.05 * (24.0 * EXP_PER_HOUR) / (HABIT_EVENTS_IN_DAY * HABIT_EVENT_EXPERIENCE_PRIORITY / _HABIT_EVENT_TOTAL_PRIORITY))
# HABIT_EVENT_EXPERIENCE_DELTA: float = 0.5  # разброс опыта


# ACTION_RELIGION_EXPERIENCE: int = 1  # сколько опыта за раз даём


# с учётом возможных способностей (т.е. считаем, что при нужных абилках у премиума скорость получения опыта будет 1.0)
# EXP_FOR_PREMIUM_ACCOUNT: float = 1.0  # модификатор опыта для премиум аккаунтов
# EXP_FOR_NORMAL_ACCOUNT: float = 0.66  # модификатор опыта для обычных акканутов


# BASE_EXPERIENCE_FOR_MONEY_SPEND: int = int(24 * EXP_PER_HOUR * 0.4)
# EXPERIENCE_DELTA_FOR_MONEY_SPEND: float = 0.5
