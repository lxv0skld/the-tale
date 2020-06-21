
import smart_imports

smart_imports.all()


class TRIGGER(rels_django.DjangoEnum):
    probability = rels.Column()

    records = (('HABIT_EVENT_MOVE', 0, 'событие черт при движении', c.HABIT_EVENTS_MOVE_PROBABILITY),
               ('HABIT_EVENT_IN_PLACE', 1, 'событие черт в горде', c.HABIT_EVENTS_IN_PLACE_PROBABILITY))


def new_hero_triggers():
    turn = game_turn.number()

    checked_at = {trigger: turn for trigger in TRIGGER.records }
    events = {trigger: 0 for trigger in TRIGGER.records }

    return Triggers(checked_at=checked_at,
                    events=events)


class Triggers:
    __slots__ = ('checked_at', 'events')

    def __init__(self, checked_at, events):
        self.checked_at = checked_at
        self.events = events

    def check(self, trigger):
        if self.events.get(trigger, 0) == 0:
            return False

        self.events[trigger] -= 1

        return True

    def step(self):
        for trigger in TRIGGER.records:
            if random.random() < trigger.probability:
                self.events[trigger] += 1

    def serialize(self):
        return {'checked_at': {key.value: value for key, value in self.checked_at.items()},
                'events': {key.value: value for key, value in self.events.items()}}

    @classmethod
    def deserialize(cls, data):
        if data is None:
            return new_hero_triggers()

        checked_at = {TRIGGER(int(key)): value for key, value in data['triggers'].items()}
        events = {TRIGGER(int(key)): value for key, value in data['events'].items()}

        return cls(checked_at=checked_at,
                   events=events)
