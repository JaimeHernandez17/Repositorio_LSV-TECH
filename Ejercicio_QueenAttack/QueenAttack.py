f = open('file.txt', 'r')
lines = f.readlines()
n = 0
i = 0
n_blocks = 0
pos_y_queen = 0
pos_x_queen = 0
pos_blocks = []
tablero = []
count_moves = 0


def QueenAttack(nxn, y_queen, x_queen, coor_blocks):
    global count_moves
    fx = x_queen
    fy = y_queen
    for i in range(len(coor_blocks)):
        if coor_blocks[i][0] == y_queen and coor_blocks[i][1] == x_queen:
            print('Bad file')
            exit()

    for i in range(nxn):
        vec = []
        for j in range(nxn):
            vec.append(0)
        tablero.append(vec)

    tablero[x_queen - 1][y_queen - 1] = 'Q'
    for coors in coor_blocks:
        tablero[coors[1] - 1][coors[0] - 1] = 'X'

    # up
    for i in range(nxn):
        if x_queen - 1 > 0 and tablero[x_queen - 2][y_queen - 1] == 0:
            count_moves += 1
            x_queen = x_queen - 1
        else:
            break
    x_queen = fx

    # down
    for i in range(nxn):
        if x_queen - 1 < nxn - 1 and tablero[x_queen][y_queen - 1] == 0:
            count_moves += 1
            x_queen = x_queen + 1
        else:
            break
    x_queen = fx

    # left
    for i in range(nxn):
        if y_queen - 1 > 0 and tablero[x_queen - 1][y_queen - 2] == 0:
            count_moves += 1
            y_queen = y_queen - 1
        else:
            break
    y_queen = fy

    # right
    for i in range(nxn):
        if y_queen - 1 < nxn - 1 and tablero[x_queen - 1][y_queen] == 0:
            count_moves += 1
            y_queen = y_queen + 1
        else:
            break
    y_queen = fy

    # diag_up_left
    for i in range(nxn):

        if (x_queen - 1 > 0 and y_queen - 1 > 0) and tablero[x_queen - 2][y_queen - 2] == 0:
            count_moves += 1
            y_queen = y_queen - 1
            x_queen = x_queen - 1
        else:
            break
    y_queen = fy
    x_queen = fx

    # diag_up_right
    for i in range(nxn):

        if (x_queen - 1 > 0 and y_queen - 1 < nxn - 1) and tablero[x_queen - 2][y_queen] == 0:
            count_moves += 1
            y_queen = y_queen + 1
            x_queen = x_queen - 1
        else:
            break
    y_queen = fy
    x_queen = fx

    # diag_down_left
    for i in range(nxn):

        if (x_queen - 1 < nxn - 1 and y_queen - 1 > 0) and tablero[x_queen][y_queen - 2] == 0:
            count_moves += 1
            y_queen = y_queen - 1
            x_queen = x_queen + 1
        else:
            break
    y_queen = fy
    x_queen = fx

    # diag_down_right
    for i in range(nxn):

        if (x_queen - 1 < nxn - 1 and y_queen - 1 < nxn - 1) and tablero[x_queen][y_queen] == 0:
            count_moves += 1
            y_queen = y_queen + 1
            x_queen = x_queen + 1
        else:
            break
    y_queen = fy
    x_queen = fx

    for tabla in tablero:
        print(tabla)

    print(count_moves)


def CountLines():
    count = 0
    for i in lines:
        count += 1
    return count


if CountLines() < 2:
    exit()
else:

    for line in lines:
        if (not line.split(' ')[0].isdigit()) or (not line.split(' ')[1].replace('\n', '').isdigit()):
            print('Bad file')
            exit()

        elif i == 0:
            n = int(line.split(' ')[0])
            n_blocks = int(line.split(' ')[1])
            if CountLines() != n_blocks + 2:
                print('Bad file')
                exit()
            i += 1

        elif i == 1:
            pos_y_queen = int(line.split(' ')[0])
            pos_x_queen = int(line.split(' ')[1])
            if (pos_y_queen > n or pos_y_queen <= 0) or (pos_x_queen > n or pos_x_queen <= 0):
                print('Bad file')
                exit()
            i += 1

        elif i > 1:
            temp = []
            pos_y_block = int(line.split(' ')[0])
            pos_x_block = int(line.split(' ')[1])
            if (pos_y_block > n or pos_y_block < 0) or (pos_x_block > n or pos_x_block < 0):
                print('Bad file')
                exit()
            temp.append(pos_y_block)
            temp.append(pos_x_block)
            pos_blocks.append(temp)
            i += 1

QueenAttack(n, pos_y_queen, pos_x_queen, pos_blocks)

f.close()
