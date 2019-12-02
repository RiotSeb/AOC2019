def day2_1():
    with open("inputs/day_2.txt", "r") as file:
        raw_data = file.read()
        splitted_data = raw_data.split(",")
        print(calculate_output(splitted_data))


def calculate_output(splitted_data):
    for index in range(0, len(splitted_data), 4):
        opcode = int(splitted_data[index])
        if opcode == 99:
            return splitted_data[0]

        position1 = int(splitted_data[index + 1])
        position2 = int(splitted_data[index + 2])
        destination = int(splitted_data[index + 3])

        value1 = int(splitted_data[position1])
        value2 = int(splitted_data[position2])

        if opcode == 1:
            addition = value1 + value2
            splitted_data[destination] = str(addition)

        if opcode == 2:
            multiplication = value1 * value2
            splitted_data[destination] = str(multiplication)


if __name__ == "__main__":
    day2_1()
