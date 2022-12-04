from ..utils.types import Ammo
from ..utils.types import Class
from ..utils.types import Equipment
from ..utils.types import Spell
from ..utils.types import Weapon
    

base_classes = {
    1: Class(
        name="wizard",
        num_spells=3,
        abilities=["You can read all languages."],
    ),
    2: Class(
        name="diviner",
        num_spells=1,
        abilities=["You may cast bones or pull cards to point the way to a stated destination."],
    ),
    3: Class(
        name="acrobat",
        abilities=[
            "You can fit through any space as big as your head.",
            "Your unarmed attackes deal damage as a small weapon.",
        ],
    ),
    4: Class(
        name="thief",
        abilities=[
            "You may roll a d20 under Luck to have something small and useful in your pocket.",
            "You have Advantage on lockpicking and sleight of hand.",
        ]
    ),
    5: Class(
        name="fighter",
        num_weapons=2,
        abilities=[
            "You have Advantage to hit with melee weapons.",
        ]
    ),
    6: Class(
        name="barbarian",
        abilities=[
            (
                "When you attack with a weapon, roll the next size up for damage. "
                "Ignore this ability while wearing armor."
            ),
        ]
    ),
}

one_classes = (
    Class(
        name="alchemist",
        abilities=[
             "You can create poisons or potions from plants and common materials, or butcher monsters for stronger solutions.",
        ],
    ),
    Class(
        name="adjacist",
        abilities=[
            "Test Dexterity to instantly be anywhere within your line of sight.",
        ],
    ),
    Class(
        name="commoner",
        abilities=[
            "You have a farm and a family, somewhere.",
        ],
    ),
    Class(
        name="exile",
        abilities=[
            "Start with overwhelming debt and a stalwart retainer.",
        ],
    ),
    Class(
        name="physiker",
        num_spells=1,
        abilities=[
            "With careful calculation, you can reroll one die result each week.",
        ],
    ),
    Class(
        name="astrologer",
        num_spells=2,
        abilities=[
            "You never lose your way as long as you can see the stars."
        ],
    ),
)
two_classes = (
    Class(
        name="cleric",
        num_spells=1,
        spells=[
            Spell(text="Mend Flesh"),
        ],
        abilities=[
            "Mend Flesh can heal yourself for d6 per level, or twice as much if healing someone else.",
        ],
    ),
    Class(
        name="potion-seller",
        items=[
            Equipment(name="strong booze potion", cost=0, quantity=3),
            Equipment(name="random spell potion", cost=0, quantity=3),
        ],
        abilities=[
            "You can brew one potion with a new random spell each day.",
        ],
    ),
    Class(
        name="butcher",
        abilities=[
            "Search any body to gain d6 meat rations.",
        ],
    ),
    Class(
        name="half-ling",
        abilities=[
            "Your body is bisected horizontally. You can detach them at will and control the disparate parts separately.",
        ],
    ),
    Class(
        name="porter",
        load_modifier=2,
        items=[
            Equipment(name="stolen luggage", cost=0)
        ],
        abilities=[
            "You carry double the usual amount",
        ],
    ),
    Class(
        name="goblin",
        abilities=[
            "You are a nasty freak, and can make your blood poisonous by immersing yourself in trash or sewage.",
        ],
    ),
)
three_classes = (
    Class(
        name="satyr",
        abilities=[
            "You can dance, jeer, and skip in circles, enticing those around you to either join or watch, stunned.",
        ],
    ),
    Class(
        name="blaggard",
        abilities=[
            "You can expell noxious gas disorienting people and beasts in arms reach. Once each day, you can spit poison at an enemy (d6 damage to yourself and 3d6 to your target).",
        ],
    ),
    Class(
        name="gleaner",
        items=[
            Equipment(name="basket", cost=0),
        ],
        abilities=[
            "You can always find something edible in the wilderness.",
        ],
    ),
    Class(
        name="witch",
        abilities=[
            "You can speak with animals.",
        ],
        spells=[
            Spell(text="Turn Milk"),
            Spell(text="Identify Plant"),
            Spell(text="Hex"),
        ],
    ),
    Class(
        name="ringmaster",
        abilities=[
            "Start with a half-trained bear retainer."
        ],
    ),
    Class(
        name="mudlark",
        abilities=[
            "Can find a random item in mud, once each day."
        ],
    ),
)
four_classes = (
    Class(
        name="opera singer",
        abilities=[
            "Your well trained voice can destroy one type of object.",
        ],
    ),
    Class(
        name="wrestler",
        abilities=[
            "Roll to grapple with advantage.",
            "+d6 damage to all attacks on grappled opponents.",
        ],
    ),
    Class(
        name="gunkscraper",
        abilities=[
            "You spent your life scraping gunk. You are immune to poison, and even a small taste of your flesh is fatal to others."
        ],
    ),
    Class(
        name="elf",
        num_spells=1,
        abilities=[
            "You see through stone as if it were murky water.",
            "Blind in sunlight.",
        ],
    ),
    Class(
        name="cynocephalus",
        abilities=[
            "See in black-and-white, and can track scents over leagues.",
            "Your bite does damage as a small weapon.",
        ],
    ),
    Class(
        name="dancer",
        abilities=[
            "Start with d6 dramatic costumes.",
            "Reroll one Dexterity check each day.",
        ],
    ),
)
five_classes = (
    Class(
        name="knight",
        abilities=[
            "You can impart gaes on one person or entity at a time. The only way to remove it is to complete the quest or die.",
        ],
    ),
    Class(
        name="sapper",
        items=[
            Ammo(name="black powder bombs", info="bag of 5", cost=0),
            Equipment(name="shovel", cost=0),
        ],
        abilities=[
        ],
    ),
    Class(
        name="janitor",
        items=[
            Equipment(name="ring of keys", cost=0),
        ],
        abilities=[
            "You ring of keys works once on any door.",
        ],
    ),
    Class(
        name="bodyguard",
        abilities=[
            "You can redirect attacks on others to hit you instead, and only take half damage.",
        ],
    ),
    Class(
        name="prisoner",
        abilities=[
            "Spring from gaol and nutured by ghouls, you can access the chthonic labyrinth between worlds once each week.",
        ],
    ),
    Class(
        name="channeler",
        abilities=[
            "You meat is a vessel for spirits of unquiet dead.",
            "Start with d3 ghosts with unfinished business inhabiting your mind.",
        ],
    ),
)
six_classes = (
    Class(
        name="ghost",
        abilities=[
            "You're intangible and can't touch physical objects.",
            "You can touch magic",
            "You can't die"
        ],
    ),
    Class(
        name="dwarf",
        item=[
            Equipment(name="ancestral weapon", cost=0),
        ],
        abilities=[
            "You have metal bones. You immediately sink in water.",
        ],
    ),
    Class(
        name="slime",
        abilities=[
            "You sluged-body can split into halves with equal health.",
        ],
    ),
    Class(
        name="centaur",
        abilities=[
            "A horrific accident, a melding of horse and human.",
            "Can run as fast as a gelding, but require weekly anti-mutagens to stabilize your flesh.",
        ],
    ),
    Class(
        name="golem",
        abilities=[
            "You were created by another from clay, stone, flesh, or metal.",
            "You need not eat, but the geas burning in your mind goads you to duty.",
        ],
    ),
    Class(
        name="dream-warrior",
        abilities=[
            "Your body and mind are honed like weapons. They allow you no rest.",
            "You can invade other's dreamworlds and kill them",
        ],
    ),
)

extra_classes = {
    1: one_classes,
    2: two_classes,
    3: three_classes,
    4: four_classes,
    5: five_classes,
    6: six_classes,
}
