import numpy as np
import matplotlib.pyplot as plt
from weapons import C75_VIPER, L100_PYTHON_AP, L2_100_KINGSNAKE, L100_PYTHON_HEAT, L100_PYTHON_HESH, PERIHELION_L_VXC, SKYGUARD, JGX11, P2_120_AP, P2_120_HEAT, P2_120_HESH, P4_120_KINGSNAKE, TITAN_150_HEAT, TITAN_150_AP, TITAN_150_HESH, JGX12, SUPERNOVA_PC, SUPERNOVA_FPC, SUPERNOVA_VPC, PERIHELION_VXC
from linghtning import LIGHTNING
from mbt import PROWLER
from plots import plot_damage_over_time, plot_dispersion, plot_health_to_compare


LIGHT_WEAPONS = [C75_VIPER,
                 L100_PYTHON_AP,
                 L2_100_KINGSNAKE,
                 L100_PYTHON_HESH,
                 PERIHELION_L_VXC,
                 JGX11]

HEAVY_WEAPONS = [P2_120_AP,
                 P2_120_HEAT,
                 P2_120_HESH,
                 P4_120_KINGSNAKE,
                 TITAN_150_HEAT,
                 TITAN_150_AP,
                 TITAN_150_HESH,
                 JGX12,
                 SUPERNOVA_PC,
                 SUPERNOVA_FPC,
                 SUPERNOVA_VPC,
                 PERIHELION_VXC,]

ARERIAL_WEAPONS = [SKYGUARD]

VEHICULES = [LIGHTNING,
             PROWLER]


def main():
    step = 0.01
    duration = 20
    t = np.arange(-2, duration, step)
    start = 0
    fig, ax = plt.subplots()
    ax.set_xlabel("seconds (s)")
    ax.set_ylabel("damage")
    plt.title("Weapons comparison")

    plot_health_to_compare(VEHICULES, t)

    plot_damage_over_time(HEAVY_WEAPONS, t, ax, step, start=start)

    plt.legend()
    plt.show()

    number_of_shots = 200
    plot_dispersion(HEAVY_WEAPONS, number_of_shots, separate=False)

if __name__ == "__main__":
    main()
