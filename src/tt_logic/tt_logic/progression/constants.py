
# расчёт скорсоти прогрессии происходит по следующим принципам:
#
# скорость прогрессии определяется через скорость получения уровней в единицу времени
# так как это определяет пльзовательский опыт
#
# прогрессия экспоненциальная, подгоняется так, чтобы:
# - скорость получения 1-ого уровня была фиксированной константой
# - график получения уровней лежал между оптимистичным и пессимистичным прогнозами по временим выполнения заданий
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




# TIME_TO_LVL_DELTA: float = 7  # часов, разница во времени получения двух соседних уровней
# TIME_TO_LVL_MULTIPLIER: float = 1.02  # множитель опыта, возводится в степень уровня

# # магическое число — ожидаемое количество выполненных героем квестов в день
# EXPECTED_QUESTS_IN_DAY: float = 2.0

# EXP_PER_HOUR: int = 10  # опыт в час
# EXP_PER_QUEST_FRACTION: float = 0.33  # разброс опыта за задание

# с учётом возможных способностей (т.е. считаем, что при нужных абилках у премиума скорость получения опыта будет 1.0)
# EXP_FOR_PREMIUM_ACCOUNT: float = 1.0  # модификатор опыта для премиум аккаунтов
# EXP_FOR_NORMAL_ACCOUNT: float = 0.66  # модификатор опыта для обычных акканутов

# TURNS_TO_IDLE: int = 6  # количество ходов на уровень, которое герой бездельничает в соответствующей action

# BASE_EXPERIENCE_FOR_MONEY_SPEND: int = int(24 * EXP_PER_HOUR * 0.4)
# EXPERIENCE_DELTA_FOR_MONEY_SPEND: float = 0.5

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
