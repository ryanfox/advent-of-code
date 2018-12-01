commands = '''RRLUDDLDUDUDUDRDDDRDDRLUUUDRUDURURURLRDDULLLDRRRRULDDRDDURDLURLURRUULRURDDDDLDDRRLDUDUUDURURDLDRRURDLLLDLLRUDRLDDRUULLLLLRRLDUDLUUDRUULLRLLLRLUURDLDLLDDRULDLUURRURLUUURLLDDULRDULULRULDDLRDDUUDLRRURLLURURLDDLURRLUURRRRLDRDLDUDRUDDRULLDUDDLRRLUUUUUDDLLDRLURDDRLLUDULDRDDLLUURUUUURDRLRLLULUULULLRRDLULRUDURDLRLRDDDRULLUULRURULLLUDUURUUUURUULDURDRRRULRLULDLRRULULUUDDDRDURLLURLLDUUUUDULRDLRDUUDDLDUDRLLRLRRRLULUDDDURLRRURUDDDRDRDRLLRDRDLDDRRDRDLLRLLLRRULRDDURRDUDRURDLDULLRRLURLRLLDURRRLLDRRURRRUULDRLDUULRDLDLURUDLLDLLUUDDDUUUDRL
DLRRDRRDDRRDURLUDDDDDULDDLLDRLURDDDDDDRDDDRDDDLLRRULLLRUDULLDURULRRDLURURUDRUURDRLUURRUDRUULUURULULDDLLDDRLDUDDRDRDDUULDULDDLUDUDDUDLULLUDLLLLLRRRUURLUUUULRURULUDDULLLRLRDRUUULULRUUUULRDLLDLDRDRDRDRRUUURULDUUDLDRDRURRUDDRLDULDDRULRRRLRDDUUDRUDLDULDURRDUDDLULULLDULLLRRRDULLLRRURDUURULDRDURRURRRRDLDRRUDDLLLDRDRDRURLUURURRUUURRUDLDDULDRDRRURDLUULDDUUUURLRUULRUURLUUUDLUDRLURUDLDLDLURUURLDURDDDDRURULLULLDRDLLRRLDLRRRDURDULLLDLRLDR
URURLLDRDLULULRDRRDDUUUDDRDUURULLULDRLUDLRUDDDLDRRLURLURUUDRLDUULDRDURRLLUDLDURRRRLURLDDRULRLDULDDRRLURDDRLUDDULUDULRLDULDLDUDRLLDDRRRDULLDLRRLDRLURLUULDDDDURULLDLLLDRRLRRLLRDDRDLDRURRUURLLDDDLRRRRRDLRRDRLDDDLULULRLUURULURUUDRULRLLRDLDULDRLLLDLRRRUDURLUURRUDURLDDDRDRURURRLRRLDDRURULDRUURRLULDLUDUULDLUULUDURRDDRLLLRLRRLUUURRDRUULLLRUUURLLDDRDRULDULURRDRURLRRLRDURRURRDLDUDRURUULULDDUDUULDRDURRRDLURRLRLDUDRDULLURLRRUDLUDRRRULRURDUDDDURLRULRRUDUUDDLLLURLLRLLDRDUURDDLUDLURDRRDLLRLURRUURRLDUUUUDUD
DRRDRRRLDDLDUDRDLRUUDRDUDRRDUDRDURRDDRLLURUUDRLRDDULLUULRUUDDRLDLRULDLRLDUDULUULLLRDLURDRDURURDUDUDDDRRLRRLLRULLLLRDRDLRRDDDLULDLLUUULRDURRULDDUDDDURRDRDRDRULRRRDRUDLLDDDRULRRLUDRDLDLDDDLRLRLRLDULRLLRLRDUUULLRRDLLRDULURRLDUDDULDDRLUDLULLRLDUDLULRDURLRULLRRDRDDLUULUUUULDRLLDRDLUDURRLLDURLLDDLLUULLDURULULDLUUDLRURRRULUDRLDRDURLDUDDULRDRRDDRLRRDDRUDRURULDRRLUURUDULDDDLRRRRDRRRLLURUURLRLULUULLRLRDLRRLLUULLDURDLULURDLRUUDUUURURUURDDRLULUUULRDRDRUUDDDRDRL
RLRUDDUUDDDDRRLRUUDLLDRUUUDRRDLDRLRLLDRLUDDURDLDUDRRUURULLRRLUULLUDRDRUDDULRLLUDLULRLRRUUDLDLRDDDRDDDUDLULDLRRLUDUDDRRRRDRDRUUDDURLRDLLDLDLRRDURULDRLRRURULRDDLLLRULLRUUUDLDUURDUUDDRRRDDRLDDRULRRRDRRLUDDDRUURRDRRDURDRUDRRDLUDDURRLUDUDLLRUURLRLLLDDURUDLDRLRLLDLLULLDRULUURLDDULDDRDDDURULLDRDDLURRDDRRRLDLRLRRLLDLLLRDUDDULRLUDDUULUDLDDDULULDLRDDLDLLLDUUDLRRLRDRRUUUURLDLRRLDULURLDRDURDDRURLDLDULURRRLRUDLDURDLLUDULDDU'''

commands = commands.split()

keypad = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
position = (1, 1)


def move(direction, position):
    if direction == 'U':
        if position[0] == 0:
            return position
        return position[0] - 1, position[1]

    elif direction == 'R':
        if position[1] == 2:
            return position
        return position[0], position[1] + 1

    elif direction == 'D':
        if position[0] == 2:
            return position
        return position[0] + 1, position[1]

    elif direction == 'L':
        if position[1] == 0:
            return position
        return position[0], position[1] - 1


def allowed_move(direction, position):
    if direction == 'U':
        # row 0
        if position[0] == 0:
            return False

        # row 1
        if position[0] == 1:
            if position[1] == 1:
                return True
            return False

        # row 2
        if position[0] == 2:
            if position[1] in (1, 2, 3):
                return True
            return False

        # rows 3 and 4 can always move up
        return True

    elif direction == 'R':
        return position[1] < len(keypad[position[0]]) - 1

    elif direction == 'D':
        # row 4
        if position[0] == 4:
            return False

        # row 3
        if position[0] == 3:
            if position[1] == 1:
                return True
            return False

        # row 2
        if position[0] == 2:
            if position[1] in (1, 2, 3):
                return True
            return False

        # rows 1 and 0 can always move down
        return True

    elif direction == 'L':
        return position[1] != 0


def move2(direction, position):
    if not allowed_move(direction, position):
        return position

    if direction == 'U':
        row = position[0] - 1

        if row == 0:
            col = 0
        if row == 1:
            col = position[1] - 1
        if row in (2, 3):
            col = position[1] + 1

        return row, col

    elif direction == 'R':
        return position[0], position[1] + 1

    elif direction == 'D':
        row = position[0] + 1

        if row == 4:
            col = 0
        if row == 3:
            col = position[1] - 1
        if row in (1, 2):
            col = position[1] + 1

        return row, col

    elif direction == 'L':
        return position[0], position[1] - 1

# part 1
code = ''
for command in commands:
    for direction in command:
        position = move(direction, position)

    code += str(keypad[position[0]][position[1]])

print(code)


# part 2
keypad = [[1], [2, 3, 4], [5, 6, 7, 8, 9], ['A', 'B', 'C'], ['D']]
position = (2, 0)

code = ''
for command in commands:
    for direction in command:
        position = move2(direction, position)

    code += str(keypad[position[0]][position[1]])

print(code)
