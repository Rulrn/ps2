
from weapons import Vehicule, VehiculeProperties, VehiculeType, VehiculeName, VehiculeColor, DirectionalArmor, Resistances
from weapons import C75_VIPER, L100_PYTHON_AP, L100_PYTHON_HEAT, L100_PYTHON_HESH, L2_100_KINGSNAKE, PERIHELION_L_VXC, SKYGUARD, JGX11
from empires import Empire

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
    secondary_weapon=[None],
    empire_specific=[  # TODO complete
        L2_100_KINGSNAKE,
        JGX11,
        PERIHELION_L_VXC,
        # NCS
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
