from dataclasses import dataclass
from enum import Enum

from empires import Empire


# Vehicules
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
    PROWLER = "prowler"
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
    PROWLER = "red"
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

class WeaponType(Enum):
    ANTI_VEHICULE = "ANTI_VEHICULE"
    ANTI_INFANTRY = "ANTI_INFANTRY"
    ANTI_AIR = "ANTI_AIR"


class EffectiveRange(Enum):
    CLOSE = "Close"
    LONG = "Long"
    VERY_LONG = "Very Long"

class FireMode(Enum):
    AUTOMATIC = "Automatic"
    SEMI_AUTOMATIC = "Semi Automatic"

@dataclass
class IndirectDamage:
    distance: float  # meters
    damage: float

@dataclass
class DamageTypes:
    melee: bool = False
    small_arms: bool = False
    common_explosive: bool = False
    heavy_explsive: bool = False
    tank_mines: bool = False
    heavy_machine_guns: bool = False
    anti_aircraft_machine_guns: bool = False
    flask_explosion: bool = False
    light_anti_vehicule: bool = False
    infantry_rocket_launchers: bool = False
    tank_shells: bool = False
    gatling_guns: bool = False
    aircraft_machine_guns: bool = False
    air_to_ground_warheads: bool = False
    anti_material_rifle: bool = False
    a2a_missiles: bool = False
    infantry_lock_on: bool = False


@dataclass
class WeaponProperties:
    cert_cost: int
    dc_cost: int
    empire: Empire
    can_use: list[VehiculeName]
    weapon_type: WeaponType
    fire_rate: float  # RPM
    muzzle_velocity: float  # m/s
    effective_range: EffectiveRange
    fire_modes: list[FireMode]
    max_damage: float
    min_damage: float
    max_indirect_damage: IndirectDamage
    min_indirect_damage: IndirectDamage
    damage_type: list[DamageTypes]
    reload_speed: float  # seconds
    magazine_size: int
    ammunition_pool: int
    min_cone_of_fire: float
    max_cone_of_fire: float
    bloom_per_shot: float

class WeaponName(Enum):
    C75_VIPER = "C75_VIPER"
    L100_PYTHON_HEAT = "L100_PYTHON_HEAT"
    L100_PYTHON_AP = "L100_PYTHON_AP"
    L100_PYTHON_HESH = "L100_PYTHON_HESH"
    SKYGUARD = "SKYGUARD"
    L2_100_KINGSNAKE = "L2_100_KINGSNAKE"
    JGX11 = "JGX11"
    PERIHELION_L_VXC = "PERIHELION_L_VXC"
    P2_120_HEAT = "P2_120_HEAT"
    P2_120_AP = "P2_120_AP"
    P2_120_HESH = "P2_120_HESH"
    P4_120_KINGSNAKE = "P4_120_KINGSNAKE"
    TITAN_150_HEAT = "TITAN_150_HEAT"
    TITAN_150_AP = "TITAN_150_AP"
    TITAN_150_HESH = "TITAN_150_HESH"
    JGX12 = "JGX12"
    SUPERNOVA_PC = "SUPERNOVA_PC"
    SUPERNOVA_FPC = "SUPERNOVA_FPC"
    SUPERNOVA_VPC = "SUPERNOVA_VPC"
    PERIHELION_VXC = "PERIHELION_VXC"

class WeaponColor(Enum):
    C75_VIPER = "green"
    L100_PYTHON_HEAT = "red"
    L100_PYTHON_AP = "orange"
    L100_PYTHON_HESH = "black"
    L2_100_KINGSNAKE = "blue"
    SKYGUARD = "black"
    JGX11 = "black"
    PERIHELION_L_VXC = "black"
    P2_120_HEAT = "red"
    P2_120_AP = "orange"
    P2_120_HESH = "black"
    P4_120_KINGSNAKE = "blue"
    TITAN_150_HEAT = "black"
    TITAN_150_AP = "black"
    TITAN_150_HESH = "black"
    JGX12 = "black"
    SUPERNOVA_PC = "black"
    SUPERNOVA_FPC = "black"
    SUPERNOVA_VPC = "black"
    PERIHELION_VXC = "black"

@dataclass
class Weapon:
    name: WeaponName
    color: WeaponColor
    properties: WeaponProperties

@dataclass
class VehiculeProperties:
    vtype: VehiculeType
    empire: Empire
    cost: int
    health: int
    decay: float  # in minutes
    primary_weapon: list[Weapon]
    secondary_weapon: list[Weapon]
    empire_specific: list[Weapon]

@dataclass
class Vehicule:
    name: VehiculeName
    properties: VehiculeProperties
    resistances: Resistances
    directionnal_armor: DirectionalArmor
    color: VehiculeColor = VehiculeColor.DEFAULT

C75_VIPER = Weapon(
    name=WeaponName.C75_VIPER,
    color=WeaponColor.C75_VIPER,
    properties=WeaponProperties(
        cert_cost=875,
        dc_cost=599,
        empire=Empire.ALL,
        can_use=[VehiculeName.LIGHTNING],
        weapon_type=WeaponType.ANTI_VEHICULE,
        fire_rate=240,
        muzzle_velocity=200,
        effective_range=EffectiveRange.CLOSE,
        fire_modes=[FireMode.AUTOMATIC],
        max_damage=250,
        min_damage=250,
        max_indirect_damage=IndirectDamage(distance=1, damage=250),
        min_indirect_damage=IndirectDamage(distance=3, damage=25),
        damage_type=[DamageTypes.tank_shells, DamageTypes.common_explosive],
        reload_speed=4.5,
        magazine_size=6,
        ammunition_pool=92,
        min_cone_of_fire=0,
        max_cone_of_fire=1.5,
        bloom_per_shot=0.5,
    )
)

L100_PYTHON_HEAT = Weapon(
    name=WeaponName.L100_PYTHON_HEAT,
    color=WeaponColor.L100_PYTHON_HEAT,
    properties=WeaponProperties(
        cert_cost=0,
        dc_cost=0,
        empire=Empire.ALL,
        can_use=[VehiculeName.LIGHTNING],
        weapon_type=WeaponType.ANTI_VEHICULE,
        fire_rate=60,
        muzzle_velocity=None,
        effective_range=EffectiveRange.LONG,
        fire_modes=[FireMode.SEMI_AUTOMATIC],
        max_damage=575,
        min_damage=575,
        max_indirect_damage=IndirectDamage(distance=1, damage=500),
        min_indirect_damage=IndirectDamage(distance=4, damage=50),
        damage_type=[DamageTypes.tank_shells, DamageTypes.common_explosive],
        reload_speed=2.5,
        magazine_size=1,
        ammunition_pool=48,
        min_cone_of_fire=None,
        max_cone_of_fire=None,
        bloom_per_shot=None,
    )
)

L100_PYTHON_AP = Weapon(
    name=WeaponName.L100_PYTHON_AP,
    color=WeaponColor.L100_PYTHON_AP,
    properties=WeaponProperties(
        cert_cost=875,
        dc_cost=599,
        empire=Empire.ALL,
        can_use=[VehiculeName.LIGHTNING],
        weapon_type=WeaponType.ANTI_VEHICULE,
        fire_rate=60,
        muzzle_velocity=250,
        effective_range=EffectiveRange.LONG,
        fire_modes=[FireMode.SEMI_AUTOMATIC],
        max_damage=700,
        min_damage=700,
        max_indirect_damage=IndirectDamage(distance=1, damage=500),
        min_indirect_damage=IndirectDamage(distance=3, damage=50),
        damage_type=[DamageTypes.tank_shells, DamageTypes.common_explosive],
        reload_speed=3,
        magazine_size=1,
        ammunition_pool=36,
        min_cone_of_fire=None,
        max_cone_of_fire=None,
        bloom_per_shot=None,
    )
)

L2_100_KINGSNAKE = Weapon(
    name=WeaponName.L2_100_KINGSNAKE,
    color=WeaponColor.L2_100_KINGSNAKE,
    properties=WeaponProperties(
        cert_cost=875,
        dc_cost=599,
        empire=Empire.TR,
        can_use=[VehiculeName.LIGHTNING],
        weapon_type=WeaponType.ANTI_VEHICULE,
        fire_rate=316,  # 333 wiki
        muzzle_velocity=225,
        effective_range=EffectiveRange.VERY_LONG,
        fire_modes=[FireMode.SEMI_AUTOMATIC],
        max_damage=400,
        min_damage=400,
        max_indirect_damage=IndirectDamage(distance=1, damage=325),
        min_indirect_damage=IndirectDamage(distance=3, damage=50),
        damage_type=[DamageTypes.tank_shells, DamageTypes.common_explosive],
        reload_speed=2.75,
        magazine_size=2,
        ammunition_pool=80,
        min_cone_of_fire=0.2,
        max_cone_of_fire=0.25,
        bloom_per_shot=0.05,
    )
)

L100_PYTHON_HESH = Weapon(
    name=WeaponName.L100_PYTHON_HESH,
    color=WeaponColor.L100_PYTHON_HESH,
    properties=WeaponProperties(
        cert_cost=875,
        dc_cost=599,
        empire=Empire.ALL,
        can_use=[VehiculeName.LIGHTNING],
        weapon_type=WeaponType.ANTI_INFANTRY,
        fire_rate=600,
        muzzle_velocity=600,
        effective_range=EffectiveRange.LONG,
        fire_modes=[FireMode.SEMI_AUTOMATIC],
        max_damage=600,
        min_damage=600,
        max_indirect_damage=IndirectDamage(distance=2, damage=800),
        min_indirect_damage=IndirectDamage(distance=5, damage=50),
        damage_type=[DamageTypes.tank_shells, DamageTypes.common_explosive],
        reload_speed=3.25,
        magazine_size=1,
        ammunition_pool=36,
        min_cone_of_fire=None,
        max_cone_of_fire=None,
        bloom_per_shot=None,
    )
)

SKYGUARD = Weapon(
    name=WeaponName.SKYGUARD,
    color=WeaponColor.SKYGUARD,
    properties=WeaponProperties(
        cert_cost=875,
        dc_cost=599,
        empire=Empire.ALL,
        can_use=[VehiculeName.LIGHTNING],
        weapon_type=WeaponType.ANTI_AIR,
        fire_rate=480,
        muzzle_velocity=400,
        effective_range=EffectiveRange.LONG,
        fire_modes=[FireMode.AUTOMATIC],
        max_damage=200,
        min_damage=150,
        max_indirect_damage=IndirectDamage(distance=5, damage=5),
        min_indirect_damage=IndirectDamage(distance=8, damage=1),
        damage_type=[DamageTypes.heavy_machine_guns, DamageTypes.flask_explosion],
        reload_speed=3.0,
        magazine_size=70,
        ammunition_pool=1050,
        min_cone_of_fire=1.5,
        max_cone_of_fire=1.5,
        bloom_per_shot=None,
    )
)

JGX11 = Weapon(
    name=WeaponName.JGX11,
    color=WeaponColor.JGX11,
    properties=WeaponProperties(
        cert_cost=875,
        dc_cost=599,
        empire=Empire.NC,
        can_use=[VehiculeName.LIGHTNING],
        weapon_type=WeaponType.ANTI_VEHICULE,
        fire_rate=13,
        muzzle_velocity=200,
        effective_range=EffectiveRange.VERY_LONG,
        fire_modes=[FireMode.SEMI_AUTOMATIC],
        max_damage=500,
        min_damage=500,
        max_indirect_damage=IndirectDamage(distance=1, damage=350),
        min_indirect_damage=IndirectDamage(distance=5, damage=100),
        damage_type=[DamageTypes.tank_shells],
        reload_speed=4,
        magazine_size=1,
        ammunition_pool=36,
        min_cone_of_fire=None,
        max_cone_of_fire=None,
        bloom_per_shot=None,
    )
)

PERIHELION_L_VXC = Weapon(
    name=WeaponName.PERIHELION_L_VXC,
    color=WeaponColor.PERIHELION_L_VXC,
    properties=WeaponProperties(
        cert_cost=875,
        dc_cost=599,
        empire=Empire.VS,
        can_use=[VehiculeName.LIGHTNING],
        weapon_type=WeaponType.ANTI_VEHICULE,
        fire_rate=60,
        muzzle_velocity=175,
        effective_range=EffectiveRange.VERY_LONG,
        fire_modes=[FireMode.SEMI_AUTOMATIC],
        max_damage=450,
        min_damage=450,
        max_indirect_damage=IndirectDamage(distance=1, damage=300),
        min_indirect_damage=IndirectDamage(distance=2, damage=50),
        damage_type=[DamageTypes.tank_shells, DamageTypes.common_explosive],
        reload_speed=2.5,
        magazine_size=3,
        ammunition_pool=60,
        min_cone_of_fire=None,
        max_cone_of_fire=None,
        bloom_per_shot=None,
    )
)

P2_120_HEAT = Weapon(
    name=WeaponName.P2_120_HEAT,
    color=WeaponColor.P2_120_HEAT,
    properties=WeaponProperties(
        cert_cost=0,
        dc_cost=0,
        empire=Empire.TR,
        can_use=[VehiculeName.PROWLER],
        weapon_type=WeaponType.ANTI_VEHICULE,
        fire_rate=120,
        muzzle_velocity=225,
        effective_range=EffectiveRange.LONG,
        fire_modes=[FireMode.SEMI_AUTOMATIC],
        max_damage=475,
        min_damage=475,
        max_indirect_damage=IndirectDamage(distance=1, damage=450),
        min_indirect_damage=IndirectDamage(distance=4, damage=50),
        damage_type=[DamageTypes.tank_shells, DamageTypes.common_explosive],
        reload_speed=2.5,
        magazine_size=2,
        ammunition_pool=56,
        min_cone_of_fire=None,
        max_cone_of_fire=None,
        bloom_per_shot=None,
    )
)

P2_120_AP = Weapon(
    name=WeaponName.P2_120_AP,
    color=WeaponColor.P2_120_AP,
    properties=WeaponProperties(
        cert_cost=875,
        dc_cost=599,
        empire=Empire.TR,
        can_use=[VehiculeName.PROWLER],
        weapon_type=WeaponType.ANTI_VEHICULE,
        fire_rate=120,
        muzzle_velocity=250,
        effective_range=EffectiveRange.LONG,
        fire_modes=[FireMode.SEMI_AUTOMATIC],
        max_damage=600,
        min_damage=600,
        max_indirect_damage=IndirectDamage(distance=1, damage=450),
        min_indirect_damage=IndirectDamage(distance=3, damage=50),
        damage_type=[DamageTypes.tank_shells, DamageTypes.common_explosive],
        reload_speed=3.5,
        magazine_size=2,
        ammunition_pool=46,
        min_cone_of_fire=None,
        max_cone_of_fire=None,
        bloom_per_shot=None,
    )
)

P2_120_HESH = Weapon(
    name=WeaponName.P2_120_HESH,
    color=WeaponColor.P2_120_HESH,
    properties=WeaponProperties(
        cert_cost=875,
        dc_cost=599,
        empire=Empire.TR,
        can_use=[VehiculeName.PROWLER],
        weapon_type=WeaponType.ANTI_VEHICULE,
        fire_rate=120,
        muzzle_velocity=200,
        effective_range=EffectiveRange.LONG,
        fire_modes=[FireMode.SEMI_AUTOMATIC],
        max_damage=550,
        min_damage=550,
        max_indirect_damage=IndirectDamage(distance=1, damage=600),
        min_indirect_damage=IndirectDamage(distance=5, damage=50),
        damage_type=[DamageTypes.tank_shells, DamageTypes.common_explosive],
        reload_speed=3.5,
        magazine_size=2,
        ammunition_pool=50,
        min_cone_of_fire=None,
        max_cone_of_fire=None,
        bloom_per_shot=None,
    )
)

P4_120_KINGSNAKE = Weapon(
    name=WeaponName.P4_120_KINGSNAKE,
    color=WeaponColor.P4_120_KINGSNAKE,
    properties=WeaponProperties(
        cert_cost=875,
        dc_cost=599,
        empire=Empire.TR,
        can_use=[VehiculeName.PROWLER],
        weapon_type=WeaponType.ANTI_VEHICULE,
        fire_rate=300,
        muzzle_velocity=225,
        effective_range=EffectiveRange.VERY_LONG,
        fire_modes=[FireMode.SEMI_AUTOMATIC],
        max_damage=350,
        min_damage=350,
        max_indirect_damage=IndirectDamage(distance=1, damage=300),
        min_indirect_damage=IndirectDamage(distance=3, damage=50),
        damage_type=[DamageTypes.tank_shells, DamageTypes.common_explosive],
        reload_speed=3.5,
        magazine_size=4,
        ammunition_pool=96,
        min_cone_of_fire=0.2,
        max_cone_of_fire=0.35,
        bloom_per_shot=0.05,
    )
)

# TODO
TITAN_150_HEAT = Weapon(
    name=WeaponName.TITAN_150_HEAT,
    color=WeaponColor.TITAN_150_HEAT,
    properties=WeaponProperties(
        cert_cost=875,
        dc_cost=599,
        empire=Empire.TR,
        can_use=[VehiculeName.PROWLER],
        weapon_type=WeaponType.ANTI_VEHICULE,
        fire_rate=300,
        muzzle_velocity=225,
        effective_range=EffectiveRange.VERY_LONG,
        fire_modes=[FireMode.SEMI_AUTOMATIC],
        max_damage=350,
        min_damage=350,
        max_indirect_damage=IndirectDamage(distance=1, damage=300),
        min_indirect_damage=IndirectDamage(distance=3, damage=50),
        damage_type=[DamageTypes.tank_shells, DamageTypes.common_explosive],
        reload_speed=3.5,
        magazine_size=4,
        ammunition_pool=96,
        min_cone_of_fire=0.2,
        max_cone_of_fire=0.35,
        bloom_per_shot=0.05,
    )
)

TITAN_150_AP = Weapon(
    name=WeaponName.TITAN_150_AP,
    color=WeaponColor.TITAN_150_AP,
    properties=WeaponProperties(
        cert_cost=875,
        dc_cost=599,
        empire=Empire.TR,
        can_use=[VehiculeName.PROWLER],
        weapon_type=WeaponType.ANTI_VEHICULE,
        fire_rate=300,
        muzzle_velocity=225,
        effective_range=EffectiveRange.VERY_LONG,
        fire_modes=[FireMode.SEMI_AUTOMATIC],
        max_damage=350,
        min_damage=350,
        max_indirect_damage=IndirectDamage(distance=1, damage=300),
        min_indirect_damage=IndirectDamage(distance=3, damage=50),
        damage_type=[DamageTypes.tank_shells, DamageTypes.common_explosive],
        reload_speed=3.5,
        magazine_size=4,
        ammunition_pool=96,
        min_cone_of_fire=0.2,
        max_cone_of_fire=0.35,
        bloom_per_shot=0.05,
    )
)

TITAN_150_HESH = Weapon(
    name=WeaponName.TITAN_150_HESH,
    color=WeaponColor.TITAN_150_HESH,
    properties=WeaponProperties(
        cert_cost=875,
        dc_cost=599,
        empire=Empire.TR,
        can_use=[VehiculeName.PROWLER],
        weapon_type=WeaponType.ANTI_VEHICULE,
        fire_rate=300,
        muzzle_velocity=225,
        effective_range=EffectiveRange.VERY_LONG,
        fire_modes=[FireMode.SEMI_AUTOMATIC],
        max_damage=350,
        min_damage=350,
        max_indirect_damage=IndirectDamage(distance=1, damage=300),
        min_indirect_damage=IndirectDamage(distance=3, damage=50),
        damage_type=[DamageTypes.tank_shells, DamageTypes.common_explosive],
        reload_speed=3.5,
        magazine_size=4,
        ammunition_pool=96,
        min_cone_of_fire=0.2,
        max_cone_of_fire=0.35,
        bloom_per_shot=0.05,
    )
)

JGX12 = Weapon(
    name=WeaponName.JGX12,
    color=WeaponColor.JGX12,
    properties=WeaponProperties(
        cert_cost=875,
        dc_cost=599,
        empire=Empire.TR,
        can_use=[VehiculeName.PROWLER],
        weapon_type=WeaponType.ANTI_VEHICULE,
        fire_rate=300,
        muzzle_velocity=225,
        effective_range=EffectiveRange.VERY_LONG,
        fire_modes=[FireMode.SEMI_AUTOMATIC],
        max_damage=350,
        min_damage=350,
        max_indirect_damage=IndirectDamage(distance=1, damage=300),
        min_indirect_damage=IndirectDamage(distance=3, damage=50),
        damage_type=[DamageTypes.tank_shells, DamageTypes.common_explosive],
        reload_speed=3.5,
        magazine_size=4,
        ammunition_pool=96,
        min_cone_of_fire=0.2,
        max_cone_of_fire=0.35,
        bloom_per_shot=0.05,
    )
)

SUPERNOVA_PC = Weapon(
    name=WeaponName.SUPERNOVA_PC,
    color=WeaponColor.SUPERNOVA_PC,
    properties=WeaponProperties(
        cert_cost=875,
        dc_cost=599,
        empire=Empire.TR,
        can_use=[VehiculeName.PROWLER],
        weapon_type=WeaponType.ANTI_VEHICULE,
        fire_rate=300,
        muzzle_velocity=225,
        effective_range=EffectiveRange.VERY_LONG,
        fire_modes=[FireMode.SEMI_AUTOMATIC],
        max_damage=350,
        min_damage=350,
        max_indirect_damage=IndirectDamage(distance=1, damage=300),
        min_indirect_damage=IndirectDamage(distance=3, damage=50),
        damage_type=[DamageTypes.tank_shells, DamageTypes.common_explosive],
        reload_speed=3.5,
        magazine_size=4,
        ammunition_pool=96,
        min_cone_of_fire=0.2,
        max_cone_of_fire=0.35,
        bloom_per_shot=0.05,
    )
)

SUPERNOVA_FPC = Weapon(
    name=WeaponName.SUPERNOVA_FPC,
    color=WeaponColor.SUPERNOVA_FPC,
    properties=WeaponProperties(
        cert_cost=875,
        dc_cost=599,
        empire=Empire.TR,
        can_use=[VehiculeName.PROWLER],
        weapon_type=WeaponType.ANTI_VEHICULE,
        fire_rate=300,
        muzzle_velocity=225,
        effective_range=EffectiveRange.VERY_LONG,
        fire_modes=[FireMode.SEMI_AUTOMATIC],
        max_damage=350,
        min_damage=350,
        max_indirect_damage=IndirectDamage(distance=1, damage=300),
        min_indirect_damage=IndirectDamage(distance=3, damage=50),
        damage_type=[DamageTypes.tank_shells, DamageTypes.common_explosive],
        reload_speed=3.5,
        magazine_size=4,
        ammunition_pool=96,
        min_cone_of_fire=0.2,
        max_cone_of_fire=0.35,
        bloom_per_shot=0.05,
    )
)

SUPERNOVA_VPC = Weapon(
    name=WeaponName.SUPERNOVA_VPC,
    color=WeaponColor.SUPERNOVA_VPC,
    properties=WeaponProperties(
        cert_cost=875,
        dc_cost=599,
        empire=Empire.TR,
        can_use=[VehiculeName.PROWLER],
        weapon_type=WeaponType.ANTI_VEHICULE,
        fire_rate=300,
        muzzle_velocity=225,
        effective_range=EffectiveRange.VERY_LONG,
        fire_modes=[FireMode.SEMI_AUTOMATIC],
        max_damage=350,
        min_damage=350,
        max_indirect_damage=IndirectDamage(distance=1, damage=300),
        min_indirect_damage=IndirectDamage(distance=3, damage=50),
        damage_type=[DamageTypes.tank_shells, DamageTypes.common_explosive],
        reload_speed=3.5,
        magazine_size=4,
        ammunition_pool=96,
        min_cone_of_fire=0.2,
        max_cone_of_fire=0.35,
        bloom_per_shot=0.05,
    )
)

PERIHELION_VXC = Weapon(
    name=WeaponName.PERIHELION_VXC,
    color=WeaponColor.PERIHELION_VXC,
    properties=WeaponProperties(
        cert_cost=875,
        dc_cost=599,
        empire=Empire.TR,
        can_use=[VehiculeName.PROWLER],
        weapon_type=WeaponType.ANTI_VEHICULE,
        fire_rate=300,
        muzzle_velocity=225,
        effective_range=EffectiveRange.VERY_LONG,
        fire_modes=[FireMode.SEMI_AUTOMATIC],
        max_damage=350,
        min_damage=350,
        max_indirect_damage=IndirectDamage(distance=1, damage=300),
        min_indirect_damage=IndirectDamage(distance=3, damage=50),
        damage_type=[DamageTypes.tank_shells, DamageTypes.common_explosive],
        reload_speed=3.5,
        magazine_size=4,
        ammunition_pool=96,
        min_cone_of_fire=0.2,
        max_cone_of_fire=0.35,
        bloom_per_shot=0.05,
    )
)
