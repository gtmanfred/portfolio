import enum
import random

import pydantic

from .utils.types import (
    Ammo,
    Armor,
    Equipment,
    Size,
    Spell,
    Stats,
    Weapon,
)
from .data.classes import base_classes
from .data.items import (
    ARMOR,
    WEAPON,
    cloak,
    knife,
    torches,
    waterskin,
)
from .data.spells import (
    ACTIONS,
    OBJECTS,
)

class Character(pydantic.BaseModel):

    name: str
    klass: str
    stats: Stats
    hp: int
    abilities: list[str]
    inventory: list[Weapon | Armor | Ammo | Equipment]
    spells: list[Spell]


class CharacterGenerator:

    def __init__(self, commoner=False, extra_classes=False):
        self.commoner = commoner
        self.extra_classes = extra_classes
        self.abilities = []
        self.inventory = []
        self.spells = []

    @classmethod
    def create(cls, commoner=False, extra_classes=False, seed=None):
        character = cls(commoner=commoner, extra_classes=extra_classes)
        character._generate(seed=seed)

        return Character(
            name=character.name,
            klass=character.class_,
            stats=character.stats,
            hp=character.hp,
            abilities=character.abilities,
            inventory=character.inventory,
            spells=character.spells,
        )


    def _generate(self, seed=None):
        if seed is not None:
            random.seed(seed)

        self._generate_name()
        self._generate_stats()
        self._generate_hp()
        self._generate_inventory()
        self._generate_spells()

    def _generate_name(self):
        self.name = 'Billy'

    def _generate_stats(self):
        if self.commoner:
            strength = sum([random.randint(1, 6), random.randint(1, 6), 3])
            dexterity = sum([random.randint(1, 6), random.randint(1, 6), 3])
            wisdom = sum([random.randint(1, 6), random.randint(1, 6), 3])
        else:
            strength = sum([random.randint(1, 6), random.randint(1, 6), random.randint(1, 6)])
            dexterity = sum([random.randint(1, 6), random.randint(1, 6), random.randint(1, 6)])
            wisdom = sum([random.randint(1, 6), random.randint(1, 6), random.randint(1, 6)])
        self.stats = Stats(
            strength=strength,
            dexterity=dexterity,
            wisdom=wisdom,
            luck=max(strength, dexterity, wisdom) // 2
        )

    def _generate_hp(self):
        hp_diff = random.randint(1, 6)
        self.hp = self.stats.strength + hp_diff

        if self.extra_classes:
            data = extra_classes(hp_diff)
        else:
            data = base_classes[hp_diff]

        self.abilities.extend(data['abilities'])
        self.class_ = data['class']
        self._num_spells = data['spells']
        self._num_weapons = data['weapons']

    def _generate_inventory(self):
        self.inventory = [
            cloak,
            knife,
            torches,
            waterskin,
        ]
        weapons = []
        while len([x for x in weapons if x < 6]) < self._num_weapons:
            weapons.append(random.randint(1, 6))

        for weapon in weapons:
            match weapon:
                case 1:
                    self._num_spells += 1
                case 2:
                    self.abilities.append("Advantage to climbing and grappling.")
                case 3:
                    self.abilities.append("Do d6 additional damage to unaware enemies.")
                    self.inventory.append(
                        random.choice([
                            weapon for weapon in WEAPON if weapon.size == Size.small and weapon.ranged is False
                        ])
                    )
                case 4:
                    self.abilities.append("+1 attack per round.")
                    self.inventory.append(
                        random.choice([
                            weapon for weapon in WEAPON if weapon.size == Size.medium and weapon.ranged is False
                        ])
                    )
                case 5:
                    self.abilities.append("Advantage on healing rolls.")

                    heavy = bool(random.randint(0, 1) % 2)
                    if heavy:
                        self.inventory.append(
                            random.choice([
                                weapon for weapon in WEAPON if weapon.size == Size.heavy and weapon.ranged is False
                            ])
                        )
                    else:
                        weap = random.choice([
                            weapon for weapon in WEAPON if weapon.ranged is True
                        ])
                        self.inventory.append(Weapon(**weap.dict()))
                        self.inventory.extend(weap.ammo)
                case 6:
                    self.inventory.append(random.choice(ARMOR))

    def _generate_spells(self):
        for _ in range(self._num_spells):
            action = random.choice(ACTIONS)
            objects = set()

            while len(objects) < action.num_objects:
                objects.add(random.choice(OBJECTS))

            self.spells.append(
                Spell(text=action.text.format(*objects))
            )
