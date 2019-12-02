import math


def day1():
    with open("inputs/day_1.txt") as file:
        total_amount = 0

        for line in file:
            fuel_addition = get_fuel(int(line), 0)
            total_amount += fuel_addition

        print(total_amount)


def get_fuel(mass, total_fuel):
    required_fuel = mass / 3
    required_fuel = math.floor(required_fuel)
    required_fuel -= 2

    if required_fuel <= 0:
        return total_fuel
    else:
        total_fuel += required_fuel
        return get_fuel(required_fuel, total_fuel)


if __name__ == "__main__":
    day1()
