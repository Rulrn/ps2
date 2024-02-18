
from dataclasses import dataclass
from enum import Enum

from weapons import Weapon, C75_VIPER, L100_PYTHON_AP, L100_PYTHON_HEAT, L100_PYTHON_HESH, L2_100_KINGSNAKE, PERIHELION_L_VXC, SKYGUARD, JGX11
from empires import Empire

class VehiculeType(Enum):
    LIGHT = "light"
    HEAVY = "heavy"
    TRANSPORT = "transport"
    MBT = "mbt"
    PATROL = "patrol_boat"

class VehiculeName(Enum):
    MAX = "max"
    FLASH = "flash"
    JAVELIN = "javelin"
    HARASSER = "harasser"
    SUNDERER = "sunderer"
    LIGHTNING = "lightning"
    MBT = "mbt"
    ANT = "ant"
    ESF = "esf"
    DERVISH = "dervish"
    LIBERATOR = "liberator"
    GALAXY = "galaxy"
    VALKYRIE = "valkyrie"
    CORSAIR = "corsair"

class VehiculeColor(Enum):
    DEFAULT = "black"
    MAX = "black"
    FLASH = "black"
    JAVELIN = "black"
    HARASSER = "black"
    SUNDERER = "black"
    LIGHTNING = "black"
    MBT = "black"
    ANT = "black"
    ESF = "black"
    DERVISH = "black"
    LIBERATOR = "black"
    GALAXY = "black"
    VALKYRIE = "black"
    CORSAIR = "black"

@dataclass
class Resistances:
    melee: float = 0.0
    small_arms: float = 0.0
    common_explosive: float = 0.0
    heavy_explsive: float = 0.0
    tank_mines: float = 0.0
    heavy_machine_guns: float = 0.0
    anti_aircraft_machine_guns: float = 0.0
    flask_explosion: float = 0.0
    light_anti_vehicule: float = 0.0
    infantry_rocket_launchers: float = 0.0
    tank_shells: float = 0.0
    gatling_guns: float = 0.0
    aircraft_machine_guns: float = 0.0
    air_to_ground_warheads: float = 0.0
    anti_material_rifle: float = 0.0
    a2a_missiles: float = 0.0
    infantry_lock_on: float = 0.0


@dataclass
class DirectionalArmor:
    front: float = 0.0
    top: float = 0.0
    side: float = 0.0
    rear: float = 0.0
    bottom: float = 0.0


@dataclass
class VehiculeProperties:
    vtype: VehiculeType
    empire: Empire
    cost: int
    health: int
    decay: float  # in minutes
    primary_weapon: list[Weapon]
    empire_specific: list[Weapon]


@dataclass
class Vehicule:
    name: VehiculeName
    properties: VehiculeProperties
    resistances: Resistances
    directionnal_armor: DirectionalArmor
    color: VehiculeColor = VehiculeColor.DEFAULT

LIGHTNING_PROPERTIES = VehiculeProperties(
    vtype=VehiculeType.LIGHT,
    empire=Empire.ALL,
    cost=300,
    health=4000,
    decay=5,
    primary_weapon=[C75_VIPER,
                    L100_PYTHON_HEAT,
                    L100_PYTHON_AP,
                    L100_PYTHON_HESH,
                    SKYGUARD],
    empire_specific=[  # TODO complete
        L2_100_KINGSNAKE,
        JGX11,
        PERIHELION_L_VXC,
    ]
)

LIGHTNING = Vehicule(
    name=VehiculeName.LIGHTNING,
    color=VehiculeColor.LIGHTNING,
    directionnal_armor=DirectionalArmor(
        front=0.0,
        top=0.0,
        side=-15.0,
        rear=-50.0,
        bottom=-100.0
    ),
    properties=LIGHTNING_PROPERTIES,
    resistances=Resistances(
        melee=100.0,
        small_arms=100.0,
        common_explosive=100.0,
        heavy_explsive=100.0,
        tank_mines=-100.0,
        heavy_machine_guns=80.0,
        anti_aircraft_machine_guns=85.0,
        flask_explosion=100.0,
        light_anti_vehicule=-20.0,
        infantry_rocket_launchers=0.0,
        tank_shells=-50.0,
        gatling_guns=75.0,
        aircraft_machine_guns=90.0,
        air_to_ground_warheads=0.0,
        anti_material_rifle=40.0,
        a2a_missiles=20.0,
        infantry_lock_on=0.0,
    )
)
