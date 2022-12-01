import enum

import pydantic


class Item(pydantic.BaseModel):
    slots: int = pydantic.Field(1, const=True)


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
    cost: int
    slots: int = pydantic.Field(2, const=True)


class Ammo(Item):
    name: str
    info: str
    cost: int


class Equipment(Item):
    name: str
    cost: int
    quantity: int = 1


class Spell(pydantic.BaseModel):
    text: str


class Weapon(Item):
    name: str
    cost: int
    size: Size
    ranged: bool
    throwable: bool = False
    twohanded: bool = False
