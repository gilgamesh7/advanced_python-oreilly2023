from collections import namedtuple
from string import ascii_lowercase
from random import Random

rnd = Random(0)

class Entity(namedtuple('EntityBase','name value')):
    @classmethod
    def from_random(cls, *, random_state=None):
        random_state = random_state if random_state is not None else Random()
        return cls(
            name = ''.join(rnd.choices(ascii_lowercase, k=4)),
            value = rnd.randint(-1_000, +1_000),
        )

class Analysis:
    def load(self):
        self.data= [ ]