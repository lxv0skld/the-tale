

from . import constants as c


def idle_on_level(level: int) -> int:
    return c.ACTION_IDLE_MINIMUM_TURNS + c.ACTION_IDLE_TURNS_TO_LEVEL * (level - 1)
