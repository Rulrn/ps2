import matplotlib.pyplot as plt
import numpy as np

from weapons import Weapon, Vehicule
from utils import get_time_per_fire

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
