def day2_2():
    with open("inputs/day_2.txt", "r") as file:
        raw_data = file.read()
        splitted_data = raw_data.split(",")

        for index_noun in range(0, 100):
            splitted_data[1] = str(index_noun)
            for index_verb in range(0, 100):
                splitted_data[2] = str(index_verb)

                if calculate_output(splitted_data) == 19690720:
                    print("Noun: {0}, Verb: {1}".format(index_noun, index_verb))
                    break


def calculate_output(splitted_data):
    splitted_data_copy = list(splitted_data)
    for index in range(0, len(splitted_data_copy), 4):
        try:
            opcode = int(splitted_data_copy[index])
            if opcode == 99:
                return int(splitted_data_copy[0])

            position1 = int(splitted_data_copy[index + 1])
            position2 = int(splitted_data_copy[index + 2])
            destination = int(splitted_data_copy[index + 3])

            value1 = int(splitted_data_copy[position1])
            value2 = int(splitted_data_copy[position2])

            if opcode == 1:
                addition = value1 + value2
                splitted_data_copy[destination] = str(addition)

            if opcode == 2:
                multiplication = value1 * value2
                splitted_data_copy[destination] = str(multiplication)

        except IndexError:
            pass


if __name__ == "__main__":
    day2_2()
