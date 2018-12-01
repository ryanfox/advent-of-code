import sys

directions = 'R3, L5, R2, L2, R1, L3, R1, R3, L4, R3, L1, L1, R1, L3, R2, L3, L2, R1, R1, L1, R4, L1, L4, R3, L2, L2, R1, L1, R5, R4, R2, L5, L2, R5, R5, L2, R3, R1, R1, L3, R1, L4, L4, L190, L5, L2, R4, L5, R4, R5, L4, R1, R2, L5, R50, L2, R1, R73, R1, L2, R191, R2, L4, R1, L5, L5, R5, L3, L5, L4, R4, R5, L4, R4, R4, R5, L2, L5, R3, L4, L4, L5, R2, R2, R2, R4, L3, R4, R5, L3, R5, L2, R3, L1, R2, R2, L3, L1, R5, L3, L5, R2, R4, R1, L1, L5, R3, R2, L3, L4, L5, L1, R3, L5, L2, R2, L3, L4, L1, R1, R4, R2, R2, R4, R2, R2, L3, L3, L4, R4, L4, L4, R1, L4, L4, R1, L2, R5, R2, R3, R3, L2, L5, R3, L3, R5, L2, R3, R2, L4, L3, L1, R2, L2, L3, L5, R3, L1, L3, L4, L3'

pointing = 0  # 0, 1, 2, 3 == N, E, S, W
position = (0, 0)  # origin

directions = directions.replace(',', '').split()


def update(pointing, distance, position):
    if pointing == 0:
        return position[0] + distance, position[1]
    elif pointing == 1:
        return position[0], position[1] + distance
    elif pointing == 2:
        return position[0] - distance, position[1]
    elif pointing == 3:
        return position[0], position[1] - distance


def update2(pointing, distance, position):
        if pointing == 0:
            return distance - 1, (position[0] + 1, position[1])
        elif pointing == 1:
            return distance - 1, (position[0], position[1] + 1)
        elif pointing == 2:
            return distance - 1, (position[0] - 1, position[1])
        elif pointing == 3:
            return distance - 1, (position[0], position[1] - 1)


# part 1
for direction in directions:
    if direction[0] == 'L':
        pointing = (pointing - 1) % 4

    elif direction[0] == 'R':
        pointing = (pointing + 1) % 4
    else:
        raise Exception

    distance = int(direction[1:])
    position = update(pointing, distance, position)

print(sum(abs(coordinate) for coordinate in position))

# part 2
visited_positions = set()

pointing = 0
position = (0, 0)

for direction in directions:
    if direction[0] == 'L':
        pointing = (pointing - 1) % 4

    elif direction[0] == 'R':
        pointing = (pointing + 1) % 4
    else:
        raise Exception

    distance = int(direction[1:])

    while distance > 0:
        distance, position = update2(pointing, distance, position)

        if position in visited_positions:
            print(sum(abs(coordinate) for coordinate in position))
            sys.exit(0)

        visited_positions.add(position)
