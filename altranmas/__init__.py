STARTING_COORDINATES = (0, 0)
INPUT_FILE = '../Hal_input.txt'


def get_next_coordinate(current_coordinate, move):
    new_x = current_coordinate[0]
    new_y = current_coordinate[1]
    if move == '>':
        new_x += 1
    elif move == '<':
        new_x -= 1
    elif move == '^':
        new_y += 1
    else:
        new_y -= 1
    return new_x, new_y


def calculate_houses_visited(input_string):
    current_coordinates = STARTING_COORDINATES
    visited_coordinates = {current_coordinates}
    for move in input_string:
        current_coordinates = get_next_coordinate(current_coordinates, move)
        visited_coordinates.add(current_coordinates)
    print('Unique locations: %i' % len(visited_coordinates))


def calculate_houses_visited_2(input_string):
    santa_coordinates = STARTING_COORDINATES
    neil_coordinates = STARTING_COORDINATES
    visited_coordinates = {santa_coordinates}
    santa_turn = True
    for move in input_string:
        if santa_turn:
            santa_coordinates = get_next_coordinate(santa_coordinates, move)
            visited_coordinates.add(santa_coordinates)
        else:
            neil_coordinates = get_next_coordinate(neil_coordinates, move)
            visited_coordinates.add(neil_coordinates)
        santa_turn = not santa_turn
    print('Unique locations: %i' % len(visited_coordinates))


def file_to_string(file_name):
    with open(file_name) as file:
        data = file.read()
    return data


if __name__ == '__main__':
    calculate_houses_visited(file_to_string(INPUT_FILE))
    calculate_houses_visited_2(file_to_string(INPUT_FILE))
