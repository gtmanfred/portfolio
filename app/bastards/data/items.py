from ..utils.types import (
    Ammo,
    Armor,
    Equipment,
    Size,
    Weapon as BaseWeapon,
)


class Weapon(BaseWeapon):
    ammo: list[Ammo] | None


arrows = Ammo(name="arrows", info="Quiver of 10", cost=1)
darts = Ammo(name="darts", info="Bundle of 10", cost=2)
bullets = Ammo(name="bullet", info="Pouch of 10", cost=5)
powder = Ammo(name="powder", info="Explosive", cost=7)


AMMO = (
    arrows,
    darts,
    bullets,
    powder,
    Ammo(name="chemical", info="Clay jar full of caustic substance", cost=22),
    Ammo(name="molotov", info="Fire spreads and burns for d6 rounds", cost=5),
)


ARMOR = (
    Armor(name="helmet", cost=10),
    Armor(name="cuirass", cost=17),
    Armor(name="greaves", cost=7),
    Armor(name="gauntlets", cost=12),
    Armor(name="surcoat", cost=5),
    Armor(name="shield", cost=9),
)


cloak = Equipment(name="cloak", cost=10)
knife = Equipment(name="knife", cost=3)
rations = Equipment(name="rations", cost=4, quantity=3)
torches = Equipment(name="torches", cost=4, quantity=3)
waterskin = Equipment(name="waterskin", cost=5)


EQUIPMENT = (
    Equipment(name="backpack", cost=10),
    Equipment(name="bellows", cost=6),
    Equipment(name="bottle", cost=3),
    Equipment(name="caltrops", cost=2),
    Equipment(name="candle", cost=2),
    Equipment(name="chalk", cost=1),
    cloak,
    Equipment(name="crowbar", cost=9),
    Equipment(name="dice", cost=2),
    Equipment(name="file", cost=2),
    Equipment(name="flint and steel", cost=2),
    Equipment(name="glue", cost=6),
    Equipment(name="grappling hook", cost=5),
    Equipment(name="hammer", cost=2),
    Equipment(name="herbs", cost=5),
    Equipment(name="hourglass", cost=16),
    Equipment(name="iron spikes", cost=1),
    knife,
    Equipment(name="lantern", cost=1),
    Equipment(name="lockpicks", cost=10),
    Equipment(name="mirror", cost=11),
    Equipment(name="net", cost=6),
    Equipment(name="oil", cost=11),
    Equipment(name="parchment", cost=10),
    Equipment(name="perfume", cost=20),
    Equipment(name="pole", cost=3),
    rations,
    Equipment(name="rope", cost=3),
    Equipment(name="sack", cost=1),
    Equipment(name="sponge", cost=1),
    Equipment(name="stakes", cost=1),
    Equipment(name="tent", cost=11),
    torches,
    waterskin,
    Equipment(name="wine", cost=11),
)

WEAPON = (
    Weapon(name="ax", cost=4, size=Size.medium, ranged=False, throwable=False, twohanded=False, ammo=None),
    Weapon(name="bow", cost=5, size=Size.medium, ranged=True, throwable=False, twohanded=False, ammo=[arrows]),
    Weapon(name="club", cost=2, size=Size.medium, ranged=False, throwable=False, twohanded=False, ammo=None),
    Weapon(name="crossbow", cost=12, size=Size.heavy, ranged=True, throwable=False, twohanded=False, ammo=[darts]),
    Weapon(name="dagger", cost=1, size=Size.small, ranged=False, throwable=True, twohanded=False, ammo=None),
    Weapon(name="mace", cost=3, size=Size.heavy, ranged=False, throwable=False, twohanded=False, ammo=None),
    Weapon(name="musket", cost=20, size=Size.heavy, ranged=True, throwable=False, twohanded=False, ammo=[bullets, powder]),
    Weapon(name="polearm", cost=11, size=Size.heavy, ranged=False, throwable=False, twohanded=False, ammo=None),
    Weapon(name="saw", cost=6, size=Size.medium, ranged=False, throwable=False, twohanded=False, ammo=None),
    Weapon(name="sling", cost=3, size=Size.small, ranged=True, throwable=False, twohanded=False, ammo=[bullets]),
    Weapon(name="spear", cost=5, size=Size.medium, ranged=False, throwable=True, twohanded=False, ammo=None),
    Weapon(name="staff", cost=2, size=Size.medium, ranged=False, throwable=False, twohanded=False, ammo=None),
    Weapon(name="sword", cost=5, size=Size.medium, ranged=False, throwable=False, twohanded=False, ammo=None),
    Weapon(name="two-hander", cost=14, size=Size.heavy, ranged=False, throwable=False, twohanded=True, ammo=None),
    Weapon(name="warhammer", cost=4, size=Size.medium, ranged=False, throwable=False, twohanded=False, ammo=None),
)
