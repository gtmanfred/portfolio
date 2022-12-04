import enum

import pydantic


class Item(pydantic.BaseModel):
    slots: int = pydantic.Field(1, const=True)
    cost: int


class Stats(pydantic.BaseModel):
    strength: int
    dexterity: int
    wisdom: int
    luck: int


class Size(str, enum.Enum):
    small = "small"
    medium = "medium"
    heavy = "heavy"


class Armor(Item):
    name: str
    slots: int = pydantic.Field(2, const=True)


class Ammo(Item):
    name: str
    info: str


class Equipment(Item):
    name: str
    quantity: int = 1


class Spell(pydantic.BaseModel):
    text: str


class Weapon(Item):
    name: str
    size: Size
    ranged: bool
    throwable: bool = False
    twohanded: bool = False


class Class(pydantic.BaseModel):
    name: str
    abilities: list[str]
    num_spells: int = 0
    num_weapons: int = 1
    spells: list[Spell] | None
    items: list[Equipment|Weapon] | None
    load_multiplier: int = 1
