
from weapons import Vehicule, VehiculeProperties, VehiculeType, VehiculeName, VehiculeColor, DirectionalArmor, Resistances
from weapons import P2_120_AP, P2_120_HEAT, P2_120_HESH, P4_120_KINGSNAKE, TITAN_150_HEAT, TITAN_150_AP, TITAN_150_HESH, JGX12, SUPERNOVA_PC, SUPERNOVA_FPC, SUPERNOVA_VPC, PERIHELION_VXC
from empires import Empire


_MBT_VEHICULE_TEMPLATE = Vehicule(
    name=None,
    color=None,
    directionnal_armor=DirectionalArmor(
        front=0.0,
        top=0.0,
        side=-15.0,
        rear=-50.0,
        bottom=-100.0
    ),
    properties=None,
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

# Prowler
PROWLER_PROPERTIES = VehiculeProperties(
    vtype=VehiculeType.HEAVY,
    empire=Empire.TR,
    cost=450,
    health=5000,
    decay=5,
    primary_weapon=[P2_120_HEAT,
                    P2_120_AP,
                    P2_120_HESH,
                    P4_120_KINGSNAKE],
    secondary_weapon=[],  # TODO complete
    empire_specific=[Empire.TR]
)

PROWLER = _MBT_VEHICULE_TEMPLATE
PROWLER.name = VehiculeName.PROWLER
PROWLER.color = VehiculeColor.PROWLER
PROWLER.properties = PROWLER_PROPERTIES

# Vanguard
PROWLER_PROPERTIES = VehiculeProperties(
    vtype=VehiculeType.HEAVY,
    empire=Empire.NC,
    cost=450,
    health=6000,
    decay=5,
    # TODO complete
    primary_weapon=[TITAN_150_HEAT,
                    TITAN_150_AP,
                    TITAN_150_HESH,
                    JGX12],
    secondary_weapon=[],  # TODO complete
    empire_specific=[Empire.TR]
)

PROWLER = _MBT_VEHICULE_TEMPLATE
PROWLER.name = VehiculeName.PROWLER
PROWLER.color = VehiculeColor.PROWLER
PROWLER.properties = PROWLER_PROPERTIES

# Magrider
PROWLER_PROPERTIES = VehiculeProperties(
    vtype=VehiculeType.HEAVY,
    empire=Empire.TR,
    cost=450,
    health=5000,
    decay=5,
    primary_weapon=[SUPERNOVA_PC,
                    SUPERNOVA_FPC,
                    SUPERNOVA_VPC,
                    PERIHELION_VXC],
    secondary_weapon=[],  # TODO complete
    empire_specific=[Empire.TR]
)

PROWLER = _MBT_VEHICULE_TEMPLATE
PROWLER.name = VehiculeName.PROWLER
PROWLER.color = VehiculeColor.PROWLER
PROWLER.properties = PROWLER_PROPERTIES
