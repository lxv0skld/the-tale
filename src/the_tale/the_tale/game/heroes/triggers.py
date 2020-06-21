
import smart_imports

smart_imports.all()


class TRIGGER(rels_django.DjangoEnum):
    probability = rels.Column()

    records = (('HABIT_EVENT_ON_MOVE', 0, 'событие черт при движении', c.HABIT_EVENTS_MOVE_PROBABILITY),
               ('HABIT_EVENT_IN_PLACE', 1, 'событие черт в горде', c.HABIT_EVENTS_IN_PLACE_PROBABILITY),
               ('COMPANION_EXPERIENCE_ON_MOVE', 2, 'спутнки даёт опыт в движении', c.COMPANIONS_WISDOM_PROBABILITY),
               ('EXP_FOR_KILL', 3, 'получить опыт за убийство', c.EXP_FOR_KILL_PROBABILITY))


def new_hero_triggers():
    return Triggers(events={})


# упрощённая реализация:
# - делаем тригеры ненакапливающимися, в будущем разумно сделать накопление, чтобы реализовать более четный рандом
# - предполагаем проверку срабатывания на каждом ходу, разумно сделать по хитрым формулам в момент проверки
class Triggers:
    __slots__ = ('checked_at', 'events')

    def __init__(self, events):
        self.events = events

    def check(self, trigger):
        return self.events.pop(trigger)

    def step(self):
        for trigger in TRIGGER.records:
            if random.random() < trigger.probability:
                self.events[trigger] = True

    def serialize(self):
        return {'events': {key.value: value for key, value in self.events.items()}}

    @classmethod
    def deserialize(cls, data):
        if data is None:
            return new_hero_triggers()

        events = {TRIGGER(int(key)): value for key, value in data['events'].items()}

        return cls(events=events)
