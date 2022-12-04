import enum
import random

import pydantic

from ..bastards.utils.types import (
    Ammo,
    Armor,
    Equipment,
    Size,
    Spell,
    Stats,
    Weapon,
)
from ..bastards.data.classes import (
    base_classes,
    extra_classes,
)
from ..bastards.data.items import (
    ARMOR,
    WEAPON,
    cloak,
    knife,
    torches,
    waterskin,
)
from ..bastards.data.spells import (
    ACTIONS,
    OBJECTS,
)


class Character(pydantic.BaseModel):

    name: str
    klass: str
    stats: Stats
    hp: int
    ac: int
    abilities: list[str]
    max_load: int
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
            ac=len([item for item in character.inventory if isinstance(item, Armor)]),
            max_load=character.max_load,
            abilities=character.abilities,
            inventory=character.inventory,
            spells=character.spells,
        )

    def _generate(self, seed=None):
        self.seed = seed
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
        self.max_load = strength

    def _generate_hp(self):
        hp_diff = random.randint(1, 6)

        if self.commoner:
            self.hp = hp_diff
            match hp_diff:
                case 1:
                    self.class_ = 'scholar'
                    self.stats.wisdom += 3
                case 2:
                    self.class_ = 'acolyte'
                    self.stats.dexterity += 3
                case 3:
                    self.class_ = 'burglar'
                    self.stats.dexterity += 3
                case 4:
                    self.class_ = 'farmer'
                    self.stats.strength += 3
                case 5:
                    self.class_ = 'soldier'
                    self.stats.strength += 3
                case 6:
                    self.class_ = 'outlander'
                    self.stats.wisdom += 3
        else:
            self.hp = self.stats.strength + hp_diff
            if self.extra_classes:
                data = random.choice(extra_classes[hp_diff])
            else:
                data = base_classes[hp_diff]

            self.abilities.extend(data.abilities)
            self.class_ = data.name
            self._num_spells = data.num_spells
            self._num_weapons = data.num_weapons
            self.max_load *= data.load_multiplier
            if data.items is not None:
                self.inventory = data.items.copy()

    def _generate_inventory(self):
        self.inventory.extend([
            cloak,
            knife,
            torches,
            waterskin,
        ])

        if not hasattr(self, '_num_weapons'):
            return

        weapons = []
        while len([x for x in weapons if x < 6]) < getattr(self, '_num_weapons', 0):
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
        for _ in range(getattr(self, '_num_spells', 0)):
            action = random.choice(ACTIONS)
            objects = set()

            while len(objects) < action.num_objects:
                objects.add(random.choice(OBJECTS))

            self.spells.append(
                Spell(text=action.text.format(*objects))
            )
