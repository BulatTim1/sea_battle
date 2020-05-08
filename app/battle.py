from copy import deepcopy


class Battle:
    def __init__(self, id1, id2):
        self.map1, self.map2 = [], []
        self.map12 = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0] for _ in range(10)]
        self.map21 = deepcopy(self.map12)
        self.map11 = deepcopy(self.map12)
        self.map22 = deepcopy(self.map12)
        self.turn1 = id1
        self.turn2 = id2
        self.turn = 1
        self.prepare = True
        self.ll1 = [0, 0, 0, 0]
        self.ll2 = [0, 0, 0, 0]

    def destroy(self, mapb, turn):
        if turn == 1:
            for j in range(1, mapb[0]):
                self.map12[mapb[j][0] - 1][mapb[j][1] - 1] = 1
            x, y = mapb[1][0] - 1, mapb[1][1] - 1
            if mapb[0] == 1:
                if x == 0:
                    if y == 0:
                        self.map12[0][1] = 2
                        self.map12[1][1] = 2
                        self.map12[1][0] = 2
                    elif y == 9:
                        self.map12[1][9] = 2
                        self.map12[0][8] = 2
                        self.map12[1][8] = 2
                    else:
                        self.map12[0][y - 1] = 2
                        self.map12[0][y + 1] = 2
                        self.map12[1][y - 1] = 2
                        self.map12[1][y] = 2
                        self.map12[1][y + 1] = 2
                elif x == 9:
                    if y == 0:
                        self.map12[9][1] = 2
                        self.map12[8][1] = 2
                        self.map12[8][0] = 2
                    elif y == 9:
                        self.map12[9][8] = 2
                        self.map12[8][9] = 2
                        self.map12[8][8] = 2
                    else:
                        self.map12[9][y - 1] = 2
                        self.map12[9][y + 1] = 2
                        self.map12[8][y - 1] = 2
                        self.map12[8][y] = 2
                        self.map12[8][y + 1] = 2
                else:
                    if y == 0:
                        self.map12[x - 1][y] = 2
                        self.map12[x - 1][y + 1] = 2
                        self.map12[x][y + 1] = 2
                        self.map12[x + 1][y] = 2
                        self.map12[x + 1][y + 1] = 2
                    elif y == 9:
                        self.map12[x - 1][y - 1] = 2
                        self.map12[x - 1][y] = 2
                        self.map12[x][y - 1] = 2
                        self.map12[x + 1][y - 1] = 2
                        self.map12[x + 1][y] = 2
                    else:
                        self.map12[x - 1][y - 1] = 2
                        self.map12[x - 1][y] = 2
                        self.map12[x - 1][y + 1] = 2
                        self.map12[x][y - 1] = 2
                        self.map12[x][y + 1] = 2
                        self.map12[x + 1][y - 1] = 2
                        self.map12[x + 1][y] = 2
                        self.map12[x + 1][y + 1] = 2
            elif mapb[0] == 2 and mapb[2][0] - 1 == x:
                if x == 0:
                    if y == 0:
                        self.map12[0][2] = 2
                        self.map12[1][1] = 2
                        self.map12[1][2] = 2
                        self.map12[1][0] = 2
                    elif y == 8:
                        self.map12[1][9] = 2
                        self.map12[0][7] = 2
                        self.map12[1][8] = 2
                        self.map12[1][7] = 2
                    else:
                        self.map12[0][y - 1] = 2
                        self.map12[0][y + 2] = 2
                        self.map12[1][y - 1] = 2
                        self.map12[1][y] = 2
                        self.map12[1][y + 1] = 2
                        self.map12[1][y + 2] = 2
                elif x == 9:
                    if y == 0:
                        self.map12[9][2] = 2
                        self.map12[8][2] = 2
                        self.map12[8][1] = 2
                        self.map12[8][0] = 2
                    elif y == 8:
                        self.map12[9][7] = 2
                        self.map12[8][9] = 2
                        self.map12[8][8] = 2
                        self.map12[8][7] = 2
                    else:
                        self.map12[9][y - 1] = 2
                        self.map12[9][y + 2] = 2
                        self.map12[8][y - 1] = 2
                        self.map12[8][y] = 2
                        self.map12[8][y + 1] = 2
                        self.map12[8][y + 2] = 2
                else:
                    if y == 0:
                        self.map12[x - 1][0] = 2
                        self.map12[x - 1][1] = 2
                        self.map12[x - 1][2] = 2
                        self.map12[x][2] = 2
                        self.map12[x + 1][0] = 2
                        self.map12[x + 1][1] = 2
                        self.map12[x + 1][2] = 2
                    elif y == 8:
                        self.map12[x - 1][9] = 2
                        self.map12[x - 1][8] = 2
                        self.map12[x - 1][7] = 2
                        self.map12[x][7] = 2
                        self.map12[x + 1][9] = 2
                        self.map12[x + 1][8] = 2
                        self.map12[x + 1][7] = 2
                    else:
                        self.map12[x - 1][y] = 2
                        self.map12[x - 1][y - 1] = 2
                        self.map12[x - 1][y + 1] = 2
                        self.map12[x - 1][y + 2] = 2
                        self.map12[x][y + 2] = 2
                        self.map12[x][y - 1] = 2
                        self.map12[x + 1][y] = 2
                        self.map12[x + 1][y - 1] = 2
                        self.map12[x + 1][y + 1] = 2
                        self.map12[x + 1][y + 2] = 2
            elif mapb[0] == 2:
                if x == 0:
                    if y == 0:
                        self.map12[0][1] = 2
                        self.map12[1][1] = 2
                        self.map12[2][1] = 2
                        self.map12[2][0] = 2
                    elif y == 9:
                        self.map12[0][8] = 2
                        self.map12[1][8] = 2
                        self.map12[2][8] = 2
                        self.map12[2][9] = 2
                    else:
                        self.map12[0][y - 1] = 2
                        self.map12[0][y + 1] = 2
                        self.map12[1][y - 1] = 2
                        self.map12[2][y] = 2
                        self.map12[1][y + 1] = 2
                        self.map12[2][y + 1] = 2
                        self.map12[2][y - 1] = 2
                elif x == 8:
                    if y == 0:
                        self.map12[9][1] = 2
                        self.map12[8][1] = 2
                        self.map12[7][1] = 2
                        self.map12[7][0] = 2
                    elif y == 9:
                        self.map12[9][8] = 2
                        self.map12[8][8] = 2
                        self.map12[7][8] = 2
                        self.map12[7][9] = 2
                    else:
                        self.map12[9][y - 1] = 2
                        self.map12[9][y + 1] = 2
                        self.map12[8][y - 1] = 2
                        self.map12[8][y + 1] = 2
                        self.map12[7][y + 1] = 2
                        self.map12[7][y - 1] = 2
                        self.map12[7][y] = 2
                else:
                    if y == 0:
                        self.map12[x - 1][y] = 2
                        self.map12[x - 1][y + 1] = 2
                        self.map12[x][y + 1] = 2
                        self.map12[x + 1][y + 1] = 2
                        self.map12[x + 2][y] = 2
                        self.map12[x + 2][y + 1] = 2
                    elif y == 9:
                        self.map12[x - 1][y] = 2
                        self.map12[x - 1][y - 1] = 2
                        self.map12[x][y - 1] = 2
                        self.map12[x + 1][y - 1] = 2
                        self.map12[x + 2][y] = 2
                        self.map12[x + 2][y - 1] = 2
                    else:
                        self.map12[x - 1][y] = 2
                        self.map12[x - 1][y + 1] = 2
                        self.map12[x - 1][y - 1] = 2
                        self.map12[x][y + 1] = 2
                        self.map12[x][y - 1] = 2
                        self.map12[x + 1][y + 1] = 2
                        self.map12[x + 1][y - 1] = 2
                        self.map12[x + 2][y - 1] = 2
                        self.map12[x + 2][y] = 2
                        self.map12[x + 2][y + 1] = 2
            elif mapb[0] == 3 and mapb[2][0] - 1 == x:
                if x == 0:
                    if y == 0:
                        self.map12[0][3] = 2
                        self.map12[1][0] = 2
                        self.map12[1][1] = 2
                        self.map12[1][2] = 2
                        self.map12[1][3] = 2
                    elif y == 7:
                        self.map12[0][6] = 2
                        self.map12[1][6] = 2
                        self.map12[1][7] = 2
                        self.map12[1][8] = 2
                        self.map12[1][9] = 2
                    else:
                        self.map12[0][y - 1] = 2
                        self.map12[0][y + 3] = 2
                        self.map12[1][y - 1] = 2
                        self.map12[1][y + 1] = 2
                        self.map12[1][y] = 2
                        self.map12[1][y + 2] = 2
                        self.map12[1][y + 3] = 2
                elif x == 9:
                    if y == 0:
                        self.map12[9][3] = 2
                        self.map12[8][0] = 2
                        self.map12[8][1] = 2
                        self.map12[8][2] = 2
                        self.map12[8][3] = 2
                    elif y == 7:
                        self.map12[9][6] = 2
                        self.map12[8][6] = 2
                        self.map12[8][8] = 2
                        self.map12[8][7] = 2
                        self.map12[8][9] = 2
                    else:
                        self.map12[9][y - 1] = 2
                        self.map12[9][y + 3] = 2
                        self.map12[8][y - 1] = 2
                        self.map12[8][y + 1] = 2
                        self.map12[8][y + 2] = 2
                        self.map12[8][y + 3] = 2
                        self.map12[8][y] = 2
                else:
                    if y == 0:
                        self.map12[x - 1][y] = 2
                        self.map12[x - 1][y + 1] = 2
                        self.map12[x - 1][y + 2] = 2
                        self.map12[x - 1][y + 3] = 2
                        self.map12[x][y + 3] = 2
                        self.map12[x + 1][y] = 2
                        self.map12[x + 1][y + 1] = 2
                        self.map12[x + 1][y + 2] = 2
                        self.map12[x + 1][y + 3] = 2
                    elif y == 7:
                        self.map12[x - 1][y] = 2
                        self.map12[x - 1][y + 1] = 2
                        self.map12[x - 1][y + 2] = 2
                        self.map12[x - 1][y - 1] = 2
                        self.map12[x][y - 1] = 2
                        self.map12[x + 1][y] = 2
                        self.map12[x + 1][y + 1] = 2
                        self.map12[x + 1][y + 2] = 2
                        self.map12[x + 1][y - 1] = 2
                    else:
                        self.map12[x - 1][y] = 2
                        self.map12[x - 1][y + 1] = 2
                        self.map12[x - 1][y + 2] = 2
                        self.map12[x - 1][y + 3] = 2
                        self.map12[x - 1][y - 1] = 2
                        self.map12[x][y + 3] = 2
                        self.map12[x][y - 1] = 2
                        self.map12[x + 1][y + 1] = 2
                        self.map12[x + 1][y - 1] = 2
                        self.map12[x + 1][y + 2] = 2
                        self.map12[x + 1][y] = 2
                        self.map12[x + 1][y + 3] = 2
            elif mapb[0] == 3:
                if x == 0:
                    if y == 0:
                        self.map12[0][1] = 2
                        self.map12[1][1] = 2
                        self.map12[2][1] = 2
                        self.map12[3][1] = 2
                        self.map12[3][0] = 2
                    elif y == 9:
                        self.map12[0][8] = 2
                        self.map12[1][8] = 2
                        self.map12[2][8] = 2
                        self.map12[3][9] = 2
                        self.map12[3][8] = 2
                    else:
                        self.map12[0][y - 1] = 2
                        self.map12[0][y + 1] = 2
                        self.map12[1][y - 1] = 2
                        self.map12[3][y] = 2
                        self.map12[3][y + 1] = 2
                        self.map12[3][y - 1] = 2
                        self.map12[1][y + 1] = 2
                        self.map12[2][y + 1] = 2
                        self.map12[2][y - 1] = 2
                elif x == 7:
                    if y == 0:
                        self.map12[9][1] = 2
                        self.map12[8][1] = 2
                        self.map12[7][1] = 2
                        self.map12[6][1] = 2
                        self.map12[6][0] = 2
                    elif y == 9:
                        self.map12[9][8] = 2
                        self.map12[8][8] = 2
                        self.map12[7][8] = 2
                        self.map12[6][9] = 2
                        self.map12[6][8] = 2
                    else:
                        self.map12[9][y - 1] = 2
                        self.map12[9][y + 1] = 2
                        self.map12[8][y - 1] = 2
                        self.map12[8][y + 1] = 2
                        self.map12[7][y + 1] = 2
                        self.map12[7][y - 1] = 2
                        self.map12[6][y + 1] = 2
                        self.map12[6][y - 1] = 2
                        self.map12[6][y] = 2
                else:
                    if y == 0:
                        self.map12[x - 1][y] = 2
                        self.map12[x - 1][y + 1] = 2
                        self.map12[x][y + 1] = 2
                        self.map12[x + 1][y + 1] = 2
                        self.map12[x + 3][y + 1] = 2
                        self.map12[x + 3][y] = 2
                        self.map12[x + 2][y + 1] = 2
                    elif y == 9:
                        self.map12[x - 1][y] = 2
                        self.map12[x - 1][y - 1] = 2
                        self.map12[x][y - 1] = 2
                        self.map12[x + 1][y - 1] = 2
                        self.map12[x + 3][y] = 2
                        self.map12[x + 3][y - 1] = 2
                        self.map12[x + 2][y - 1] = 2
                    else:
                        self.map12[x - 1][y] = 2
                        self.map12[x - 1][y + 1] = 2
                        self.map12[x - 1][y - 1] = 2
                        self.map12[x][y + 1] = 2
                        self.map12[x][y - 1] = 2
                        self.map12[x + 1][y + 1] = 2
                        self.map12[x + 1][y - 1] = 2
                        self.map12[x + 2][y - 1] = 2
                        self.map12[x + 2][y + 1] = 2
                        self.map12[x + 3][y] = 2
                        self.map12[x + 3][y + 1] = 2
                        self.map12[x + 3][y - 1] = 2
            elif mapb[0] == 4 and mapb[2][0] - 1 == x:
                if x == 0:
                    if y == 0:
                        self.map12[0][4] = 2
                        self.map12[1][0] = 2
                        self.map12[1][1] = 2
                        self.map12[1][2] = 2
                        self.map12[1][3] = 2
                        self.map12[1][4] = 2
                    elif y == 6:
                        self.map12[0][5] = 2
                        self.map12[1][5] = 2
                        self.map12[1][6] = 2
                        self.map12[1][7] = 2
                        self.map12[1][8] = 2
                        self.map12[1][9] = 2
                    else:
                        self.map12[0][y - 1] = 2
                        self.map12[0][y + 4] = 2
                        self.map12[1][y - 1] = 2
                        self.map12[1][y + 1] = 2
                        self.map12[1][y] = 2
                        self.map12[1][y + 2] = 2
                        self.map12[1][y + 3] = 2
                        self.map12[1][y + 4] = 2
                elif x == 9:
                    if y == 0:
                        self.map12[9][4] = 2
                        self.map12[8][0] = 2
                        self.map12[8][1] = 2
                        self.map12[8][2] = 2
                        self.map12[8][3] = 2
                        self.map12[8][4] = 2
                    elif y == 6:
                        self.map12[9][5] = 2
                        self.map12[8][5] = 2
                        self.map12[8][6] = 2
                        self.map12[8][8] = 2
                        self.map12[8][7] = 2
                        self.map12[8][9] = 2
                    else:
                        self.map12[9][y - 1] = 2
                        self.map12[9][y + 4] = 2
                        self.map12[8][y - 1] = 2
                        self.map12[8][y + 1] = 2
                        self.map12[8][y + 2] = 2
                        self.map12[8][y + 3] = 2
                        self.map12[8][y + 4] = 2
                        self.map12[8][y] = 2
                else:
                    if y == 0:
                        self.map12[x - 1][y] = 2
                        self.map12[x - 1][y + 1] = 2
                        self.map12[x - 1][y + 2] = 2
                        self.map12[x - 1][y + 3] = 2
                        self.map12[x - 1][y + 4] = 2
                        self.map12[x][y + 4] = 2
                        self.map12[x + 1][y] = 2
                        self.map12[x + 1][y + 1] = 2
                        self.map12[x + 1][y + 2] = 2
                        self.map12[x + 1][y + 3] = 2
                        self.map12[x + 1][y + 4] = 2
                    elif y == 6:
                        self.map12[x - 1][y] = 2
                        self.map12[x - 1][y + 1] = 2
                        self.map12[x - 1][y + 2] = 2
                        self.map12[x - 1][y + 3] = 2
                        self.map12[x - 1][y - 1] = 2
                        self.map12[x][y - 1] = 2
                        self.map12[x + 1][y] = 2
                        self.map12[x + 1][y + 1] = 2
                        self.map12[x + 1][y + 2] = 2
                        self.map12[x + 1][y + 3] = 2
                        self.map12[x + 1][y - 1] = 2
                    else:
                        self.map12[x - 1][y] = 2
                        self.map12[x - 1][y + 1] = 2
                        self.map12[x - 1][y + 2] = 2
                        self.map12[x - 1][y + 3] = 2
                        self.map12[x - 1][y + 4] = 2
                        self.map12[x - 1][y - 1] = 2
                        self.map12[x][y + 4] = 2
                        self.map12[x][y - 1] = 2
                        self.map12[x + 1][y + 1] = 2
                        self.map12[x + 1][y - 1] = 2
                        self.map12[x + 1][y + 2] = 2
                        self.map12[x + 1][y + 4] = 2
                        self.map12[x + 1][y] = 2
                        self.map12[x + 1][y + 3] = 2
            elif mapb[0] == 4:
                if x == 0:
                    if y == 0:
                        self.map12[0][1] = 2
                        self.map12[1][1] = 2
                        self.map12[2][1] = 2
                        self.map12[3][1] = 2
                        self.map12[4][1] = 2
                        self.map12[4][0] = 2
                    elif y == 9:
                        self.map12[0][8] = 2
                        self.map12[1][8] = 2
                        self.map12[2][8] = 2
                        self.map12[4][9] = 2
                        self.map12[4][8] = 2
                        self.map12[3][8] = 2
                    else:
                        self.map12[0][y - 1] = 2
                        self.map12[0][y + 1] = 2
                        self.map12[1][y - 1] = 2
                        self.map12[3][y + 1] = 2
                        self.map12[3][y - 1] = 2
                        self.map12[1][y + 1] = 2
                        self.map12[2][y + 1] = 2
                        self.map12[2][y - 1] = 2
                        self.map12[4][y] = 2
                        self.map12[4][y + 1] = 2
                        self.map12[4][y - 1] = 2
                elif x == 6:
                    if y == 0:
                        self.map12[9][1] = 2
                        self.map12[8][1] = 2
                        self.map12[7][1] = 2
                        self.map12[6][1] = 2
                        self.map12[5][1] = 2
                        self.map12[5][0] = 2
                    elif y == 9:
                        self.map12[9][8] = 2
                        self.map12[8][8] = 2
                        self.map12[7][8] = 2
                        self.map12[5][8] = 2
                        self.map12[6][8] = 2
                        self.map12[5][9] = 2
                    else:
                        self.map12[9][y - 1] = 2
                        self.map12[9][y + 1] = 2
                        self.map12[8][y - 1] = 2
                        self.map12[8][y + 1] = 2
                        self.map12[7][y + 1] = 2
                        self.map12[7][y - 1] = 2
                        self.map12[6][y + 1] = 2
                        self.map12[6][y - 1] = 2
                        self.map12[5][y + 1] = 2
                        self.map12[5][y - 1] = 2
                        self.map12[5][y] = 2
                else:
                    if y == 0:
                        self.map12[x - 1][y] = 2
                        self.map12[x - 1][y + 1] = 2
                        self.map12[x][y + 1] = 2
                        self.map12[x + 1][y + 1] = 2
                        self.map12[x + 2][y + 1] = 2
                        self.map12[x + 3][y + 1] = 2
                        self.map12[x + 4][y + 1] = 2
                        self.map12[x + 4][y] = 2
                    elif y == 9:
                        self.map12[x - 1][y] = 2
                        self.map12[x - 1][y - 1] = 2
                        self.map12[x][y - 1] = 2
                        self.map12[x + 1][y - 1] = 2
                        self.map12[x + 2][y - 1] = 2
                        self.map12[x + 4][y] = 2
                        self.map12[x + 3][y - 1] = 2
                        self.map12[x + 4][y - 1] = 2
                    else:
                        self.map12[x - 1][y] = 2
                        self.map12[x - 1][y + 1] = 2
                        self.map12[x - 1][y - 1] = 2
                        self.map12[x][y + 1] = 2
                        self.map12[x][y - 1] = 2
                        self.map12[x + 1][y + 1] = 2
                        self.map12[x + 1][y - 1] = 2
                        self.map12[x + 2][y - 1] = 2
                        self.map12[x + 2][y + 1] = 2
                        self.map12[x + 4][y] = 2
                        self.map12[x + 3][y + 1] = 2
                        self.map12[x + 3][y - 1] = 2
                        self.map12[x + 4][y + 1] = 2
                        self.map12[x + 4][y - 1] = 2
        elif turn == 2:
            for j in range(1, mapb[0]):
                self.map21[mapb[j][0] - 1][mapb[j][1] - 1] = 1
            x, y = mapb[1][0] - 1, mapb[1][1] - 1
            if mapb[0] == 1:
                if x == 0:
                    if y == 0:
                        self.map21[0][1] = 2
                        self.map21[1][1] = 2
                        self.map21[1][0] = 2
                    elif y == 9:
                        self.map21[1][9] = 2
                        self.map21[0][8] = 2
                        self.map21[1][8] = 2
                    else:
                        self.map21[0][y - 1] = 2
                        self.map21[0][y + 1] = 2
                        self.map21[1][y - 1] = 2
                        self.map21[1][y] = 2
                        self.map21[1][y + 1] = 2
                elif x == 9:
                    if y == 0:
                        self.map21[9][1] = 2
                        self.map21[8][1] = 2
                        self.map21[8][0] = 2
                    elif y == 9:
                        self.map21[9][8] = 2
                        self.map21[8][9] = 2
                        self.map21[8][8] = 2
                    else:
                        self.map21[9][y - 1] = 2
                        self.map21[9][y + 1] = 2
                        self.map21[8][y - 1] = 2
                        self.map21[8][y] = 2
                        self.map21[8][y + 1] = 2
                else:
                    if y == 0:
                        self.map21[x - 1][y] = 2
                        self.map21[x - 1][y + 1] = 2
                        self.map21[x][y + 1] = 2
                        self.map21[x + 1][y] = 2
                        self.map21[x + 1][y + 1] = 2
                    elif y == 9:
                        self.map21[x - 1][y - 1] = 2
                        self.map21[x - 1][y] = 2
                        self.map21[x][y - 1] = 2
                        self.map21[x + 1][y - 1] = 2
                        self.map21[x + 1][y] = 2
                    else:
                        self.map21[x - 1][y - 1] = 2
                        self.map21[x - 1][y] = 2
                        self.map21[x - 1][y + 1] = 2
                        self.map21[x][y - 1] = 2
                        self.map21[x][y + 1] = 2
                        self.map21[x + 1][y - 1] = 2
                        self.map21[x + 1][y] = 2
                        self.map21[x + 1][y + 1] = 2
            elif mapb[0] == 2 and mapb[2][0] - 1 == x:
                if x == 0:
                    if y == 0:
                        self.map21[0][2] = 2
                        self.map21[1][1] = 2
                        self.map21[1][2] = 2
                        self.map21[1][0] = 2
                    elif y == 8:
                        self.map21[1][9] = 2
                        self.map21[0][7] = 2
                        self.map21[1][8] = 2
                        self.map21[1][7] = 2
                    else:
                        self.map21[0][y - 1] = 2
                        self.map21[0][y + 2] = 2
                        self.map21[1][y - 1] = 2
                        self.map21[1][y] = 2
                        self.map21[1][y + 1] = 2
                        self.map21[1][y + 2] = 2
                elif x == 9:
                    if y == 0:
                        self.map21[9][2] = 2
                        self.map21[8][2] = 2
                        self.map21[8][1] = 2
                        self.map21[8][0] = 2
                    elif y == 8:
                        self.map21[9][7] = 2
                        self.map21[8][9] = 2
                        self.map21[8][8] = 2
                        self.map21[8][7] = 2
                    else:
                        self.map21[9][y - 1] = 2
                        self.map21[9][y + 2] = 2
                        self.map21[8][y - 1] = 2
                        self.map21[8][y] = 2
                        self.map21[8][y + 1] = 2
                        self.map21[8][y + 2] = 2
                else:
                    if y == 0:
                        self.map21[x - 1][0] = 2
                        self.map21[x - 1][1] = 2
                        self.map21[x - 1][2] = 2
                        self.map21[x][2] = 2
                        self.map21[x + 1][0] = 2
                        self.map21[x + 1][1] = 2
                        self.map21[x + 1][2] = 2
                    elif y == 8:
                        self.map21[x - 1][9] = 2
                        self.map21[x - 1][8] = 2
                        self.map21[x - 1][7] = 2
                        self.map21[x][7] = 2
                        self.map21[x + 1][9] = 2
                        self.map21[x + 1][8] = 2
                        self.map21[x + 1][7] = 2
                    else:
                        self.map21[x - 1][y] = 2
                        self.map21[x - 1][y - 1] = 2
                        self.map21[x - 1][y + 1] = 2
                        self.map21[x - 1][y + 2] = 2
                        self.map21[x][y + 2] = 2
                        self.map21[x][y - 1] = 2
                        self.map21[x + 1][y] = 2
                        self.map21[x + 1][y - 1] = 2
                        self.map21[x + 1][y + 1] = 2
                        self.map21[x + 1][y + 2] = 2
            elif mapb[0] == 2:
                if x == 0:
                    if y == 0:
                        self.map21[0][1] = 2
                        self.map21[1][1] = 2
                        self.map21[2][1] = 2
                        self.map21[2][0] = 2
                    elif y == 9:
                        self.map21[0][8] = 2
                        self.map21[1][8] = 2
                        self.map21[2][8] = 2
                        self.map21[2][9] = 2
                    else:
                        self.map21[0][y - 1] = 2
                        self.map21[0][y + 1] = 2
                        self.map21[1][y - 1] = 2
                        self.map21[2][y] = 2
                        self.map21[1][y + 1] = 2
                        self.map21[2][y + 1] = 2
                        self.map21[2][y - 1] = 2
                elif x == 8:
                    if y == 0:
                        self.map21[9][1] = 2
                        self.map21[8][1] = 2
                        self.map21[7][1] = 2
                        self.map21[7][0] = 2
                    elif y == 9:
                        self.map21[9][8] = 2
                        self.map21[8][8] = 2
                        self.map21[7][8] = 2
                        self.map21[7][9] = 2
                    else:
                        self.map21[9][y - 1] = 2
                        self.map21[9][y + 1] = 2
                        self.map21[8][y - 1] = 2
                        self.map21[8][y + 1] = 2
                        self.map21[7][y + 1] = 2
                        self.map21[7][y - 1] = 2
                        self.map21[7][y] = 2
                else:
                    if y == 0:
                        self.map21[x - 1][y] = 2
                        self.map21[x - 1][y + 1] = 2
                        self.map21[x][y + 1] = 2
                        self.map21[x + 1][y + 1] = 2
                        self.map21[x + 2][y] = 2
                        self.map21[x + 2][y + 1] = 2
                    elif y == 9:
                        self.map21[x - 1][y] = 2
                        self.map21[x - 1][y - 1] = 2
                        self.map21[x][y - 1] = 2
                        self.map21[x + 1][y - 1] = 2
                        self.map21[x + 2][y] = 2
                        self.map21[x + 2][y - 1] = 2
                    else:
                        self.map21[x - 1][y] = 2
                        self.map21[x - 1][y + 1] = 2
                        self.map21[x - 1][y - 1] = 2
                        self.map21[x][y + 1] = 2
                        self.map21[x][y - 1] = 2
                        self.map21[x + 1][y + 1] = 2
                        self.map21[x + 1][y - 1] = 2
                        self.map21[x + 2][y - 1] = 2
                        self.map21[x + 2][y] = 2
                        self.map21[x + 2][y + 1] = 2
            elif mapb[0] == 3 and mapb[2][0] - 1 == x:
                if x == 0:
                    if y == 0:
                        self.map21[0][3] = 2
                        self.map21[1][0] = 2
                        self.map21[1][1] = 2
                        self.map21[1][2] = 2
                        self.map21[1][3] = 2
                    elif y == 7:
                        self.map21[0][6] = 2
                        self.map21[1][6] = 2
                        self.map21[1][7] = 2
                        self.map21[1][8] = 2
                        self.map21[1][9] = 2
                    else:
                        self.map21[0][y - 1] = 2
                        self.map21[0][y + 3] = 2
                        self.map21[1][y - 1] = 2
                        self.map21[1][y + 1] = 2
                        self.map21[1][y] = 2
                        self.map21[1][y + 2] = 2
                        self.map21[1][y + 3] = 2
                elif x == 9:
                    if y == 0:
                        self.map21[9][3] = 2
                        self.map21[8][0] = 2
                        self.map21[8][1] = 2
                        self.map21[8][2] = 2
                        self.map21[8][3] = 2
                    elif y == 7:
                        self.map21[9][6] = 2
                        self.map21[8][6] = 2
                        self.map21[8][8] = 2
                        self.map21[8][7] = 2
                        self.map21[8][9] = 2
                    else:
                        self.map21[9][y - 1] = 2
                        self.map21[9][y + 3] = 2
                        self.map21[8][y - 1] = 2
                        self.map21[8][y + 1] = 2
                        self.map21[8][y + 2] = 2
                        self.map21[8][y + 3] = 2
                        self.map21[8][y] = 2
                else:
                    if y == 0:
                        self.map21[x - 1][y] = 2
                        self.map21[x - 1][y + 1] = 2
                        self.map21[x - 1][y + 2] = 2
                        self.map21[x - 1][y + 3] = 2
                        self.map21[x][y + 3] = 2
                        self.map21[x + 1][y] = 2
                        self.map21[x + 1][y + 1] = 2
                        self.map21[x + 1][y + 2] = 2
                        self.map21[x + 1][y + 3] = 2
                    elif y == 7:
                        self.map21[x - 1][y] = 2
                        self.map21[x - 1][y + 1] = 2
                        self.map21[x - 1][y + 2] = 2
                        self.map21[x - 1][y - 1] = 2
                        self.map21[x][y - 1] = 2
                        self.map21[x + 1][y] = 2
                        self.map21[x + 1][y + 1] = 2
                        self.map21[x + 1][y + 2] = 2
                        self.map21[x + 1][y - 1] = 2
                    else:
                        self.map21[x - 1][y] = 2
                        self.map21[x - 1][y + 1] = 2
                        self.map21[x - 1][y + 2] = 2
                        self.map21[x - 1][y + 3] = 2
                        self.map21[x - 1][y - 1] = 2
                        self.map21[x][y + 3] = 2
                        self.map21[x][y - 1] = 2
                        self.map21[x + 1][y + 1] = 2
                        self.map21[x + 1][y - 1] = 2
                        self.map21[x + 1][y + 2] = 2
                        self.map21[x + 1][y] = 2
                        self.map21[x + 1][y + 3] = 2
            elif mapb[0] == 3:
                if x == 0:
                    if y == 0:
                        self.map21[0][1] = 2
                        self.map21[1][1] = 2
                        self.map21[2][1] = 2
                        self.map21[3][1] = 2
                        self.map21[3][0] = 2
                    elif y == 9:
                        self.map21[0][8] = 2
                        self.map21[1][8] = 2
                        self.map21[2][8] = 2
                        self.map21[3][9] = 2
                        self.map21[3][8] = 2
                    else:
                        self.map21[0][y - 1] = 2
                        self.map21[0][y + 1] = 2
                        self.map21[1][y - 1] = 2
                        self.map21[3][y] = 2
                        self.map21[3][y + 1] = 2
                        self.map21[3][y - 1] = 2
                        self.map21[1][y + 1] = 2
                        self.map21[2][y + 1] = 2
                        self.map21[2][y - 1] = 2
                elif x == 7:
                    if y == 0:
                        self.map21[9][1] = 2
                        self.map21[8][1] = 2
                        self.map21[7][1] = 2
                        self.map21[6][1] = 2
                        self.map21[6][0] = 2
                    elif y == 9:
                        self.map21[9][8] = 2
                        self.map21[8][8] = 2
                        self.map21[7][8] = 2
                        self.map21[6][9] = 2
                        self.map21[6][8] = 2
                    else:
                        self.map21[9][y - 1] = 2
                        self.map21[9][y + 1] = 2
                        self.map21[8][y - 1] = 2
                        self.map21[8][y + 1] = 2
                        self.map21[7][y + 1] = 2
                        self.map21[7][y - 1] = 2
                        self.map21[6][y + 1] = 2
                        self.map21[6][y - 1] = 2
                        self.map21[6][y] = 2
                else:
                    if y == 0:
                        self.map21[x - 1][y] = 2
                        self.map21[x - 1][y + 1] = 2
                        self.map21[x][y + 1] = 2
                        self.map21[x + 1][y + 1] = 2
                        self.map21[x + 3][y + 1] = 2
                        self.map21[x + 3][y] = 2
                        self.map21[x + 2][y + 1] = 2
                    elif y == 9:
                        self.map21[x - 1][y] = 2
                        self.map21[x - 1][y - 1] = 2
                        self.map21[x][y - 1] = 2
                        self.map21[x + 1][y - 1] = 2
                        self.map21[x + 3][y] = 2
                        self.map21[x + 3][y - 1] = 2
                        self.map21[x + 2][y - 1] = 2
                    else:
                        self.map21[x - 1][y] = 2
                        self.map21[x - 1][y + 1] = 2
                        self.map21[x - 1][y - 1] = 2
                        self.map21[x][y + 1] = 2
                        self.map21[x][y - 1] = 2
                        self.map21[x + 1][y + 1] = 2
                        self.map21[x + 1][y - 1] = 2
                        self.map21[x + 2][y - 1] = 2
                        self.map21[x + 2][y + 1] = 2
                        self.map21[x + 3][y] = 2
                        self.map21[x + 3][y + 1] = 2
                        self.map21[x + 3][y - 1] = 2
            elif mapb[0] == 4 and mapb[2][0] - 1 == x:
                if x == 0:
                    if y == 0:
                        self.map21[0][4] = 2
                        self.map21[1][0] = 2
                        self.map21[1][1] = 2
                        self.map21[1][2] = 2
                        self.map21[1][3] = 2
                        self.map21[1][4] = 2
                    elif y == 6:
                        self.map21[0][5] = 2
                        self.map21[1][5] = 2
                        self.map21[1][6] = 2
                        self.map21[1][7] = 2
                        self.map21[1][8] = 2
                        self.map21[1][9] = 2
                    else:
                        self.map21[0][y - 1] = 2
                        self.map21[0][y + 4] = 2
                        self.map21[1][y - 1] = 2
                        self.map21[1][y + 1] = 2
                        self.map21[1][y] = 2
                        self.map21[1][y + 2] = 2
                        self.map21[1][y + 3] = 2
                        self.map21[1][y + 4] = 2
                elif x == 9:
                    if y == 0:
                        self.map21[9][4] = 2
                        self.map21[8][0] = 2
                        self.map21[8][1] = 2
                        self.map21[8][2] = 2
                        self.map21[8][3] = 2
                        self.map21[8][4] = 2
                    elif y == 6:
                        self.map21[9][5] = 2
                        self.map21[8][5] = 2
                        self.map21[8][6] = 2
                        self.map21[8][8] = 2
                        self.map21[8][7] = 2
                        self.map21[8][9] = 2
                    else:
                        self.map21[9][y - 1] = 2
                        self.map21[9][y + 4] = 2
                        self.map21[8][y - 1] = 2
                        self.map21[8][y + 1] = 2
                        self.map21[8][y + 2] = 2
                        self.map21[8][y + 3] = 2
                        self.map21[8][y + 4] = 2
                        self.map21[8][y] = 2
                else:
                    if y == 0:
                        self.map21[x - 1][y] = 2
                        self.map21[x - 1][y + 1] = 2
                        self.map21[x - 1][y + 2] = 2
                        self.map21[x - 1][y + 3] = 2
                        self.map21[x - 1][y + 4] = 2
                        self.map21[x][y + 4] = 2
                        self.map21[x + 1][y] = 2
                        self.map21[x + 1][y + 1] = 2
                        self.map21[x + 1][y + 2] = 2
                        self.map21[x + 1][y + 3] = 2
                        self.map21[x + 1][y + 4] = 2
                    elif y == 6:
                        self.map21[x - 1][y] = 2
                        self.map21[x - 1][y + 1] = 2
                        self.map21[x - 1][y + 2] = 2
                        self.map21[x - 1][y + 3] = 2
                        self.map21[x - 1][y - 1] = 2
                        self.map21[x][y - 1] = 2
                        self.map21[x + 1][y] = 2
                        self.map21[x + 1][y + 1] = 2
                        self.map21[x + 1][y + 2] = 2
                        self.map21[x + 1][y + 3] = 2
                        self.map21[x + 1][y - 1] = 2
                    else:
                        self.map21[x - 1][y] = 2
                        self.map21[x - 1][y + 1] = 2
                        self.map21[x - 1][y + 2] = 2
                        self.map21[x - 1][y + 3] = 2
                        self.map21[x - 1][y + 4] = 2
                        self.map21[x - 1][y - 1] = 2
                        self.map21[x][y + 4] = 2
                        self.map21[x][y - 1] = 2
                        self.map21[x + 1][y + 1] = 2
                        self.map21[x + 1][y - 1] = 2
                        self.map21[x + 1][y + 2] = 2
                        self.map21[x + 1][y + 4] = 2
                        self.map21[x + 1][y] = 2
                        self.map21[x + 1][y + 3] = 2
            elif mapb[0] == 4:
                if x == 0:
                    if y == 0:
                        self.map21[0][1] = 2
                        self.map21[1][1] = 2
                        self.map21[2][1] = 2
                        self.map21[3][1] = 2
                        self.map21[4][1] = 2
                        self.map21[4][0] = 2
                    elif y == 9:
                        self.map21[0][8] = 2
                        self.map21[1][8] = 2
                        self.map21[2][8] = 2
                        self.map21[4][9] = 2
                        self.map21[4][8] = 2
                        self.map21[3][8] = 2
                    else:
                        self.map21[0][y - 1] = 2
                        self.map21[0][y + 1] = 2
                        self.map21[1][y - 1] = 2
                        self.map21[3][y + 1] = 2
                        self.map21[3][y - 1] = 2
                        self.map21[1][y + 1] = 2
                        self.map21[2][y + 1] = 2
                        self.map21[2][y - 1] = 2
                        self.map21[4][y] = 2
                        self.map21[4][y + 1] = 2
                        self.map21[4][y - 1] = 2
                elif x == 6:
                    if y == 0:
                        self.map21[9][1] = 2
                        self.map21[8][1] = 2
                        self.map21[7][1] = 2
                        self.map21[6][1] = 2
                        self.map21[5][1] = 2
                        self.map21[5][0] = 2
                    elif y == 9:
                        self.map21[9][8] = 2
                        self.map21[8][8] = 2
                        self.map21[7][8] = 2
                        self.map21[5][8] = 2
                        self.map21[6][8] = 2
                        self.map21[5][9] = 2
                    else:
                        self.map21[9][y - 1] = 2
                        self.map21[9][y + 1] = 2
                        self.map21[8][y - 1] = 2
                        self.map21[8][y + 1] = 2
                        self.map21[7][y + 1] = 2
                        self.map21[7][y - 1] = 2
                        self.map21[6][y + 1] = 2
                        self.map21[6][y - 1] = 2
                        self.map21[5][y + 1] = 2
                        self.map21[5][y - 1] = 2
                        self.map21[5][y] = 2
                else:
                    if y == 0:
                        self.map21[x - 1][y] = 2
                        self.map21[x - 1][y + 1] = 2
                        self.map21[x][y + 1] = 2
                        self.map21[x + 1][y + 1] = 2
                        self.map21[x + 2][y + 1] = 2
                        self.map21[x + 3][y + 1] = 2
                        self.map21[x + 4][y + 1] = 2
                        self.map21[x + 4][y] = 2
                    elif y == 9:
                        self.map21[x - 1][y] = 2
                        self.map21[x - 1][y - 1] = 2
                        self.map21[x][y - 1] = 2
                        self.map21[x + 1][y - 1] = 2
                        self.map21[x + 2][y - 1] = 2
                        self.map21[x + 4][y] = 2
                        self.map21[x + 3][y - 1] = 2
                        self.map21[x + 4][y - 1] = 2
                    else:
                        self.map21[x - 1][y] = 2
                        self.map21[x - 1][y + 1] = 2
                        self.map21[x - 1][y - 1] = 2
                        self.map21[x][y + 1] = 2
                        self.map21[x][y - 1] = 2
                        self.map21[x + 1][y + 1] = 2
                        self.map21[x + 1][y - 1] = 2
                        self.map21[x + 2][y - 1] = 2
                        self.map21[x + 2][y + 1] = 2
                        self.map21[x + 4][y] = 2
                        self.map21[x + 3][y + 1] = 2
                        self.map21[x + 3][y - 1] = 2
                        self.map21[x + 4][y + 1] = 2
                        self.map21[x + 4][y - 1] = 2

    def is_destroyed(self, i):
        for j in i[i[0]:]:
            if not j:
                return False
        if self.turn == 1:
            if i[0] == 1:
                self.ll2[0] -= 1
            elif i[0] == 2:
                self.ll2[1] -= 1
            elif i[0] == 3:
                self.ll2[2] -= 1
            elif i[0] == 3:
                self.ll2[2] -= 1
            elif i[0] == 4:
                self.ll2[3] -= 1
        elif self.turn == 2:
            if i[0] == 1:
                self.ll1[0] -= 1
            elif i[0] == 2:
                self.ll1[1] -= 1
            elif i[0] == 3:
                self.ll1[2] -= 1
            elif i[0] == 3:
                self.ll1[2] -= 1
            elif i[0] == 4:
                self.ll1[3] -= 1
        return True

    def check(self, turn, x, y, type, pos):
        if 0 > x or 9 < x or 0 > y or 9 < 0 or not (turn == 1 or turn == 2):
            return False
        elif type == 2 and pos == 1 and y > 8:
            return False
        elif type == 2 and pos == 2 and x > 8:
            return False
        elif type == 3 and pos == 1 and y > 7:
            return False
        elif type == 3 and pos == 2 and x > 7:
            return False
        elif type == 4 and pos == 1 and y > 6:
            return False
        elif type == 4 and pos == 2 and x > 6:
            return False
        elif turn == 1:
            c = 1
            for i in self.map1:
                if i[0] == type:
                    c += 1
            if type == 1 and c > 4:
                return False
            elif type == 2 and c > 3:
                return False
            elif type == 3 and c > 2:
                return False
            elif type == 4 and c > 1:
                return False
            elif pos == 1:
                for i in range(y, y + type):
                    if self.map11[x][i] != 0:
                        return False
            elif pos == 2:
                for i in range(x, x + type):
                    if self.map11[i][y] != 0:
                        return False
            return True
        elif turn == 2:
            c = 1
            for i in self.map2:
                if i[0] == type:
                    c += 1
            if type == 1 and c > 4:
                return False
            elif type == 2 and c > 3:
                return False
            elif type == 3 and c > 2:
                return False
            elif type == 4 and c > 1:
                return False
            if pos == 1:
                for i in range(y, y + type):
                    if self.map22[x][i] != 0:
                        return False
            elif pos == 2:
                for i in range(x, x + type):
                    if self.map22[i][y] != 0:
                        return False
            return True
        else:
            return False

    def setmarks(self, turn):
        if turn == 1:
            for i in self.map1:
                if i[0] == 1:
                    if i[1] == 0 and i[2] == 0:
                        self.map11[0][1] = -1
                        self.map11[1][0] = -1
                        self.map11[1][1] = -1
                    elif i[1] == 0 and i[2] == 9:
                        self.map11[0][8] = -1
                        self.map11[1][8] = -1
                        self.map11[1][9] = -1
                    elif i[1] == 9 and i[2] == 0:
                        self.map11[8][0] = -1
                        self.map11[8][1] = -1
                        self.map11[9][1] = -1
                    elif i[1] == 9 and i[2] == 9:
                        self.map11[8][8] = -1
                        self.map11[8][9] = -1
                        self.map11[9][8] = -1
                    elif i[1] == 0:
                        self.map11[0][i[2] - 1] = -1
                        self.map11[0][i[2] + 1] = -1
                        self.map11[1][i[2] - 1] = -1
                        self.map11[1][i[2]] = -1
                        self.map11[1][i[2] + 1] = -1
                    elif i[1] == 9:
                        self.map11[9][i[2] - 1] = -1
                        self.map11[9][i[2] + 1] = -1
                        self.map11[8][i[2] - 1] = -1
                        self.map11[8][i[2]] = -1
                        self.map11[8][i[2] + 1] = -1
                    elif i[2] == 0:
                        self.map11[i[1] - 1][0] = -1
                        self.map11[i[1] - 1][1] = -1
                        self.map11[i[1]][1] = -1
                        self.map11[i[1] + 1][0] = -1
                        self.map11[i[1] + 1][1] = -1
                    elif i[2] == 9:
                        self.map11[i[1] - 1][9] = -1
                        self.map11[i[1] + 1][9] = -1
                        self.map11[i[1] - 1][8] = -1
                        self.map11[i[1]][8] = -1
                        self.map11[i[1] + 1][8] = -1
                    else:
                        self.map11[i[1] - 1][i[2] - 1] = -1
                        self.map11[i[1] - 1][i[2]] = -1
                        self.map11[i[1] - 1][i[2] + 1] = -1
                        self.map11[i[1]][i[2] - 1] = -1
                        self.map11[i[1]][i[2] + 1] = -1
                        self.map11[i[1] + 1][i[2] - 1] = -1
                        self.map11[i[1] + 1][i[2]] = -1
                        self.map11[i[1] + 1][i[2] + 1] = -1
                elif i[0] == 2 and i[3] == 1:
                    if i[1] == 0 and i[2] == 0:
                        self.map11[0][2] = -1
                        self.map11[1][0] = -1
                        self.map11[1][1] = -1
                        self.map11[1][2] = -1
                    elif i[1] == 0 and i[2] == 8:
                        self.map11[0][7] = -1
                        self.map11[1][7] = -1
                        self.map11[1][8] = -1
                        self.map11[1][9] = -1
                    elif i[1] == 9 and i[2] == 0:
                        self.map11[8][0] = -1
                        self.map11[8][1] = -1
                        self.map11[8][2] = -1
                        self.map11[9][2] = -1
                    elif i[1] == 9 and i[2] == 8:
                        self.map11[8][7] = -1
                        self.map11[8][8] = -1
                        self.map11[8][9] = -1
                        self.map11[9][7] = -1
                    elif i[1] == 0:
                        self.map11[0][i[2] - 1] = -1
                        self.map11[0][i[2] + 2] = -1
                        self.map11[1][i[2] - 1] = -1
                        self.map11[1][i[2]] = -1
                        self.map11[1][i[2] + 1] = -1
                        self.map11[1][i[2] + 2] = -1
                    elif i[1] == 9:
                        self.map11[9][i[2] - 1] = -1
                        self.map11[9][i[2] + 2] = -1
                        self.map11[8][i[2] - 1] = -1
                        self.map11[8][i[2]] = -1
                        self.map11[8][i[2] + 1] = -1
                        self.map11[8][i[2] + 2] = -1
                    elif i[2] == 0:
                        self.map11[i[1] - 1][0] = -1
                        self.map11[i[1] + 1][0] = -1
                        self.map11[i[1] - 1][1] = -1
                        self.map11[i[1] + 1][1] = -1
                        self.map11[i[1] - 1][2] = -1
                        self.map11[i[1] + 1][2] = -1
                        self.map11[i[1]][2] = -1
                    elif i[2] == 8:
                        self.map11[i[1] - 1][9] = -1
                        self.map11[i[1] + 1][9] = -1
                        self.map11[i[1] - 1][8] = -1
                        self.map11[i[1] + 1][8] = -1
                        self.map11[i[1] - 1][7] = -1
                        self.map11[i[1] + 1][7] = -1
                        self.map11[i[1]][7] = -1
                    else:
                        self.map11[i[1] - 1][i[2] - 1] = -1
                        self.map11[i[1] - 1][i[2]] = -1
                        self.map11[i[1] - 1][i[2] + 1] = -1
                        self.map11[i[1] - 1][i[2] + 2] = -1
                        self.map11[i[1] + 1][i[2] - 1] = -1
                        self.map11[i[1] + 1][i[2]] = -1
                        self.map11[i[1] + 1][i[2] + 1] = -1
                        self.map11[i[1] + 1][i[2] + 2] = -1
                        self.map11[i[1]][i[2] - 1] = -1
                        self.map11[i[1]][i[2] + 2] = -1
                elif i[0] == 2 and i[3] == 2:
                    if i[1] == 0 and i[2] == 0:
                        self.map11[0][1] = -1
                        self.map11[1][1] = -1
                        self.map11[2][1] = -1
                        self.map11[2][0] = -1
                    if i[1] == 0 and i[2] == 9:
                        self.map11[0][8] = -1
                        self.map11[1][8] = -1
                        self.map11[2][8] = -1
                        self.map11[2][9] = -1
                    if i[1] == 8 and i[2] == 0:
                        self.map11[7][0] = -1
                        self.map11[7][1] = -1
                        self.map11[8][1] = -1
                        self.map11[9][1] = -1
                    if i[1] == 8 and i[2] == 9:
                        self.map11[7][9] = -1
                        self.map11[7][8] = -1
                        self.map11[8][8] = -1
                        self.map11[9][8] = -1
                    elif i[1] == 0:
                        self.map11[0][i[2] - 1] = -1
                        self.map11[0][i[2] + 1] = -1
                        self.map11[1][i[2] - 1] = -1
                        self.map11[1][i[2] + 1] = -1
                        self.map11[2][i[2] - 1] = -1
                        self.map11[2][i[2] + 1] = -1
                        self.map11[2][i[2]] = -1
                    elif i[1] == 8:
                        self.map11[9][i[2] - 1] = -1
                        self.map11[9][i[2] + 1] = -1
                        self.map11[8][i[2] - 1] = -1
                        self.map11[8][i[2] + 1] = -1
                        self.map11[7][i[2] - 1] = -1
                        self.map11[7][i[2] + 1] = -1
                        self.map11[7][i[2]] = -1
                    elif i[2] == 0:
                        self.map11[i[1] - 1][0] = -1
                        self.map11[i[1] - 1][1] = -1
                        self.map11[i[1]][1] = -1
                        self.map11[i[1] + 1][1] = -1
                        self.map11[i[1] + 2][1] = -1
                        self.map11[i[1] + 2][0] = -1
                    elif i[2] == 9:
                        self.map11[i[1] - 1][9] = -1
                        self.map11[i[1] - 1][8] = -1
                        self.map11[i[1] + 1][8] = -1
                        self.map11[i[1] + 2][8] = -1
                        self.map11[i[1] + 2][9] = -1
                        self.map11[i[1]][8] = -1
                    else:
                        self.map11[i[1] - 1][i[2] - 1] = -1
                        self.map11[i[1] - 1][i[2]] = -1
                        self.map11[i[1] - 1][i[2] + 1] = -1
                        self.map11[i[1] + 1][i[2] + 1] = -1
                        self.map11[i[1] + 1][i[2] - 1] = -1
                        self.map11[i[1]][i[2] - 1] = -1
                        self.map11[i[1]][i[2] + 2] = -1
                        self.map11[i[1] + 2][i[2]] = -1
                        self.map11[i[1] + 2][i[2] + 1] = -1
                        self.map11[i[1] + 2][i[2] - 1] = -1
                elif i[0] == 3 and i[3] == 1:
                    if i[1] == 0 and i[2] == 0:
                        self.map11[0][3] = -1
                        self.map11[1][0] = -1
                        self.map11[1][1] = -1
                        self.map11[1][2] = -1
                        self.map11[1][3] = -1
                    elif i[1] == 0 and i[2] == 7:
                        self.map11[0][6] = -1
                        self.map11[1][6] = -1
                        self.map11[1][7] = -1
                        self.map11[1][8] = -1
                        self.map11[1][9] = -1
                    elif i[1] == 9 and i[2] == 0:
                        self.map11[8][0] = -1
                        self.map11[8][1] = -1
                        self.map11[8][2] = -1
                        self.map11[8][3] = -1
                        self.map11[9][3] = -1
                    elif i[1] == 9 and i[2] == 7:
                        self.map11[8][6] = -1
                        self.map11[8][7] = -1
                        self.map11[8][8] = -1
                        self.map11[8][9] = -1
                        self.map11[9][6] = -1
                    elif i[1] == 0:
                        self.map11[0][i[2] - 1] = -1
                        self.map11[0][i[2] + 3] = -1
                        self.map11[1][i[2] - 1] = -1
                        self.map11[1][i[2]] = -1
                        self.map11[1][i[2] + 1] = -1
                        self.map11[1][i[2] + 2] = -1
                        self.map11[1][i[2] + 3] = -1
                    elif i[1] == 9:
                        self.map11[9][i[2] - 1] = -1
                        self.map11[9][i[2] + 3] = -1
                        self.map11[8][i[2] - 1] = -1
                        self.map11[8][i[2]] = -1
                        self.map11[8][i[2] + 1] = -1
                        self.map11[8][i[2] + 2] = -1
                        self.map11[8][i[2] + 3] = -1
                    elif i[2] == 0:
                        self.map11[i[1] - 1][0] = -1
                        self.map11[i[1] + 1][0] = -1
                        self.map11[i[1] - 1][1] = -1
                        self.map11[i[1] + 1][1] = -1
                        self.map11[i[1] - 1][2] = -1
                        self.map11[i[1] + 1][2] = -1
                        self.map11[i[1] - 1][3] = -1
                        self.map11[i[1] + 1][3] = -1
                        self.map11[i[1]][3] = -1
                    elif i[2] == 7:
                        self.map11[i[1] - 1][9] = -1
                        self.map11[i[1] + 1][9] = -1
                        self.map11[i[1] - 1][8] = -1
                        self.map11[i[1] + 1][8] = -1
                        self.map11[i[1] - 1][7] = -1
                        self.map11[i[1] + 1][7] = -1
                        self.map11[i[1] - 1][6] = -1
                        self.map11[i[1] + 1][6] = -1
                        self.map11[i[1]][6] = -1
                    else:
                        self.map11[i[1] - 1][i[2] - 1] = -1
                        self.map11[i[1] - 1][i[2]] = -1
                        self.map11[i[1] - 1][i[2] + 1] = -1
                        self.map11[i[1] - 1][i[2] + 2] = -1
                        self.map11[i[1] - 1][i[2] + 3] = -1
                        self.map11[i[1] + 1][i[2] - 1] = -1
                        self.map11[i[1] + 1][i[2]] = -1
                        self.map11[i[1] + 1][i[2] + 1] = -1
                        self.map11[i[1] + 1][i[2] + 2] = -1
                        self.map11[i[1] + 1][i[2] + 3] = -1
                        self.map11[i[1]][i[2] - 1] = -1
                        self.map11[i[1]][i[2] + 3] = -1
                elif i[0] == 3 and i[3] == 2:
                    if i[1] == 0 and i[2] == 0:
                        self.map11[0][1] = -1
                        self.map11[1][1] = -1
                        self.map11[2][1] = -1
                        self.map11[3][1] = -1
                        self.map11[3][0] = -1
                    if i[1] == 0 and i[2] == 9:
                        self.map11[0][8] = -1
                        self.map11[1][8] = -1
                        self.map11[2][8] = -1
                        self.map11[3][8] = -1
                        self.map11[3][9] = -1
                    if i[1] == 7 and i[2] == 0:
                        self.map11[6][0] = -1
                        self.map11[6][1] = -1
                        self.map11[7][1] = -1
                        self.map11[8][1] = -1
                        self.map11[9][1] = -1
                    if i[1] == 7 and i[2] == 9:
                        self.map11[6][9] = -1
                        self.map11[6][8] = -1
                        self.map11[7][8] = -1
                        self.map11[8][8] = -1
                        self.map11[9][8] = -1
                    elif i[1] == 0:
                        self.map11[0][i[2] - 1] = -1
                        self.map11[0][i[2] + 1] = -1
                        self.map11[1][i[2] - 1] = -1
                        self.map11[1][i[2] + 1] = -1
                        self.map11[2][i[2] + 1] = -1
                        self.map11[2][i[2] - 1] = -1
                        self.map11[3][i[2] + 1] = -1
                        self.map11[3][i[2] - 1] = -1
                        self.map11[3][i[2]] = -1
                    elif i[1] == 7:
                        self.map11[9][i[2] - 1] = -1
                        self.map11[9][i[2] + 1] = -1
                        self.map11[8][i[2] - 1] = -1
                        self.map11[8][i[2] + 1] = -1
                        self.map11[7][i[2] - 1] = -1
                        self.map11[7][i[2] + 1] = -1
                        self.map11[6][i[2] - 1] = -1
                        self.map11[6][i[2] + 1] = -1
                        self.map11[6][i[2]] = -1
                    elif i[2] == 0:
                        self.map11[i[1] - 1][0] = -1
                        self.map11[i[1] - 1][1] = -1
                        self.map11[i[1]][1] = -1
                        self.map11[i[1] + 1][1] = -1
                        self.map11[i[1] + 2][1] = -1
                        self.map11[i[1] + 3][1] = -1
                        self.map11[i[1] + 3][0] = -1
                    elif i[2] == 9:
                        self.map11[i[1] - 1][9] = -1
                        self.map11[i[1] - 1][8] = -1
                        self.map11[i[1]][8] = -1
                        self.map11[i[1] + 1][8] = -1
                        self.map11[i[1] + 2][8] = -1
                        self.map11[i[1] + 3][8] = -1
                        self.map11[i[1] + 3][9] = -1
                    else:
                        self.map11[i[1] - 1][i[2] - 1] = -1
                        self.map11[i[1] - 1][i[2]] = -1
                        self.map11[i[1] - 1][i[2] + 1] = -1
                        self.map11[i[1] + 1][i[2] + 1] = -1
                        self.map11[i[1] + 1][i[2] - 1] = -1
                        self.map11[i[1]][i[2] - 1] = -1
                        self.map11[i[1]][i[2] + 2] = -1
                        self.map11[i[1] + 2][i[2] + 1] = -1
                        self.map11[i[1] + 2][i[2] - 1] = -1
                        self.map11[i[1] + 3][i[2] + 1] = -1
                        self.map11[i[1] + 3][i[2] - 1] = -1
                        self.map11[i[1] + 3][i[2]] = -1
                elif i[0] == 4 and i[3] == 1:
                    if i[1] == 0 and i[2] == 0:
                        self.map11[0][4] = -1
                        self.map11[1][0] = -1
                        self.map11[1][1] = -1
                        self.map11[1][2] = -1
                        self.map11[1][3] = -1
                        self.map11[1][4] = -1
                    elif i[1] == 0 and i[2] == 6:
                        self.map11[0][5] = -1
                        self.map11[1][5] = -1
                        self.map11[1][6] = -1
                        self.map11[1][7] = -1
                        self.map11[1][8] = -1
                        self.map11[1][9] = -1
                    elif i[1] == 9 and i[2] == 0:
                        self.map11[8][0] = -1
                        self.map11[8][1] = -1
                        self.map11[8][2] = -1
                        self.map11[8][3] = -1
                        self.map11[8][4] = -1
                        self.map11[9][4] = -1
                    elif i[1] == 9 and i[2] == 6:
                        self.map11[8][5] = -1
                        self.map11[8][6] = -1
                        self.map11[8][7] = -1
                        self.map11[8][8] = -1
                        self.map11[8][9] = -1
                        self.map11[9][5] = -1
                    elif i[1] == 0:
                        self.map11[0][i[2] - 1] = -1
                        self.map11[0][i[2] + 4] = -1
                        self.map11[1][i[2] - 1] = -1
                        self.map11[1][i[2]] = -1
                        self.map11[1][i[2] + 1] = -1
                        self.map11[1][i[2] + 2] = -1
                        self.map11[1][i[2] + 3] = -1
                        self.map11[1][i[2] + 4] = -1
                    elif i[1] == 9:
                        self.map11[9][i[2] - 1] = -1
                        self.map11[9][i[2] + 4] = -1
                        self.map11[8][i[2] - 1] = -1
                        self.map11[8][i[2]] = -1
                        self.map11[8][i[2] + 1] = -1
                        self.map11[8][i[2] + 2] = -1
                        self.map11[8][i[2] + 3] = -1
                        self.map11[8][i[2] + 4] = -1
                    elif i[2] == 0:
                        self.map11[i[1] - 1][0] = -1
                        self.map11[i[1] + 1][0] = -1
                        self.map11[i[1] - 1][1] = -1
                        self.map11[i[1] + 1][1] = -1
                        self.map11[i[1] - 1][2] = -1
                        self.map11[i[1] + 1][2] = -1
                        self.map11[i[1] - 1][3] = -1
                        self.map11[i[1] + 1][3] = -1
                        self.map11[i[1] - 1][4] = -1
                        self.map11[i[1] + 1][4] = -1
                        self.map11[i[1]][4] = -1
                    elif i[2] == 6:
                        self.map11[i[1] - 1][9] = -1
                        self.map11[i[1] + 1][9] = -1
                        self.map11[i[1] - 1][8] = -1
                        self.map11[i[1] + 1][8] = -1
                        self.map11[i[1] - 1][7] = -1
                        self.map11[i[1] + 1][7] = -1
                        self.map11[i[1] - 1][6] = -1
                        self.map11[i[1] + 1][6] = -1
                        self.map11[i[1] - 1][5] = -1
                        self.map11[i[1] + 1][5] = -1
                        self.map11[i[1]][5] = -1
                    else:
                        self.map11[i[1] - 1][i[2] - 1] = -1
                        self.map11[i[1] - 1][i[2]] = -1
                        self.map11[i[1] - 1][i[2] + 1] = -1
                        self.map11[i[1] - 1][i[2] + 2] = -1
                        self.map11[i[1] - 1][i[2] + 3] = -1
                        self.map11[i[1] - 1][i[2] + 4] = -1
                        self.map11[i[1] + 1][i[2] - 1] = -1
                        self.map11[i[1] + 1][i[2]] = -1
                        self.map11[i[1] + 1][i[2] + 1] = -1
                        self.map11[i[1] + 1][i[2] + 2] = -1
                        self.map11[i[1] + 1][i[2] + 3] = -1
                        self.map11[i[1] + 1][i[2] + 4] = -1
                        self.map11[i[1]][i[2] - 1] = -1
                        self.map11[i[1]][i[2] + 4] = -1
                elif i[0] == 4 and i[3] == 2:
                    if i[1] == 0 and i[2] == 0:
                        self.map11[0][1] = -1
                        self.map11[1][1] = -1
                        self.map11[2][1] = -1
                        self.map11[3][1] = -1
                        self.map11[4][1] = -1
                        self.map11[4][0] = -1
                    if i[1] == 0 and i[2] == 9:
                        self.map11[0][8] = -1
                        self.map11[1][8] = -1
                        self.map11[2][8] = -1
                        self.map11[3][8] = -1
                        self.map11[4][8] = -1
                        self.map11[4][9] = -1
                    if i[1] == 6 and i[2] == 0:
                        self.map11[5][0] = -1
                        self.map11[5][1] = -1
                        self.map11[6][1] = -1
                        self.map11[7][1] = -1
                        self.map11[8][1] = -1
                        self.map11[9][1] = -1
                    if i[1] == 6 and i[2] == 9:
                        self.map11[5][9] = -1
                        self.map11[5][8] = -1
                        self.map11[6][8] = -1
                        self.map11[7][8] = -1
                        self.map11[8][8] = -1
                        self.map11[9][8] = -1
                    elif i[1] == 0:
                        self.map11[0][i[2] - 1] = -1
                        self.map11[0][i[2] + 1] = -1
                        self.map11[1][i[2] - 1] = -1
                        self.map11[1][i[2] + 1] = -1
                        self.map11[2][i[2] + 1] = -1
                        self.map11[2][i[2] - 1] = -1
                        self.map11[3][i[2] + 1] = -1
                        self.map11[3][i[2] - 1] = -1
                        self.map11[4][i[2] + 1] = -1
                        self.map11[4][i[2] - 1] = -1
                        self.map11[4][i[2]] = -1
                    elif i[1] == 6:
                        self.map11[9][i[2] - 1] = -1
                        self.map11[9][i[2] + 1] = -1
                        self.map11[8][i[2] - 1] = -1
                        self.map11[8][i[2] + 1] = -1
                        self.map11[7][i[2] - 1] = -1
                        self.map11[7][i[2] + 1] = -1
                        self.map11[6][i[2] - 1] = -1
                        self.map11[6][i[2] + 1] = -1
                        self.map11[5][i[2] - 1] = -1
                        self.map11[5][i[2] + 1] = -1
                        self.map11[5][i[2]] = -1
                    elif i[2] == 0:
                        self.map11[i[1] - 1][0] = -1
                        self.map11[i[1] - 1][1] = -1
                        self.map11[i[1]][1] = -1
                        self.map11[i[1] + 1][1] = -1
                        self.map11[i[1] + 2][1] = -1
                        self.map11[i[1] + 3][1] = -1
                        self.map11[i[1] + 4][1] = -1
                        self.map11[i[1] + 4][0] = -1
                    elif i[2] == 9:
                        self.map11[i[1] - 1][9] = -1
                        self.map11[i[1] - 1][8] = -1
                        self.map11[i[1]][8] = -1
                        self.map11[i[1] + 1][8] = -1
                        self.map11[i[1] + 2][8] = -1
                        self.map11[i[1] + 3][8] = -1
                        self.map11[i[1] + 4][8] = -1
                        self.map11[i[1] + 4][9] = -1
                    else:
                        self.map11[i[1] - 1][i[2] - 1] = -1
                        self.map11[i[1] - 1][i[2]] = -1
                        self.map11[i[1] - 1][i[2] + 1] = -1
                        self.map11[i[1] + 1][i[2] + 1] = -1
                        self.map11[i[1] + 1][i[2] - 1] = -1
                        self.map11[i[1]][i[2] - 1] = -1
                        self.map11[i[1]][i[2] + 2] = -1
                        self.map11[i[1] + 2][i[2] + 1] = -1
                        self.map11[i[1] + 2][i[2] - 1] = -1
                        self.map11[i[1] + 3][i[2] + 1] = -1
                        self.map11[i[1] + 3][i[2] - 1] = -1
                        self.map11[i[1] + 4][i[2] + 1] = -1
                        self.map11[i[1] + 4][i[2] - 1] = -1
                        self.map11[i[1] + 4][i[2]] = -1
            return True
        elif turn == 2:
            for i in self.map2:
                if i[0] == 1:
                    if i[1] == 0 and i[2] == 0:
                        self.map22[0][1] = -1
                        self.map22[1][0] = -1
                        self.map22[1][1] = -1
                    elif i[1] == 0 and i[2] == 9:
                        self.map22[0][8] = -1
                        self.map22[1][8] = -1
                        self.map22[1][9] = -1
                    elif i[1] == 9 and i[2] == 0:
                        self.map22[8][0] = -1
                        self.map22[8][1] = -1
                        self.map22[9][1] = -1
                    elif i[1] == 9 and i[2] == 9:
                        self.map22[8][8] = -1
                        self.map22[8][9] = -1
                        self.map22[9][8] = -1
                    elif i[1] == 0:
                        self.map22[0][i[2] - 1] = -1
                        self.map22[0][i[2] + 1] = -1
                        self.map22[1][i[2] - 1] = -1
                        self.map22[1][i[2]] = -1
                        self.map22[1][i[2] + 1] = -1
                    elif i[1] == 9:
                        self.map22[9][i[2] - 1] = -1
                        self.map22[9][i[2] + 1] = -1
                        self.map22[8][i[2] - 1] = -1
                        self.map22[8][i[2]] = -1
                        self.map22[8][i[2] + 1] = -1
                    elif i[2] == 0:
                        self.map22[i[1] - 1][0] = -1
                        self.map22[i[1] - 1][1] = -1
                        self.map22[i[1]][1] = -1
                        self.map22[i[1] + 1][0] = -1
                        self.map22[i[1] + 1][1] = -1
                    elif i[2] == 9:
                        self.map22[i[1] - 1][9] = -1
                        self.map22[i[1] + 1][9] = -1
                        self.map22[i[1] - 1][8] = -1
                        self.map22[i[1]][8] = -1
                        self.map22[i[1] + 1][8] = -1
                    else:
                        self.map22[i[1] - 1][i[2] - 1] = -1
                        self.map22[i[1] - 1][i[2]] = -1
                        self.map22[i[1] - 1][i[2] + 1] = -1
                        self.map22[i[1]][i[2] - 1] = -1
                        self.map22[i[1]][i[2] + 1] = -1
                        self.map22[i[1] + 1][i[2] - 1] = -1
                        self.map22[i[1] + 1][i[2]] = -1
                        self.map22[i[1] + 1][i[2] + 1] = -1
                elif i[0] == 2 and i[3] == 1:
                    if i[1] == 0 and i[2] == 0:
                        self.map22[0][2] = -1
                        self.map22[1][0] = -1
                        self.map22[1][1] = -1
                        self.map22[1][2] = -1
                    elif i[1] == 0 and i[2] == 8:
                        self.map22[0][7] = -1
                        self.map22[1][7] = -1
                        self.map22[1][8] = -1
                        self.map22[1][9] = -1
                    elif i[1] == 9 and i[2] == 0:
                        self.map22[8][0] = -1
                        self.map22[8][1] = -1
                        self.map22[8][2] = -1
                        self.map22[9][2] = -1
                    elif i[1] == 9 and i[2] == 8:
                        self.map22[8][7] = -1
                        self.map22[8][8] = -1
                        self.map22[8][9] = -1
                        self.map22[9][7] = -1
                    elif i[1] == 0:
                        self.map22[0][i[2] - 1] = -1
                        self.map22[0][i[2] + 2] = -1
                        self.map22[1][i[2] - 1] = -1
                        self.map22[1][i[2]] = -1
                        self.map22[1][i[2] + 1] = -1
                        self.map22[1][i[2] + 2] = -1
                    elif i[1] == 9:
                        self.map22[9][i[2] - 1] = -1
                        self.map22[9][i[2] + 2] = -1
                        self.map22[8][i[2] - 1] = -1
                        self.map22[8][i[2]] = -1
                        self.map22[8][i[2] + 1] = -1
                        self.map22[8][i[2] + 2] = -1
                    elif i[2] == 0:
                        self.map22[i[1] - 1][0] = -1
                        self.map22[i[1] + 1][0] = -1
                        self.map22[i[1] - 1][1] = -1
                        self.map22[i[1] + 1][1] = -1
                        self.map22[i[1] - 1][2] = -1
                        self.map22[i[1] + 1][2] = -1
                        self.map22[i[1]][2] = -1
                    elif i[2] == 8:
                        self.map22[i[1] - 1][9] = -1
                        self.map22[i[1] + 1][9] = -1
                        self.map22[i[1] - 1][8] = -1
                        self.map22[i[1] + 1][8] = -1
                        self.map22[i[1] - 1][7] = -1
                        self.map22[i[1] + 1][7] = -1
                        self.map22[i[1]][7] = -1
                    else:
                        self.map22[i[1] - 1][i[2] - 1] = -1
                        self.map22[i[1] - 1][i[2]] = -1
                        self.map22[i[1] - 1][i[2] + 1] = -1
                        self.map22[i[1] - 1][i[2] + 2] = -1
                        self.map22[i[1] + 1][i[2] - 1] = -1
                        self.map22[i[1] + 1][i[2]] = -1
                        self.map22[i[1] + 1][i[2] + 1] = -1
                        self.map22[i[1] + 1][i[2] + 2] = -1
                        self.map22[i[1]][i[2] - 1] = -1
                        self.map22[i[1]][i[2] + 2] = -1
                elif i[0] == 2 and i[3] == 2:
                    if i[1] == 0 and i[2] == 0:
                        self.map22[0][1] = -1
                        self.map22[1][1] = -1
                        self.map22[2][1] = -1
                        self.map22[2][0] = -1
                    if i[1] == 0 and i[2] == 9:
                        self.map22[0][8] = -1
                        self.map22[1][8] = -1
                        self.map22[2][8] = -1
                        self.map22[2][9] = -1
                    if i[1] == 8 and i[2] == 0:
                        self.map22[7][0] = -1
                        self.map22[7][1] = -1
                        self.map22[8][1] = -1
                        self.map22[9][1] = -1
                    if i[1] == 8 and i[2] == 9:
                        self.map22[7][9] = -1
                        self.map22[7][8] = -1
                        self.map22[8][8] = -1
                        self.map22[9][8] = -1
                    elif i[1] == 0:
                        self.map22[0][i[2] - 1] = -1
                        self.map22[0][i[2] + 1] = -1
                        self.map22[1][i[2] - 1] = -1
                        self.map22[1][i[2] + 1] = -1
                        self.map22[2][i[2] - 1] = -1
                        self.map22[2][i[2] + 1] = -1
                        self.map22[2][i[2]] = -1
                    elif i[1] == 8:
                        self.map22[9][i[2] - 1] = -1
                        self.map22[9][i[2] + 1] = -1
                        self.map22[8][i[2] - 1] = -1
                        self.map22[8][i[2] + 1] = -1
                        self.map22[7][i[2] - 1] = -1
                        self.map22[7][i[2] + 1] = -1
                        self.map22[7][i[2]] = -1
                    elif i[2] == 0:
                        self.map22[i[1] - 1][0] = -1
                        self.map22[i[1] - 1][1] = -1
                        self.map22[i[1]][1] = -1
                        self.map22[i[1] + 1][1] = -1
                        self.map22[i[1] + 2][1] = -1
                        self.map22[i[1] + 2][0] = -1
                    elif i[2] == 9:
                        self.map22[i[1] - 1][9] = -1
                        self.map22[i[1] - 1][8] = -1
                        self.map22[i[1] + 1][8] = -1
                        self.map22[i[1] + 2][8] = -1
                        self.map22[i[1] + 2][9] = -1
                        self.map22[i[1]][8] = -1
                    else:
                        self.map22[i[1] - 1][i[2] - 1] = -1
                        self.map22[i[1] - 1][i[2]] = -1
                        self.map22[i[1] - 1][i[2] + 1] = -1
                        self.map22[i[1] + 1][i[2] + 1] = -1
                        self.map22[i[1] + 1][i[2] - 1] = -1
                        self.map22[i[1]][i[2] - 1] = -1
                        self.map22[i[1]][i[2] + 2] = -1
                        self.map22[i[1] + 2][i[2]] = -1
                        self.map22[i[1] + 2][i[2] + 1] = -1
                        self.map22[i[1] + 2][i[2] - 1] = -1
                elif i[0] == 3 and i[3] == 1:
                    if i[1] == 0 and i[2] == 0:
                        self.map22[0][3] = -1
                        self.map22[1][0] = -1
                        self.map22[1][1] = -1
                        self.map22[1][2] = -1
                        self.map22[1][3] = -1
                    elif i[1] == 0 and i[2] == 7:
                        self.map22[0][6] = -1
                        self.map22[1][6] = -1
                        self.map22[1][7] = -1
                        self.map22[1][8] = -1
                        self.map22[1][9] = -1
                    elif i[1] == 9 and i[2] == 0:
                        self.map22[8][0] = -1
                        self.map22[8][1] = -1
                        self.map22[8][2] = -1
                        self.map22[8][3] = -1
                        self.map22[9][3] = -1
                    elif i[1] == 9 and i[2] == 7:
                        self.map22[8][6] = -1
                        self.map22[8][7] = -1
                        self.map22[8][8] = -1
                        self.map22[8][9] = -1
                        self.map22[9][6] = -1
                    elif i[1] == 0:
                        self.map22[0][i[2] - 1] = -1
                        self.map22[0][i[2] + 3] = -1
                        self.map22[1][i[2] - 1] = -1
                        self.map22[1][i[2]] = -1
                        self.map22[1][i[2] + 1] = -1
                        self.map22[1][i[2] + 2] = -1
                        self.map22[1][i[2] + 3] = -1
                    elif i[1] == 9:
                        self.map22[9][i[2] - 1] = -1
                        self.map22[9][i[2] + 3] = -1
                        self.map22[8][i[2] - 1] = -1
                        self.map22[8][i[2]] = -1
                        self.map22[8][i[2] + 1] = -1
                        self.map22[8][i[2] + 2] = -1
                        self.map22[8][i[2] + 3] = -1
                    elif i[2] == 0:
                        self.map22[i[1] - 1][0] = -1
                        self.map22[i[1] + 1][0] = -1
                        self.map22[i[1] - 1][1] = -1
                        self.map22[i[1] + 1][1] = -1
                        self.map22[i[1] - 1][2] = -1
                        self.map22[i[1] + 1][2] = -1
                        self.map22[i[1] - 1][3] = -1
                        self.map22[i[1] + 1][3] = -1
                        self.map22[i[1]][3] = -1
                    elif i[2] == 7:
                        self.map22[i[1] - 1][9] = -1
                        self.map22[i[1] + 1][9] = -1
                        self.map22[i[1] - 1][8] = -1
                        self.map22[i[1] + 1][8] = -1
                        self.map22[i[1] - 1][7] = -1
                        self.map22[i[1] + 1][7] = -1
                        self.map22[i[1] - 1][6] = -1
                        self.map22[i[1] + 1][6] = -1
                        self.map22[i[1]][6] = -1
                    else:
                        self.map22[i[1] - 1][i[2] - 1] = -1
                        self.map22[i[1] - 1][i[2]] = -1
                        self.map22[i[1] - 1][i[2] + 1] = -1
                        self.map22[i[1] - 1][i[2] + 2] = -1
                        self.map22[i[1] - 1][i[2] + 3] = -1
                        self.map22[i[1] + 1][i[2] - 1] = -1
                        self.map22[i[1] + 1][i[2]] = -1
                        self.map22[i[1] + 1][i[2] + 1] = -1
                        self.map22[i[1] + 1][i[2] + 2] = -1
                        self.map22[i[1] + 1][i[2] + 3] = -1
                        self.map22[i[1]][i[2] - 1] = -1
                        self.map22[i[1]][i[2] + 3] = -1
                elif i[0] == 3 and i[3] == 2:
                    if i[1] == 0 and i[2] == 0:
                        self.map22[0][1] = -1
                        self.map22[1][1] = -1
                        self.map22[2][1] = -1
                        self.map22[3][1] = -1
                        self.map22[3][0] = -1
                    if i[1] == 0 and i[2] == 9:
                        self.map22[0][8] = -1
                        self.map22[1][8] = -1
                        self.map22[2][8] = -1
                        self.map22[3][8] = -1
                        self.map22[3][9] = -1
                    if i[1] == 7 and i[2] == 0:
                        self.map22[6][0] = -1
                        self.map22[6][1] = -1
                        self.map22[7][1] = -1
                        self.map22[8][1] = -1
                        self.map22[9][1] = -1
                    if i[1] == 7 and i[2] == 9:
                        self.map22[6][9] = -1
                        self.map22[6][8] = -1
                        self.map22[7][8] = -1
                        self.map22[8][8] = -1
                        self.map22[9][8] = -1
                    elif i[1] == 0:
                        self.map22[0][i[2] - 1] = -1
                        self.map22[0][i[2] + 1] = -1
                        self.map22[1][i[2] - 1] = -1
                        self.map22[1][i[2] + 1] = -1
                        self.map22[2][i[2] + 1] = -1
                        self.map22[2][i[2] - 1] = -1
                        self.map22[3][i[2] + 1] = -1
                        self.map22[3][i[2] - 1] = -1
                        self.map22[3][i[2]] = -1
                    elif i[1] == 7:
                        self.map22[9][i[2] - 1] = -1
                        self.map22[9][i[2] + 1] = -1
                        self.map22[8][i[2] - 1] = -1
                        self.map22[8][i[2] + 1] = -1
                        self.map22[7][i[2] - 1] = -1
                        self.map22[7][i[2] + 1] = -1
                        self.map22[6][i[2] - 1] = -1
                        self.map22[6][i[2] + 1] = -1
                        self.map22[6][i[2]] = -1
                    elif i[2] == 0:
                        self.map22[i[1] - 1][0] = -1
                        self.map22[i[1] - 1][1] = -1
                        self.map22[i[1]][1] = -1
                        self.map22[i[1] + 1][1] = -1
                        self.map22[i[1] + 2][1] = -1
                        self.map22[i[1] + 3][1] = -1
                        self.map22[i[1] + 3][0] = -1
                    elif i[2] == 9:
                        self.map22[i[1] - 1][9] = -1
                        self.map22[i[1] - 1][8] = -1
                        self.map22[i[1]][8] = -1
                        self.map22[i[1] + 1][8] = -1
                        self.map22[i[1] + 2][8] = -1
                        self.map22[i[1] + 3][8] = -1
                        self.map22[i[1] + 3][9] = -1
                    else:
                        self.map22[i[1] - 1][i[2] - 1] = -1
                        self.map22[i[1] - 1][i[2]] = -1
                        self.map22[i[1] - 1][i[2] + 1] = -1
                        self.map22[i[1] + 1][i[2] + 1] = -1
                        self.map22[i[1] + 1][i[2] - 1] = -1
                        self.map22[i[1]][i[2] - 1] = -1
                        self.map22[i[1]][i[2] + 2] = -1
                        self.map22[i[1] + 2][i[2] + 1] = -1
                        self.map22[i[1] + 2][i[2] - 1] = -1
                        self.map22[i[1] + 3][i[2] + 1] = -1
                        self.map22[i[1] + 3][i[2] - 1] = -1
                        self.map22[i[1] + 3][i[2]] = -1
                elif i[0] == 4 and i[3] == 1:
                    if i[1] == 0 and i[2] == 0:
                        self.map22[0][4] = -1
                        self.map22[1][0] = -1
                        self.map22[1][1] = -1
                        self.map22[1][2] = -1
                        self.map22[1][3] = -1
                        self.map22[1][4] = -1
                    elif i[1] == 0 and i[2] == 6:
                        self.map22[0][5] = -1
                        self.map22[1][5] = -1
                        self.map22[1][6] = -1
                        self.map22[1][7] = -1
                        self.map22[1][8] = -1
                        self.map22[1][9] = -1
                    elif i[1] == 9 and i[2] == 0:
                        self.map22[8][0] = -1
                        self.map22[8][1] = -1
                        self.map22[8][2] = -1
                        self.map22[8][3] = -1
                        self.map22[8][4] = -1
                        self.map22[9][4] = -1
                    elif i[1] == 9 and i[2] == 6:
                        self.map22[8][5] = -1
                        self.map22[8][6] = -1
                        self.map22[8][7] = -1
                        self.map22[8][8] = -1
                        self.map22[8][9] = -1
                        self.map22[9][5] = -1
                    elif i[1] == 0:
                        self.map22[0][i[2] - 1] = -1
                        self.map22[0][i[2] + 4] = -1
                        self.map22[1][i[2] - 1] = -1
                        self.map22[1][i[2]] = -1
                        self.map22[1][i[2] + 1] = -1
                        self.map22[1][i[2] + 2] = -1
                        self.map22[1][i[2] + 3] = -1
                        self.map22[1][i[2] + 4] = -1
                    elif i[1] == 9:
                        self.map22[9][i[2] - 1] = -1
                        self.map22[9][i[2] + 4] = -1
                        self.map22[8][i[2] - 1] = -1
                        self.map22[8][i[2]] = -1
                        self.map22[8][i[2] + 1] = -1
                        self.map22[8][i[2] + 2] = -1
                        self.map22[8][i[2] + 3] = -1
                        self.map22[8][i[2] + 4] = -1
                    elif i[2] == 0:
                        self.map22[i[1] - 1][0] = -1
                        self.map22[i[1] + 1][0] = -1
                        self.map22[i[1] - 1][1] = -1
                        self.map22[i[1] + 1][1] = -1
                        self.map22[i[1] - 1][2] = -1
                        self.map22[i[1] + 1][2] = -1
                        self.map22[i[1] - 1][3] = -1
                        self.map22[i[1] + 1][3] = -1
                        self.map22[i[1] - 1][4] = -1
                        self.map22[i[1] + 1][4] = -1
                        self.map22[i[1]][4] = -1
                    elif i[2] == 6:
                        self.map22[i[1] - 1][9] = -1
                        self.map22[i[1] + 1][9] = -1
                        self.map22[i[1] - 1][8] = -1
                        self.map22[i[1] + 1][8] = -1
                        self.map22[i[1] - 1][7] = -1
                        self.map22[i[1] + 1][7] = -1
                        self.map22[i[1] - 1][6] = -1
                        self.map22[i[1] + 1][6] = -1
                        self.map22[i[1] - 1][5] = -1
                        self.map22[i[1] + 1][5] = -1
                        self.map22[i[1]][5] = -1
                    else:
                        self.map22[i[1] - 1][i[2] - 1] = -1
                        self.map22[i[1] - 1][i[2]] = -1
                        self.map22[i[1] - 1][i[2] + 1] = -1
                        self.map22[i[1] - 1][i[2] + 2] = -1
                        self.map22[i[1] - 1][i[2] + 3] = -1
                        self.map22[i[1] - 1][i[2] + 4] = -1
                        self.map22[i[1] + 1][i[2] - 1] = -1
                        self.map22[i[1] + 1][i[2]] = -1
                        self.map22[i[1] + 1][i[2] + 1] = -1
                        self.map22[i[1] + 1][i[2] + 2] = -1
                        self.map22[i[1] + 1][i[2] + 3] = -1
                        self.map22[i[1] + 1][i[2] + 4] = -1
                        self.map22[i[1]][i[2] - 1] = -1
                        self.map22[i[1]][i[2] + 4] = -1
                elif i[0] == 4 and i[3] == 2:
                    if i[1] == 0 and i[2] == 0:
                        self.map22[0][1] = -1
                        self.map22[1][1] = -1
                        self.map22[2][1] = -1
                        self.map22[3][1] = -1
                        self.map22[4][1] = -1
                        self.map22[4][0] = -1
                    if i[1] == 0 and i[2] == 9:
                        self.map22[0][8] = -1
                        self.map22[1][8] = -1
                        self.map22[2][8] = -1
                        self.map22[3][8] = -1
                        self.map22[4][8] = -1
                        self.map22[4][9] = -1
                    if i[1] == 6 and i[2] == 0:
                        self.map22[5][0] = -1
                        self.map22[5][1] = -1
                        self.map22[6][1] = -1
                        self.map22[7][1] = -1
                        self.map22[8][1] = -1
                        self.map22[9][1] = -1
                    if i[1] == 6 and i[2] == 9:
                        self.map22[5][9] = -1
                        self.map22[5][8] = -1
                        self.map22[6][8] = -1
                        self.map22[7][8] = -1
                        self.map22[8][8] = -1
                        self.map22[9][8] = -1
                    elif i[1] == 0:
                        self.map22[0][i[2] - 1] = -1
                        self.map22[0][i[2] + 1] = -1
                        self.map22[1][i[2] - 1] = -1
                        self.map22[1][i[2] + 1] = -1
                        self.map22[2][i[2] + 1] = -1
                        self.map22[2][i[2] - 1] = -1
                        self.map22[3][i[2] + 1] = -1
                        self.map22[3][i[2] - 1] = -1
                        self.map22[4][i[2] + 1] = -1
                        self.map22[4][i[2] - 1] = -1
                        self.map22[4][i[2]] = -1
                    elif i[1] == 6:
                        self.map22[9][i[2] - 1] = -1
                        self.map22[9][i[2] + 1] = -1
                        self.map22[8][i[2] - 1] = -1
                        self.map22[8][i[2] + 1] = -1
                        self.map22[7][i[2] - 1] = -1
                        self.map22[7][i[2] + 1] = -1
                        self.map22[6][i[2] - 1] = -1
                        self.map22[6][i[2] + 1] = -1
                        self.map22[5][i[2] - 1] = -1
                        self.map22[5][i[2] + 1] = -1
                        self.map22[5][i[2]] = -1
                    elif i[2] == 0:
                        self.map22[i[1] - 1][0] = -1
                        self.map22[i[1] - 1][1] = -1
                        self.map22[i[1]][1] = -1
                        self.map22[i[1] + 1][1] = -1
                        self.map22[i[1] + 2][1] = -1
                        self.map22[i[1] + 3][1] = -1
                        self.map22[i[1] + 4][1] = -1
                        self.map22[i[1] + 4][0] = -1
                    elif i[2] == 9:
                        self.map22[i[1] - 1][9] = -1
                        self.map22[i[1] - 1][8] = -1
                        self.map22[i[1]][8] = -1
                        self.map22[i[1] + 1][8] = -1
                        self.map22[i[1] + 2][8] = -1
                        self.map22[i[1] + 3][8] = -1
                        self.map22[i[1] + 4][8] = -1
                        self.map22[i[1] + 4][9] = -1
                    else:
                        self.map22[i[1] - 1][i[2] - 1] = -1
                        self.map22[i[1] - 1][i[2]] = -1
                        self.map22[i[1] - 1][i[2] + 1] = -1
                        self.map22[i[1] + 1][i[2] + 1] = -1
                        self.map22[i[1] + 1][i[2] - 1] = -1
                        self.map22[i[1]][i[2] - 1] = -1
                        self.map22[i[1]][i[2] + 2] = -1
                        self.map22[i[1] + 2][i[2] + 1] = -1
                        self.map22[i[1] + 2][i[2] - 1] = -1
                        self.map22[i[1] + 3][i[2] + 1] = -1
                        self.map22[i[1] + 3][i[2] - 1] = -1
                        self.map22[i[1] + 4][i[2] + 1] = -1
                        self.map22[i[1] + 4][i[2] - 1] = -1
                        self.map22[i[1] + 4][i[2]] = -1
            return True
        else:
            return False

    def setmarkship(self, turn, type, x, y, pos):
        if turn == 1:
            if type == 1:
                if x == 0 and y == 0:
                    self.map11[0][1] = -1
                    self.map11[1][0] = -1
                    self.map11[1][1] = -1
                elif x == 0 and y == 9:
                    self.map11[0][8] = -1
                    self.map11[1][8] = -1
                    self.map11[1][9] = -1
                elif x == 9 and y == 0:
                    self.map11[8][0] = -1
                    self.map11[8][1] = -1
                    self.map11[9][1] = -1
                elif x == 9 and y == 9:
                    self.map11[8][8] = -1
                    self.map11[8][9] = -1
                    self.map11[9][8] = -1
                elif x == 0:
                    self.map11[0][y - 1] = -1
                    self.map11[0][y + 1] = -1
                    self.map11[1][y - 1] = -1
                    self.map11[1][y] = -1
                    self.map11[1][y + 1] = -1
                elif x == 9:
                    self.map11[9][y - 1] = -1
                    self.map11[9][y + 1] = -1
                    self.map11[8][y - 1] = -1
                    self.map11[8][y] = -1
                    self.map11[8][y + 1] = -1
                elif y == 0:
                    self.map11[x - 1][0] = -1
                    self.map11[x - 1][1] = -1
                    self.map11[x][1] = -1
                    self.map11[x + 1][0] = -1
                    self.map11[x + 1][1] = -1
                elif y == 9:
                    self.map11[x - 1][9] = -1
                    self.map11[x + 1][9] = -1
                    self.map11[x - 1][8] = -1
                    self.map11[x][8] = -1
                    self.map11[x + 1][8] = -1
                else:
                    self.map11[x - 1][y - 1] = -1
                    self.map11[x - 1][y] = -1
                    self.map11[x - 1][y + 1] = -1
                    self.map11[x][y - 1] = -1
                    self.map11[x][y + 1] = -1
                    self.map11[x + 1][y - 1] = -1
                    self.map11[x + 1][y] = -1
                    self.map11[x + 1][y + 1] = -1
            elif type == 2 and pos == 1:
                if x == 0 and y == 0:
                    self.map11[0][2] = -1
                    self.map11[1][0] = -1
                    self.map11[1][1] = -1
                    self.map11[1][2] = -1
                elif x == 0 and y == 8:
                    self.map11[0][7] = -1
                    self.map11[1][7] = -1
                    self.map11[1][8] = -1
                    self.map11[1][9] = -1
                elif x == 9 and y == 0:
                    self.map11[8][0] = -1
                    self.map11[8][1] = -1
                    self.map11[8][2] = -1
                    self.map11[9][2] = -1
                elif x == 9 and y == 8:
                    self.map11[8][7] = -1
                    self.map11[8][8] = -1
                    self.map11[8][9] = -1
                    self.map11[9][7] = -1
                elif x == 0:
                    self.map11[0][y - 1] = -1
                    self.map11[0][y + 2] = -1
                    self.map11[1][y - 1] = -1
                    self.map11[1][y] = -1
                    self.map11[1][y + 1] = -1
                    self.map11[1][y + 2] = -1
                elif x == 9:
                    self.map11[9][y - 1] = -1
                    self.map11[9][y + 2] = -1
                    self.map11[8][y - 1] = -1
                    self.map11[8][y] = -1
                    self.map11[8][y + 1] = -1
                    self.map11[8][y + 2] = -1
                elif y == 0:
                    self.map11[x - 1][0] = -1
                    self.map11[x + 1][0] = -1
                    self.map11[x - 1][1] = -1
                    self.map11[x + 1][1] = -1
                    self.map11[x - 1][2] = -1
                    self.map11[x + 1][2] = -1
                    self.map11[x][2] = -1
                elif y == 8:
                    self.map11[x - 1][9] = -1
                    self.map11[x + 1][9] = -1
                    self.map11[x - 1][8] = -1
                    self.map11[x + 1][8] = -1
                    self.map11[x - 1][7] = -1
                    self.map11[x + 1][7] = -1
                    self.map11[x][7] = -1
                else:
                    self.map11[x - 1][y - 1] = -1
                    self.map11[x - 1][y] = -1
                    self.map11[x - 1][y + 1] = -1
                    self.map11[x - 1][y + 2] = -1
                    self.map11[x + 1][y - 1] = -1
                    self.map11[x + 1][y] = -1
                    self.map11[x + 1][y + 1] = -1
                    self.map11[x + 1][y + 2] = -1
                    self.map11[x][y - 1] = -1
                    self.map11[x][y + 2] = -1
            elif type == 2 and pos == 2:
                if x == 0 and y == 0:
                    self.map11[0][1] = -1
                    self.map11[1][1] = -1
                    self.map11[2][1] = -1
                    self.map11[2][0] = -1
                elif x == 0 and y == 9:
                    self.map11[0][8] = -1
                    self.map11[1][8] = -1
                    self.map11[2][8] = -1
                    self.map11[2][9] = -1
                elif x == 8 and y == 0:
                    self.map11[7][0] = -1
                    self.map11[7][1] = -1
                    self.map11[8][1] = -1
                    self.map11[9][1] = -1
                elif x == 8 and y == 9:
                    self.map11[7][9] = -1
                    self.map11[7][8] = -1
                    self.map11[8][8] = -1
                    self.map11[9][8] = -1
                elif x == 0:
                    self.map11[0][y - 1] = -1
                    self.map11[0][y + 1] = -1
                    self.map11[1][y - 1] = -1
                    self.map11[1][y + 1] = -1
                    self.map11[2][y - 1] = -1
                    self.map11[2][y + 1] = -1
                    self.map11[2][y] = -1
                elif x == 8:
                    self.map11[9][y - 1] = -1
                    self.map11[9][y + 1] = -1
                    self.map11[8][y - 1] = -1
                    self.map11[8][y + 1] = -1
                    self.map11[7][y - 1] = -1
                    self.map11[7][y + 1] = -1
                    self.map11[7][y] = -1
                elif y == 0:
                    self.map11[x - 1][0] = -1
                    self.map11[x - 1][1] = -1
                    self.map11[x][1] = -1
                    self.map11[x + 1][1] = -1
                    self.map11[x + 2][1] = -1
                    self.map11[x + 2][0] = -1
                elif y == 9:
                    self.map11[x - 1][9] = -1
                    self.map11[x - 1][8] = -1
                    self.map11[x + 1][8] = -1
                    self.map11[x + 2][8] = -1
                    self.map11[x + 2][9] = -1
                    self.map11[x][8] = -1
                else:
                    self.map11[x - 1][y - 1] = -1
                    self.map11[x - 1][y] = -1
                    self.map11[x - 1][y + 1] = -1
                    self.map11[x + 1][y + 1] = -1
                    self.map11[x + 1][y - 1] = -1
                    self.map11[x][y - 1] = -1
                    self.map11[x][y + 2] = -1
                    self.map11[x + 2][y] = -1
                    self.map11[x + 2][y + 1] = -1
                    self.map11[x + 2][y - 1] = -1
            elif type == 3 and pos == 1:
                if x == 0 and y == 0:
                    self.map11[0][3] = -1
                    self.map11[1][0] = -1
                    self.map11[1][1] = -1
                    self.map11[1][2] = -1
                    self.map11[1][3] = -1
                elif x == 0 and y == 7:
                    self.map11[0][6] = -1
                    self.map11[1][6] = -1
                    self.map11[1][7] = -1
                    self.map11[1][8] = -1
                    self.map11[1][9] = -1
                elif x == 9 and y == 0:
                    self.map11[8][0] = -1
                    self.map11[8][1] = -1
                    self.map11[8][2] = -1
                    self.map11[8][3] = -1
                    self.map11[9][3] = -1
                elif x == 9 and y == 7:
                    self.map11[8][6] = -1
                    self.map11[8][7] = -1
                    self.map11[8][8] = -1
                    self.map11[8][9] = -1
                    self.map11[9][6] = -1
                elif x == 0:
                    self.map11[0][y - 1] = -1
                    self.map11[0][y + 3] = -1
                    self.map11[1][y - 1] = -1
                    self.map11[1][y] = -1
                    self.map11[1][y + 1] = -1
                    self.map11[1][y + 2] = -1
                    self.map11[1][y + 3] = -1
                elif x == 9:
                    self.map11[9][y - 1] = -1
                    self.map11[9][y + 3] = -1
                    self.map11[8][y - 1] = -1
                    self.map11[8][y] = -1
                    self.map11[8][y + 1] = -1
                    self.map11[8][y + 2] = -1
                    self.map11[8][y + 3] = -1
                elif y == 0:
                    self.map11[x - 1][0] = -1
                    self.map11[x + 1][0] = -1
                    self.map11[x - 1][1] = -1
                    self.map11[x + 1][1] = -1
                    self.map11[x - 1][2] = -1
                    self.map11[x + 1][2] = -1
                    self.map11[x - 1][3] = -1
                    self.map11[x + 1][3] = -1
                    self.map11[x][3] = -1
                elif y == 7:
                    self.map11[x - 1][9] = -1
                    self.map11[x + 1][9] = -1
                    self.map11[x - 1][8] = -1
                    self.map11[x + 1][8] = -1
                    self.map11[x - 1][7] = -1
                    self.map11[x + 1][7] = -1
                    self.map11[x - 1][6] = -1
                    self.map11[x + 1][6] = -1
                    self.map11[x][6] = -1
                else:
                    self.map11[x - 1][y - 1] = -1
                    self.map11[x - 1][y] = -1
                    self.map11[x - 1][y + 1] = -1
                    self.map11[x - 1][y + 2] = -1
                    self.map11[x - 1][y + 3] = -1
                    self.map11[x + 1][y - 1] = -1
                    self.map11[x + 1][y] = -1
                    self.map11[x + 1][y + 1] = -1
                    self.map11[x + 1][y + 2] = -1
                    self.map11[x + 1][y + 3] = -1
                    self.map11[x][y - 1] = -1
                    self.map11[x][y + 3] = -1
            elif type == 3 and pos == 2:
                if x == 0 and y == 0:
                    self.map11[0][1] = -1
                    self.map11[1][1] = -1
                    self.map11[2][1] = -1
                    self.map11[3][1] = -1
                    self.map11[3][0] = -1
                elif x == 0 and y == 9:
                    self.map11[0][8] = -1
                    self.map11[1][8] = -1
                    self.map11[2][8] = -1
                    self.map11[3][8] = -1
                    self.map11[3][9] = -1
                elif x == 7 and y == 0:
                    self.map11[6][0] = -1
                    self.map11[6][1] = -1
                    self.map11[7][1] = -1
                    self.map11[8][1] = -1
                    self.map11[9][1] = -1
                elif x == 7 and y == 9:
                    self.map11[6][9] = -1
                    self.map11[6][8] = -1
                    self.map11[7][8] = -1
                    self.map11[8][8] = -1
                    self.map11[9][8] = -1
                elif x == 0:
                    self.map11[0][y - 1] = -1
                    self.map11[0][y + 1] = -1
                    self.map11[1][y - 1] = -1
                    self.map11[1][y + 1] = -1
                    self.map11[2][y + 1] = -1
                    self.map11[2][y - 1] = -1
                    self.map11[3][y + 1] = -1
                    self.map11[3][y - 1] = -1
                    self.map11[3][y] = -1
                elif x == 7:
                    self.map11[9][y - 1] = -1
                    self.map11[9][y + 1] = -1
                    self.map11[8][y - 1] = -1
                    self.map11[8][y + 1] = -1
                    self.map11[7][y - 1] = -1
                    self.map11[7][y + 1] = -1
                    self.map11[6][y - 1] = -1
                    self.map11[6][y + 1] = -1
                    self.map11[6][y] = -1
                elif y == 0:
                    self.map11[x - 1][0] = -1
                    self.map11[x - 1][1] = -1
                    self.map11[x][1] = -1
                    self.map11[x + 1][1] = -1
                    self.map11[x + 2][1] = -1
                    self.map11[x + 3][1] = -1
                    self.map11[x + 3][0] = -1
                elif y == 9:
                    self.map11[x - 1][9] = -1
                    self.map11[x - 1][8] = -1
                    self.map11[x][8] = -1
                    self.map11[x + 1][8] = -1
                    self.map11[x + 2][8] = -1
                    self.map11[x + 3][8] = -1
                    self.map11[x + 3][9] = -1
                else:
                    self.map11[x - 1][y - 1] = -1
                    self.map11[x - 1][y] = -1
                    self.map11[x - 1][y + 1] = -1
                    self.map11[x + 1][y + 1] = -1
                    self.map11[x + 1][y - 1] = -1
                    self.map11[x][y - 1] = -1
                    self.map11[x][y + 2] = -1
                    self.map11[x + 2][y + 1] = -1
                    self.map11[x + 2][y - 1] = -1
                    self.map11[x + 3][y + 1] = -1
                    self.map11[x + 3][y - 1] = -1
                    self.map11[x + 3][y] = -1
            elif type == 4 and pos == 1:
                if x == 0 and y == 0:
                    self.map11[0][4] = -1
                    self.map11[1][0] = -1
                    self.map11[1][1] = -1
                    self.map11[1][2] = -1
                    self.map11[1][3] = -1
                    self.map11[1][4] = -1
                elif x == 0 and y == 6:
                    self.map11[0][5] = -1
                    self.map11[1][5] = -1
                    self.map11[1][6] = -1
                    self.map11[1][7] = -1
                    self.map11[1][8] = -1
                    self.map11[1][9] = -1
                elif x == 9 and y == 0:
                    self.map11[8][0] = -1
                    self.map11[8][1] = -1
                    self.map11[8][2] = -1
                    self.map11[8][3] = -1
                    self.map11[8][4] = -1
                    self.map11[9][4] = -1
                elif x == 9 and y == 6:
                    self.map11[8][5] = -1
                    self.map11[8][6] = -1
                    self.map11[8][7] = -1
                    self.map11[8][8] = -1
                    self.map11[8][9] = -1
                    self.map11[9][5] = -1
                elif x == 0:
                    self.map11[0][y - 1] = -1
                    self.map11[0][y + 4] = -1
                    self.map11[1][y - 1] = -1
                    self.map11[1][y] = -1
                    self.map11[1][y + 1] = -1
                    self.map11[1][y + 2] = -1
                    self.map11[1][y + 3] = -1
                    self.map11[1][y + 4] = -1
                elif x == 9:
                    self.map11[9][y - 1] = -1
                    self.map11[9][y + 4] = -1
                    self.map11[8][y - 1] = -1
                    self.map11[8][y] = -1
                    self.map11[8][y + 1] = -1
                    self.map11[8][y + 2] = -1
                    self.map11[8][y + 3] = -1
                    self.map11[8][y + 4] = -1
                elif y == 0:
                    self.map11[x - 1][0] = -1
                    self.map11[x + 1][0] = -1
                    self.map11[x - 1][1] = -1
                    self.map11[x + 1][1] = -1
                    self.map11[x - 1][2] = -1
                    self.map11[x + 1][2] = -1
                    self.map11[x - 1][3] = -1
                    self.map11[x + 1][3] = -1
                    self.map11[x - 1][4] = -1
                    self.map11[x + 1][4] = -1
                    self.map11[x][4] = -1
                elif y == 6:
                    self.map11[x - 1][9] = -1
                    self.map11[x + 1][9] = -1
                    self.map11[x - 1][8] = -1
                    self.map11[x + 1][8] = -1
                    self.map11[x - 1][7] = -1
                    self.map11[x + 1][7] = -1
                    self.map11[x - 1][6] = -1
                    self.map11[x + 1][6] = -1
                    self.map11[x - 1][5] = -1
                    self.map11[x + 1][5] = -1
                    self.map11[x][5] = -1
                else:
                    self.map11[x - 1][y - 1] = -1
                    self.map11[x - 1][y] = -1
                    self.map11[x - 1][y + 1] = -1
                    self.map11[x - 1][y + 2] = -1
                    self.map11[x - 1][y + 3] = -1
                    self.map11[x - 1][y + 4] = -1
                    self.map11[x + 1][y - 1] = -1
                    self.map11[x + 1][y] = -1
                    self.map11[x + 1][y + 1] = -1
                    self.map11[x + 1][y + 2] = -1
                    self.map11[x + 1][y + 3] = -1
                    self.map11[x + 1][y + 4] = -1
                    self.map11[x][y - 1] = -1
                    self.map11[x][y + 4] = -1
            elif type == 4 and pos == 2:
                if x == 0 and y == 0:
                    self.map11[0][1] = -1
                    self.map11[1][1] = -1
                    self.map11[2][1] = -1
                    self.map11[3][1] = -1
                    self.map11[4][1] = -1
                    self.map11[4][0] = -1
                elif x == 0 and y == 9:
                    self.map11[0][8] = -1
                    self.map11[1][8] = -1
                    self.map11[2][8] = -1
                    self.map11[3][8] = -1
                    self.map11[4][8] = -1
                    self.map11[4][9] = -1
                elif x == 6 and y == 0:
                    self.map11[5][0] = -1
                    self.map11[5][1] = -1
                    self.map11[6][1] = -1
                    self.map11[7][1] = -1
                    self.map11[8][1] = -1
                    self.map11[9][1] = -1
                elif x == 6 and y == 9:
                    self.map11[5][9] = -1
                    self.map11[5][8] = -1
                    self.map11[6][8] = -1
                    self.map11[7][8] = -1
                    self.map11[8][8] = -1
                    self.map11[9][8] = -1
                elif x == 0:
                    self.map11[0][y - 1] = -1
                    self.map11[0][y + 1] = -1
                    self.map11[1][y - 1] = -1
                    self.map11[1][y + 1] = -1
                    self.map11[2][y + 1] = -1
                    self.map11[2][y - 1] = -1
                    self.map11[3][y + 1] = -1
                    self.map11[3][y - 1] = -1
                    self.map11[4][y + 1] = -1
                    self.map11[4][y - 1] = -1
                    self.map11[4][y] = -1
                elif x == 6:
                    self.map11[9][y - 1] = -1
                    self.map11[9][y + 1] = -1
                    self.map11[8][y - 1] = -1
                    self.map11[8][y + 1] = -1
                    self.map11[7][y - 1] = -1
                    self.map11[7][y + 1] = -1
                    self.map11[6][y - 1] = -1
                    self.map11[6][y + 1] = -1
                    self.map11[5][y - 1] = -1
                    self.map11[5][y + 1] = -1
                    self.map11[5][y] = -1
                elif y == 0:
                    self.map11[x - 1][0] = -1
                    self.map11[x - 1][1] = -1
                    self.map11[x][1] = -1
                    self.map11[x + 1][1] = -1
                    self.map11[x + 2][1] = -1
                    self.map11[x + 3][1] = -1
                    self.map11[x + 4][1] = -1
                    self.map11[x + 4][0] = -1
                elif y == 9:
                    self.map11[x - 1][9] = -1
                    self.map11[x - 1][8] = -1
                    self.map11[x][8] = -1
                    self.map11[x + 1][8] = -1
                    self.map11[x + 2][8] = -1
                    self.map11[x + 3][8] = -1
                    self.map11[x + 4][8] = -1
                    self.map11[x + 4][9] = -1
                else:
                    self.map11[x - 1][y - 1] = -1
                    self.map11[x - 1][y] = -1
                    self.map11[x - 1][y + 1] = -1
                    self.map11[x + 1][y + 1] = -1
                    self.map11[x + 1][y - 1] = -1
                    self.map11[x][y - 1] = -1
                    self.map11[x][y + 2] = -1
                    self.map11[x + 2][y + 1] = -1
                    self.map11[x + 2][y - 1] = -1
                    self.map11[x + 3][y + 1] = -1
                    self.map11[x + 3][y - 1] = -1
                    self.map11[x + 4][y + 1] = -1
                    self.map11[x + 4][y - 1] = -1
                    self.map11[x + 4][y] = -1
            return True
        elif turn == 2:
            if type == 1:
                if x == 0 and y == 0:
                    self.map22[0][1] = -1
                    self.map22[1][0] = -1
                    self.map22[1][1] = -1
                elif x == 0 and y == 9:
                    self.map22[0][8] = -1
                    self.map22[1][8] = -1
                    self.map22[1][9] = -1
                elif x == 9 and y == 0:
                    self.map22[8][0] = -1
                    self.map22[8][1] = -1
                    self.map22[9][1] = -1
                elif x == 9 and y == 9:
                    self.map22[8][8] = -1
                    self.map22[8][9] = -1
                    self.map22[9][8] = -1
                elif x == 0:
                    self.map22[0][y - 1] = -1
                    self.map22[0][y + 1] = -1
                    self.map22[1][y - 1] = -1
                    self.map22[1][y] = -1
                    self.map22[1][y + 1] = -1
                elif x == 9:
                    self.map22[9][y - 1] = -1
                    self.map22[9][y + 1] = -1
                    self.map22[8][y - 1] = -1
                    self.map22[8][y] = -1
                    self.map22[8][y + 1] = -1
                elif y == 0:
                    self.map22[x - 1][0] = -1
                    self.map22[x - 1][1] = -1
                    self.map22[x][1] = -1
                    self.map22[x + 1][0] = -1
                    self.map22[x + 1][1] = -1
                elif y == 9:
                    self.map22[x - 1][9] = -1
                    self.map22[x + 1][9] = -1
                    self.map22[x - 1][8] = -1
                    self.map22[x][8] = -1
                    self.map22[x + 1][8] = -1
                else:
                    self.map22[x - 1][y - 1] = -1
                    self.map22[x - 1][y] = -1
                    self.map22[x - 1][y + 1] = -1
                    self.map22[x][y - 1] = -1
                    self.map22[x][y + 1] = -1
                    self.map22[x + 1][y - 1] = -1
                    self.map22[x + 1][y] = -1
                    self.map22[x + 1][y + 1] = -1
            elif type == 2 and pos == 1:
                if x == 0 and y == 0:
                    self.map22[0][2] = -1
                    self.map22[1][0] = -1
                    self.map22[1][1] = -1
                    self.map22[1][2] = -1
                elif x == 0 and y == 8:
                    self.map22[0][7] = -1
                    self.map22[1][7] = -1
                    self.map22[1][8] = -1
                    self.map22[1][9] = -1
                elif x == 9 and y == 0:
                    self.map22[8][0] = -1
                    self.map22[8][1] = -1
                    self.map22[8][2] = -1
                    self.map22[9][2] = -1
                elif x == 9 and y == 8:
                    self.map22[8][7] = -1
                    self.map22[8][8] = -1
                    self.map22[8][9] = -1
                    self.map22[9][7] = -1
                elif x == 0:
                    self.map22[0][y - 1] = -1
                    self.map22[0][y + 2] = -1
                    self.map22[1][y - 1] = -1
                    self.map22[1][y] = -1
                    self.map22[1][y + 1] = -1
                    self.map22[1][y + 2] = -1
                elif x == 9:
                    self.map22[9][y - 1] = -1
                    self.map22[9][y + 2] = -1
                    self.map22[8][y - 1] = -1
                    self.map22[8][y] = -1
                    self.map22[8][y + 1] = -1
                    self.map22[8][y + 2] = -1
                elif y == 0:
                    self.map22[x - 1][0] = -1
                    self.map22[x + 1][0] = -1
                    self.map22[x - 1][1] = -1
                    self.map22[x + 1][1] = -1
                    self.map22[x - 1][2] = -1
                    self.map22[x + 1][2] = -1
                    self.map22[x][2] = -1
                elif y == 8:
                    self.map22[x - 1][9] = -1
                    self.map22[x + 1][9] = -1
                    self.map22[x - 1][8] = -1
                    self.map22[x + 1][8] = -1
                    self.map22[x - 1][7] = -1
                    self.map22[x + 1][7] = -1
                    self.map22[x][7] = -1
                else:
                    self.map22[x - 1][y - 1] = -1
                    self.map22[x - 1][y] = -1
                    self.map22[x - 1][y + 1] = -1
                    self.map22[x - 1][y + 2] = -1
                    self.map22[x + 1][y - 1] = -1
                    self.map22[x + 1][y] = -1
                    self.map22[x + 1][y + 1] = -1
                    self.map22[x + 1][y + 2] = -1
                    self.map22[x][y - 1] = -1
                    self.map22[x][y + 2] = -1
            elif type == 2 and pos == 2:
                if x == 0 and y == 0:
                    self.map22[0][1] = -1
                    self.map22[1][1] = -1
                    self.map22[2][1] = -1
                    self.map22[2][0] = -1
                elif x == 0 and y == 9:
                    self.map22[0][8] = -1
                    self.map22[1][8] = -1
                    self.map22[2][8] = -1
                    self.map22[2][9] = -1
                elif x == 8 and y == 0:
                    self.map22[7][0] = -1
                    self.map22[7][1] = -1
                    self.map22[8][1] = -1
                    self.map22[9][1] = -1
                elif x == 8 and y == 9:
                    self.map22[7][9] = -1
                    self.map22[7][8] = -1
                    self.map22[8][8] = -1
                    self.map22[9][8] = -1
                elif x == 0:
                    self.map22[0][y - 1] = -1
                    self.map22[0][y + 1] = -1
                    self.map22[1][y - 1] = -1
                    self.map22[1][y + 1] = -1
                    self.map22[2][y - 1] = -1
                    self.map22[2][y + 1] = -1
                    self.map22[2][y] = -1
                elif x == 8:
                    self.map22[9][y - 1] = -1
                    self.map22[9][y + 1] = -1
                    self.map22[8][y - 1] = -1
                    self.map22[8][y + 1] = -1
                    self.map22[7][y - 1] = -1
                    self.map22[7][y + 1] = -1
                    self.map22[7][y] = -1
                elif y == 0:
                    self.map22[x - 1][0] = -1
                    self.map22[x - 1][1] = -1
                    self.map22[x][1] = -1
                    self.map22[x + 1][1] = -1
                    self.map22[x + 2][1] = -1
                    self.map22[x + 2][0] = -1
                elif y == 9:
                    self.map22[x - 1][9] = -1
                    self.map22[x - 1][8] = -1
                    self.map22[x + 1][8] = -1
                    self.map22[x + 2][8] = -1
                    self.map22[x + 2][9] = -1
                    self.map22[x][8] = -1
                else:
                    self.map22[x - 1][y - 1] = -1
                    self.map22[x - 1][y] = -1
                    self.map22[x - 1][y + 1] = -1
                    self.map22[x + 1][y + 1] = -1
                    self.map22[x + 1][y - 1] = -1
                    self.map22[x][y - 1] = -1
                    self.map22[x][y + 2] = -1
                    self.map22[x + 2][y] = -1
                    self.map22[x + 2][y + 1] = -1
                    self.map22[x + 2][y - 1] = -1
            elif type == 3 and pos == 1:
                if x == 0 and y == 0:
                    self.map22[0][3] = -1
                    self.map22[1][0] = -1
                    self.map22[1][1] = -1
                    self.map22[1][2] = -1
                    self.map22[1][3] = -1
                elif x == 0 and y == 7:
                    self.map22[0][6] = -1
                    self.map22[1][6] = -1
                    self.map22[1][7] = -1
                    self.map22[1][8] = -1
                    self.map22[1][9] = -1
                elif x == 9 and y == 0:
                    self.map22[8][0] = -1
                    self.map22[8][1] = -1
                    self.map22[8][2] = -1
                    self.map22[8][3] = -1
                    self.map22[9][3] = -1
                elif x == 9 and y == 7:
                    self.map22[8][6] = -1
                    self.map22[8][7] = -1
                    self.map22[8][8] = -1
                    self.map22[8][9] = -1
                    self.map22[9][6] = -1
                elif x == 0:
                    self.map22[0][y - 1] = -1
                    self.map22[0][y + 3] = -1
                    self.map22[1][y - 1] = -1
                    self.map22[1][y] = -1
                    self.map22[1][y + 1] = -1
                    self.map22[1][y + 2] = -1
                    self.map22[1][y + 3] = -1
                elif x == 9:
                    self.map22[9][y - 1] = -1
                    self.map22[9][y + 3] = -1
                    self.map22[8][y - 1] = -1
                    self.map22[8][y] = -1
                    self.map22[8][y + 1] = -1
                    self.map22[8][y + 2] = -1
                    self.map22[8][y + 3] = -1
                elif y == 0:
                    self.map22[x - 1][0] = -1
                    self.map22[x + 1][0] = -1
                    self.map22[x - 1][1] = -1
                    self.map22[x + 1][1] = -1
                    self.map22[x - 1][2] = -1
                    self.map22[x + 1][2] = -1
                    self.map22[x - 1][3] = -1
                    self.map22[x + 1][3] = -1
                    self.map22[x][3] = -1
                elif y == 7:
                    self.map22[x - 1][9] = -1
                    self.map22[x + 1][9] = -1
                    self.map22[x - 1][8] = -1
                    self.map22[x + 1][8] = -1
                    self.map22[x - 1][7] = -1
                    self.map22[x + 1][7] = -1
                    self.map22[x - 1][6] = -1
                    self.map22[x + 1][6] = -1
                    self.map22[x][6] = -1
                else:
                    self.map22[x - 1][y - 1] = -1
                    self.map22[x - 1][y] = -1
                    self.map22[x - 1][y + 1] = -1
                    self.map22[x - 1][y + 2] = -1
                    self.map22[x - 1][y + 3] = -1
                    self.map22[x + 1][y - 1] = -1
                    self.map22[x + 1][y] = -1
                    self.map22[x + 1][y + 1] = -1
                    self.map22[x + 1][y + 2] = -1
                    self.map22[x + 1][y + 3] = -1
                    self.map22[x][y - 1] = -1
                    self.map22[x][y + 3] = -1
            elif type == 3 and pos == 2:
                if x == 0 and y == 0:
                    self.map22[0][1] = -1
                    self.map22[1][1] = -1
                    self.map22[2][1] = -1
                    self.map22[3][1] = -1
                    self.map22[3][0] = -1
                elif x == 0 and y == 9:
                    self.map22[0][8] = -1
                    self.map22[1][8] = -1
                    self.map22[2][8] = -1
                    self.map22[3][8] = -1
                    self.map22[3][9] = -1
                elif x == 7 and y == 0:
                    self.map22[6][0] = -1
                    self.map22[6][1] = -1
                    self.map22[7][1] = -1
                    self.map22[8][1] = -1
                    self.map22[9][1] = -1
                elif x == 7 and y == 9:
                    self.map22[6][9] = -1
                    self.map22[6][8] = -1
                    self.map22[7][8] = -1
                    self.map22[8][8] = -1
                    self.map22[9][8] = -1
                elif x == 0:
                    self.map22[0][y - 1] = -1
                    self.map22[0][y + 1] = -1
                    self.map22[1][y - 1] = -1
                    self.map22[1][y + 1] = -1
                    self.map22[2][y + 1] = -1
                    self.map22[2][y - 1] = -1
                    self.map22[3][y + 1] = -1
                    self.map22[3][y - 1] = -1
                    self.map22[3][y] = -1
                elif x == 7:
                    self.map22[9][y - 1] = -1
                    self.map22[9][y + 1] = -1
                    self.map22[8][y - 1] = -1
                    self.map22[8][y + 1] = -1
                    self.map22[7][y - 1] = -1
                    self.map22[7][y + 1] = -1
                    self.map22[6][y - 1] = -1
                    self.map22[6][y + 1] = -1
                    self.map22[6][y] = -1
                elif y == 0:
                    self.map22[x - 1][0] = -1
                    self.map22[x - 1][1] = -1
                    self.map22[x][1] = -1
                    self.map22[x + 1][1] = -1
                    self.map22[x + 2][1] = -1
                    self.map22[x + 3][1] = -1
                    self.map22[x + 3][0] = -1
                elif y == 9:
                    self.map22[x - 1][9] = -1
                    self.map22[x - 1][8] = -1
                    self.map22[x][8] = -1
                    self.map22[x + 1][8] = -1
                    self.map22[x + 2][8] = -1
                    self.map22[x + 3][8] = -1
                    self.map22[x + 3][9] = -1
                else:
                    self.map22[x - 1][y - 1] = -1
                    self.map22[x - 1][y] = -1
                    self.map22[x - 1][y + 1] = -1
                    self.map22[x + 1][y + 1] = -1
                    self.map22[x + 1][y - 1] = -1
                    self.map22[x][y - 1] = -1
                    self.map22[x][y + 2] = -1
                    self.map22[x + 2][y + 1] = -1
                    self.map22[x + 2][y - 1] = -1
                    self.map22[x + 3][y + 1] = -1
                    self.map22[x + 3][y - 1] = -1
                    self.map22[x + 3][y] = -1
            elif type == 4 and pos == 1:
                if x == 0 and y == 0:
                    self.map22[0][4] = -1
                    self.map22[1][0] = -1
                    self.map22[1][1] = -1
                    self.map22[1][2] = -1
                    self.map22[1][3] = -1
                    self.map22[1][4] = -1
                elif x == 0 and y == 6:
                    self.map22[0][5] = -1
                    self.map22[1][5] = -1
                    self.map22[1][6] = -1
                    self.map22[1][7] = -1
                    self.map22[1][8] = -1
                    self.map22[1][9] = -1
                elif x == 9 and y == 0:
                    self.map22[8][0] = -1
                    self.map22[8][1] = -1
                    self.map22[8][2] = -1
                    self.map22[8][3] = -1
                    self.map22[8][4] = -1
                    self.map22[9][4] = -1
                elif x == 9 and y == 6:
                    self.map22[8][5] = -1
                    self.map22[8][6] = -1
                    self.map22[8][7] = -1
                    self.map22[8][8] = -1
                    self.map22[8][9] = -1
                    self.map22[9][5] = -1
                elif x == 0:
                    self.map22[0][y - 1] = -1
                    self.map22[0][y + 4] = -1
                    self.map22[1][y - 1] = -1
                    self.map22[1][y] = -1
                    self.map22[1][y + 1] = -1
                    self.map22[1][y + 2] = -1
                    self.map22[1][y + 3] = -1
                    self.map22[1][y + 4] = -1
                elif x == 9:
                    self.map22[9][y - 1] = -1
                    self.map22[9][y + 4] = -1
                    self.map22[8][y - 1] = -1
                    self.map22[8][y] = -1
                    self.map22[8][y + 1] = -1
                    self.map22[8][y + 2] = -1
                    self.map22[8][y + 3] = -1
                    self.map22[8][y + 4] = -1
                elif y == 0:
                    self.map22[x - 1][0] = -1
                    self.map22[x + 1][0] = -1
                    self.map22[x - 1][1] = -1
                    self.map22[x + 1][1] = -1
                    self.map22[x - 1][2] = -1
                    self.map22[x + 1][2] = -1
                    self.map22[x - 1][3] = -1
                    self.map22[x + 1][3] = -1
                    self.map22[x - 1][4] = -1
                    self.map22[x + 1][4] = -1
                    self.map22[x][4] = -1
                elif y == 6:
                    self.map22[x - 1][9] = -1
                    self.map22[x + 1][9] = -1
                    self.map22[x - 1][8] = -1
                    self.map22[x + 1][8] = -1
                    self.map22[x - 1][7] = -1
                    self.map22[x + 1][7] = -1
                    self.map22[x - 1][6] = -1
                    self.map22[x + 1][6] = -1
                    self.map22[x - 1][5] = -1
                    self.map22[x + 1][5] = -1
                    self.map22[x][5] = -1
                else:
                    self.map22[x - 1][y - 1] = -1
                    self.map22[x - 1][y] = -1
                    self.map22[x - 1][y + 1] = -1
                    self.map22[x - 1][y + 2] = -1
                    self.map22[x - 1][y + 3] = -1
                    self.map22[x - 1][y + 4] = -1
                    self.map22[x + 1][y - 1] = -1
                    self.map22[x + 1][y] = -1
                    self.map22[x + 1][y + 1] = -1
                    self.map22[x + 1][y + 2] = -1
                    self.map22[x + 1][y + 3] = -1
                    self.map22[x + 1][y + 4] = -1
                    self.map22[x][y - 1] = -1
                    self.map22[x][y + 4] = -1
            elif type == 4 and pos == 2:
                if x == 0 and y == 0:
                    self.map22[0][1] = -1
                    self.map22[1][1] = -1
                    self.map22[2][1] = -1
                    self.map22[3][1] = -1
                    self.map22[4][1] = -1
                    self.map22[4][0] = -1
                elif x == 0 and y == 9:
                    self.map22[0][8] = -1
                    self.map22[1][8] = -1
                    self.map22[2][8] = -1
                    self.map22[3][8] = -1
                    self.map22[4][8] = -1
                    self.map22[4][9] = -1
                elif x == 6 and y == 0:
                    self.map22[5][0] = -1
                    self.map22[5][1] = -1
                    self.map22[6][1] = -1
                    self.map22[7][1] = -1
                    self.map22[8][1] = -1
                    self.map22[9][1] = -1
                elif x == 6 and y == 9:
                    self.map22[5][9] = -1
                    self.map22[5][8] = -1
                    self.map22[6][8] = -1
                    self.map22[7][8] = -1
                    self.map22[8][8] = -1
                    self.map22[9][8] = -1
                elif x == 0:
                    self.map22[0][y - 1] = -1
                    self.map22[0][y + 1] = -1
                    self.map22[1][y - 1] = -1
                    self.map22[1][y + 1] = -1
                    self.map22[2][y + 1] = -1
                    self.map22[2][y - 1] = -1
                    self.map22[3][y + 1] = -1
                    self.map22[3][y - 1] = -1
                    self.map22[4][y + 1] = -1
                    self.map22[4][y - 1] = -1
                    self.map22[4][y] = -1
                elif x == 6:
                    self.map22[9][y - 1] = -1
                    self.map22[9][y + 1] = -1
                    self.map22[8][y - 1] = -1
                    self.map22[8][y + 1] = -1
                    self.map22[7][y - 1] = -1
                    self.map22[7][y + 1] = -1
                    self.map22[6][y - 1] = -1
                    self.map22[6][y + 1] = -1
                    self.map22[5][y - 1] = -1
                    self.map22[5][y + 1] = -1
                    self.map22[5][y] = -1
                elif y == 0:
                    self.map22[x - 1][0] = -1
                    self.map22[x - 1][1] = -1
                    self.map22[x][1] = -1
                    self.map22[x + 1][1] = -1
                    self.map22[x + 2][1] = -1
                    self.map22[x + 3][1] = -1
                    self.map22[x + 4][1] = -1
                    self.map22[x + 4][0] = -1
                elif y == 9:
                    self.map22[x - 1][9] = -1
                    self.map22[x - 1][8] = -1
                    self.map22[x][8] = -1
                    self.map22[x + 1][8] = -1
                    self.map22[x + 2][8] = -1
                    self.map22[x + 3][8] = -1
                    self.map22[x + 4][8] = -1
                    self.map22[x + 4][9] = -1
                else:
                    self.map22[x - 1][y - 1] = -1
                    self.map22[x - 1][y] = -1
                    self.map22[x - 1][y + 1] = -1
                    self.map22[x + 1][y + 1] = -1
                    self.map22[x + 1][y - 1] = -1
                    self.map22[x][y - 1] = -1
                    self.map22[x][y + 2] = -1
                    self.map22[x + 2][y + 1] = -1
                    self.map22[x + 2][y - 1] = -1
                    self.map22[x + 3][y + 1] = -1
                    self.map22[x + 3][y - 1] = -1
                    self.map22[x + 4][y + 1] = -1
                    self.map22[x + 4][y - 1] = -1
                    self.map22[x + 4][y] = -1
            return True
        return False

    def setup(self, turn, posx, posy, type, pos):
        if not self.prepare:
            return False
        elif not self.check(turn, posx - 1, posy - 1, type, pos):
            return False
        else:
            self.setmarkship(turn, type, posx - 1, posy - 1, pos)
            if turn == 1:
                self.map1.append([type, posx - 1, posy - 1, pos])
                self.ll1[type - 1] += 1
                if pos == 1:
                    for i in range(posy - 1, posy + type - 1):
                        self.map11[posx - 1][i] = type
                else:
                    for i in range(posx - 1, posx + type - 1):
                        self.map11[i][posy - 1] = type
            else:
                self.map2.append([type, posx - 1, posy - 1, pos])
                self.ll2[type - 1] += 1
                if pos == 1:
                    for i in range(posy - 1, posy + type - 1):
                        self.map22[posx - 1][i] = type
                else:
                    for i in range(posx - 1, posx + type - 1):
                        self.map22[i][posy - 1] = type
        return True

    def start(self):
        if self.check1() and self.check2():
            self.prepare = False
            return True
        return False

    def check1(self):
        if len(self.map1) == 10:
            return True
        return False

    def check2(self):
        if len(self.map2) == 10:
            return True
        return False

    def win(self):
        if max(self.ll1) == 0:
            return 2
        elif max(self.ll2) == 0:
            return 1
        else:
            return 3

    def hit(self, x, y):
        if self.prepare:
            return -1
        if self.turn == 1:
            if self.map22[x - 1][y - 1] == 1 or self.map22[x - 1][y - 1] == 2 or self.map22[x - 1][y - 1] == 3 or self.map22[x - 1][y - 1] == 4:
                self.map22[x - 1][y - 1] += 4
                self.map12[x - 1][y - 1] = 'X'
                return 2
            else:
                self.map22[x - 1][y - 1] = -2
                self.map12[x - 1][y - 1] = '*'
                self.turn = 2
                return 1
        else:
            if self.map11[x - 1][y - 1] == 1 or self.map11[x - 1][y - 1] == 2 or self.map11[x - 1][y - 1] == 3 or self.map11[x - 1][y - 1] == 4:
                self.map11[x - 1][y - 1] += 4
                self.map21[x - 1][y - 1] = 'X'
                return 2
            else:
                self.map11[x - 1][y - 1] = -2
                self.map21[x - 1][y - 1] = '*'
                self.turn = 1
                return 1

    def decript(self, s, f=False):
        if s[0] == 'A' or s[0] == 'А':
            x = 1
        elif s[0] == 'B' or s[0] == 'Б':
            x = 2
        elif s[0] == 'C' or s[0] == 'В':
            x = 3
        elif s[0] == 'D' or s[0] == 'Г':
            x = 4
        elif s[0] == 'E' or s[0] == 'Д':
            x = 5
        elif s[0] == 'F' or s[0] == 'Е':
            x = 6
        elif s[0] == 'G' or s[0] == 'Ж':
            x = 7
        elif s[0] == 'H' or s[0] == 'З':
            x = 8
        elif s[0] == 'I' or s[0] == 'И':
            x = 9
        elif s[0] == 'J' or s[0] == 'К':
            x = 10
        else:
            return -1, -1
        if not f:
            try:
                y = int(s[1:])
            except ValueError:
                return -1, -1
            return x, y
        else:
            return x

    def ids(self):
        return [self.turn1, self.turn2]

    def map(self, turn):
        m1, m2 = [], []
        if turn == 1:
            for i in self.map11:
                s = []
                for j in i:
                    if j == -1 or j == 0:
                        s.append(' ')
                    elif j == -2:
                        s.append('*')
                    elif j > 4:
                        s.append("X")
                    else:
                        s.append(j)
                m1.append(s)
            for i in self.map22:
                s = []
                for j in i:
                    if j == -1 or j == 0:
                        s.append(' ')
                    elif j == -2:
                        s.append('*')
                    elif j > 4:
                        s.append("X")
                    else:
                        s.append(" ")
                m2.append(s)
        elif turn == 2:
            for i in self.map22:
                s = []
                for j in i:
                    if j == -1 or j == 0:
                        s.append(' ')
                    elif j == -2:
                        s.append('*')
                    elif j > 4:
                        s.append("X")
                    else:
                        s.append(j)
                m1.append(s)
            for i in self.map11:
                s = []
                for j in i:
                    if j == -1 or j == 0:
                        s.append(' ')
                    elif j == -2:
                        s.append('*')
                    elif j > 4:
                        s.append("X")
                    else:
                        s.append(' ')
                m2.append(s)
        return m1, m2

    def turn(self):
        return self.turn


if __name__ == "__main__":
    battle = Battle(1, 3)
    f1, f2 = False, False
    print("Первый игрок:")
    while not battle.check1():
        s = input(
            'Напиши позицию "головы"(A1, B2), тип коробля(1-4) и горизонатльно(1) или вертикально(2) он расположен\n').split()
        if len(s) == 3:
            x, y = battle.decript(s[0])
            try:
                if x != -1 or y != -1 or (int(s[2]) != 1 and int(s[2]) != 2) or (
                        int(s[1]) != 1 and int(s[1]) != 2 and int(s[1]) != 3 and int(s[1]) != 4):
                    t, x, y, type, pos = 1, x, y, int(s[1]), int(s[2])
                    f = battle.setup(t, x, y, type, pos)
                    if f is False:
                        print("Невозможно!")
                    m1 = battle.map(1)[0]
                    print(*m1, sep='\n')
                else:
                    print("Неверная информация")
            except ValueError:
                print("Неверная информация")
        else:
            print("Неверная информация")
    print("Второй игрок:")
    while not battle.check2():
        s = input(
            'Напиши позицию "головы"(A1, B2), тип коробля(1-4) и горизонатльно(1) или вертикально(2) он расположен\n').split()
        if len(s) == 3:
            x, y = battle.decript(s[0])
            try:
                if x != -1 or y != -1 or (int(s[2]) != 1 and int(s[2]) != 2) or (
                        int(s[1]) != 1 and int(s[1]) != 2 and int(s[1]) != 3 and int(s[1]) != 4):
                    t, x, y, type, pos = 2, x, y, int(s[1]), int(s[2])
                    f = battle.setup(t, x, y, type, pos)
                    if f is False:
                        print("Невозможно!")
                    m1 = battle.map(2)[0]
                    print(*m1, sep='\n')
                else:
                    print("Неверная информация")
            except ValueError:
                print("Неверная информация")
        else:
            print("Неверная информация")
    # f2 = battle.setup(1, 6, 6, 4, 1)  # кто ходит, х, у, раазмер, горизонтально или вертикально
    battle.start()
    while battle.win() == 3:
        if battle.turn == 1:
            print("Игрок 1:")
            m1, m2 = battle.map(1)
            print(*m1, sep='\n')
            print("Игрок 2:")
            print(*m2, sep='\n')
            print("Напишите координаты атаки:")
            s = input()
            while not(len(s) == 2 or len(s) == 3):
                s = input()
            x, y = battle.decript(s)
            battle.hit(x, y)
        elif battle.turn == 2:
            print("Игрок 2:")
            m1, m2 = battle.map(2)
            print(*m1, sep='\n')
            print("Игрок 1:")
            print(*m2, sep='\n')
            print("Напишите координаты атаки:")
            s = input()
            while not(len(s) == 2 or len(s) == 3):
                s = input()
            x, y = battle.decript(s)
            battle.hit(x, y)
