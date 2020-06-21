
import math

from tt_logic.model import constants as mc


TURN_DELTA: int = 10  # в секундах - задержка одного хода

TURNS_IN_HOUR: float = 60 * 60 / TURN_DELTA  # количество ходов в 1 часе


########################
# цикл путешествия героя
########################

# цикл начинается с полного здоровья, состоит из цепочки боёв и перемещений, пока есть здоровье
# когда здоровье подходит к нулю, герой лечится

BATTLE_LENGTH: int = 16  # ходов, средняя длительность одного боя (количество действий в бой)
INTERVAL_BETWEEN_BATTLES: int = 3  # ходов, время, между двумя битвами

BATTLES_BEFORE_HEAL: int = 8  # количество боёв в цикле

MOVE_TURNS_IN_ACTION_CYCLE: int = INTERVAL_BETWEEN_BATTLES * BATTLES_BEFORE_HEAL

HEAL_TIME_FRACTION: float = 0.2  # доля времени от цепочки битв, которую занимает полный отхил героя
HEAL_STEP_FRACTION: float = 0.2  # разброс регенерации за один ход

# длинна цепочки боёв до остановки на лечение в ходах
BATTLES_LINE_LENGTH: int = BATTLES_BEFORE_HEAL * (BATTLE_LENGTH + INTERVAL_BETWEEN_BATTLES) - INTERVAL_BETWEEN_BATTLES

# вероятность начать битву в ход
BATTLES_PER_TURN: float = 1.0 / (INTERVAL_BETWEEN_BATTLES + 1)

HEAL_LENGTH: int = int(math.floor(BATTLES_LINE_LENGTH * HEAL_TIME_FRACTION))  # ходов, длительность лечения героя

ACTIONS_CYCLE_LENGTH: int = BATTLES_LINE_LENGTH + HEAL_LENGTH  # ходов, длинна цикла

CYCLES_IN_HOUR: float = mc.TURNS_IN_HOUR / ACTIONS_CYCLE_LENGTH

MOVE_TURNS_IN_HOUR: float = MOVE_TURNS_IN_ACTION_CYCLE * CYCLES_IN_HOUR

# примерное количество боёв, которое будет происходить в час игрового времени
BATTLES_PER_HOUR: float = BATTLES_BEFORE_HEAL * CYCLES_IN_HOUR

#################
# прочие действия
#################

ACTION_IDLE_MINIMUM_TURNS: int = int(math.ceil(0.25 * TURNS_IN_HOUR))
ACTION_IDLE_TURNS_TO_LEVEL: int = 6  # количество ходов на уровень, которое герой бездельничает в соответствующем действии

###############################
# скорость героя (клеток / ход)
###############################

HERO_SPEED_BASE: float = 0.1

# бонусы в долях
HERO_SPEED_ARTIFACT_SMALL_BONUS: float = 0.02
HERO_SPEED_ARTIFACT_NORMAL_BONUS: float = 0.1

HERO_SPEED_COMPANION_SMALL_BONUS: float = 0.1
HERO_SPEED_COMPANION_NORMAL_BONUS: float = 0.15
HERO_SPEED_COMPANION_LARGE_BONUS: float = 0.2

HERO_SPEED_ABILITY_BONUS: float = 0.15

HERO_SPEED_MAX: float = HERO_SPEED_BASE * (1 +
                                           HERO_SPEED_ARTIFACT_NORMAL_BONUS +
                                           HERO_SPEED_COMPANION_LARGE_BONUS +
                                           HERO_SPEED_ABILITY_BONUS)
