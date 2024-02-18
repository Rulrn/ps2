from dataclasses import dataclass
from enum import Enum

from empires import Empire
from vehicules import VehiculeName

class WeaponType(Enum):
    ANTI_VEHICULE = "Anti-Vehicule"
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


class WeaponColor(Enum):
    C75_VIPER = "green"
    L100_PYTHON_HEAT = "red"
    L100_PYTHON_AP = "orange"
    L100_PYTHON_HESH = "black"
    SKYGUARD = "black"
    L2_100_KINGSNAKE = "blue"
    JGX11 = "black"
    PERIHELION_L_VXC = "black"

@dataclass
class Weapon:
    name: WeaponName
    color: WeaponColor
    properties: WeaponProperties


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
