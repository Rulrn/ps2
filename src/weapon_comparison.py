import numpy as np
import matplotlib.pyplot as plt
from dataclasses import dataclass
from enum import Enum
import random

TYPES = {
    "light": "light",
    "heavy": "heavy",
    "transport": "transport",
    "mbt": "mbt",
    "patrol": "patrol_boat",
}

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

class Empire(Enum):
    ALL = "Common Pool"
    TR = "Terran Republic"
    NC = "New Republic"
    VS = "Vanu Sovereignty"
    NSO = "Nanite Systems Operative"

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

LIGHT_WEAPONS = [C75_VIPER,
                 L100_PYTHON_AP,
                 L2_100_KINGSNAKE,
                 L100_PYTHON_HESH,
                 PERIHELION_L_VXC,
                 JGX11]

ARERIAL_WEAPONS = [SKYGUARD]

VEHICULES = [LIGHTNING]

def get_time_per_fire(fire_rate, _round=2):
    return round(60 / fire_rate, _round)


def plot_health_to_compare(vehicules: list[Vehicule], x_axis):
    for vehicule in vehicules:
        plt.hlines(y=vehicule.properties.health, xmin=x_axis.min(), xmax=x_axis.max(), colors=vehicule.color.value, linestyles='--', lw=2, label=vehicule.name.value)

def plot_damage_over_time(weapons: list[Weapon], x_axis, _ax, step, start=0):
    for weapon in weapons:
        y = np.full(x_axis.shape, 0, dtype=np.float64)

        number_of_ammunition = weapon.properties.ammunition_pool
        rounds = weapon.properties.magazine_size
        cnt = 10000
        fire_counter = 0
        time_per_rounds = get_time_per_fire(weapon.properties.fire_rate)

        is_reloading = False

        for idx in range(len(x_axis)):
            time = round(x_axis[idx], 3)

            if not time >= start:
                continue

            if number_of_ammunition <= 0:
                print(f"No more ammunition : {weapon.name.value} at {time}")
                break

            if rounds == 0:
                is_reloading = True
                cnt = weapon.properties.reload_speed
                rounds = weapon.properties.magazine_size

            if is_reloading:
                cnt -= step

            if cnt <= (step / 10):
                is_reloading = False
                cnt = 1000
                fire_counter = 0

            is_fire = round(fire_counter / time_per_rounds, 5).is_integer()

            # print(f"time: {time}, {cnt=}, {fire_counter=}, {fire_counter % time_per_rounds=}, {rounds=}")

            if is_fire and not is_reloading:
                # print("Shots fired !")
                y[idx:-1] += (weapon.properties.max_damage * 1.5)  # TODO revoir la logique
                rounds -= 1
                number_of_ammunition -= 1

            fire_counter = round(fire_counter + step, 3)
        _ax.plot(x_axis, y, label=weapon.name.value)


def plot_dispersion(weapons, n_shots, worst_case=True, separate=False):
    fig, ax = plt.subplots()
    plt.title("Dispersion")
    ax.set_xlabel("Dispersion x")
    ax.set_ylabel("Dispersion y")

    max_dispersion = 2

    for weapon in weapons:

        color = weapon.color.value

        label = f"{weapon.name.value} - {weapon.properties.empire.name}"

        if not weapon.properties.max_cone_of_fire:
            plt.scatter(0, 0, label=label, s=20, color=color)
            if separate:
                ax.set_xlim([-max_dispersion, max_dispersion])
                ax.set_ylim([-max_dispersion, max_dispersion])
                plt.legend()
                plt.show()
            continue

        _min = -weapon.properties.max_cone_of_fire
        _max = weapon.properties.max_cone_of_fire
        circle = plt.Circle((0, 0), _max, color=color, fill=False)
        ax.add_patch(circle)

        radius_dispersion = np.random.uniform(low=_min, high=_max, size=n_shots)
        random_angle = np.random.uniform(low=-180, high=180, size=n_shots)
        x_pos = radius_dispersion * np.cos(random_angle)
        y_pos = radius_dispersion * np.sin(random_angle)

        plt.scatter(x_pos, y_pos, label=label + f" - {_max}", s=20, alpha=0.5, color=color)

        if separate:
            ax.set_xlim([-max_dispersion, max_dispersion])
            ax.set_ylim([-max_dispersion, max_dispersion])
            plt.legend()
            plt.show()

    if not separate:
        ax.set_xlim([-max_dispersion, max_dispersion])
        ax.set_ylim([-max_dispersion, max_dispersion])
        plt.legend()
        plt.show()

def main():
    step = 0.01
    duration = 120
    t = np.arange(-2, duration, step)
    start = 0
    fig, ax = plt.subplots()
    ax.set_xlabel("seconds (s)")
    ax.set_ylabel("damage")
    plt.title("Weapons comparison")

    plot_health_to_compare(VEHICULES, t)

    plot_damage_over_time(LIGHT_WEAPONS, t, ax, step, start=start)

    plt.legend()
    plt.show()

    number_of_shots = 200
    plot_dispersion(LIGHT_WEAPONS, number_of_shots, separate=False)

if __name__ == "__main__":
    main()
