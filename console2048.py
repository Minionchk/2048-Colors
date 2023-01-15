import random

# Шестнадцатеричное значение цвета
mp = [[0, 0, 0, 0], [0, 0, 0, 0],
      [0, 0, 0, 0], [0, 0, 0, 0]]
vis = [[0, 0, 0, 0], [0, 0, 0, 0],
       [0, 0, 0, 0], [0, 0, 0, 0]]
newmp = [[0, 0, 0, 0], [0, 0, 0, 0],
         [0, 0, 0, 0], [0, 0, 0, 0]]
vc = [[1, 1, 1, 1], [1, 1, 1, 1],
      [1, 1, 1, 1], [1, 1, 1, 1]]


def random_num():
    while True:
        x1 = random.randint(0, 3)
        y1 = random.randint(0, 3)
        if vis[x1][y1] == 0:
            mp[x1][y1] = random.choice([2, 4, 2, 2])
            vis[x1][y1] = 1
            return


def init():
    for i in range(4):
        for j in range(4):
            newmp[i][j] = 0
            vis[i][j] = 0


def init_mp():
    for i in range(4):
        for j in range(4):
            mp[i][j] = 0


def gameover():
    if vis == vc and panduan() is False:
        return True
    return False


def panduan():
    movex = [-1, 1, 0, 0]
    movey = [0, 0, -1, 1]
    for i in range(4):
        for j in range(4):
            for q in range(4):
                newx = int(i + movex[q])
                newy = int(j + movey[q])
                if (newx < 0 or newx > 3) or (newy < 0 or newy > 3):
                    continue
                else:
                    if mp[i][j] == mp[newx][newy]:
                        return True
    return False


# UP
def put_up():
    init()
    for i in range(4):
        q = 0
        for j in range(4):
            if mp[j][i] == 0:
                continue
            else:
                newmp[q][i] = mp[j][i]
                q += 1
    for i in range(4):
        for j in range(1, 4):
            if newmp[j][i] == 0:
                break
            else:
                if newmp[j][i] == newmp[j - 1][i]:
                    newmp[j - 1][i] = newmp[j][i] + newmp[j - 1][i]
                    newmp[j][i] = 0
    if newmp == mp:
        return
    init_mp()
    for i in range(4):
        q = 0
        for j in range(4):
            if newmp[j][i] == 0:
                continue
            else:
                mp[q][i] = newmp[j][i]
                vis[q][i] = 1
                q += 1
    random_num()
    gameover()
    return


def put_down():
    init()
    for i in range(4):
        q = 3
        j = 3
        while j >= 0:
            if mp[j][i] == 0:
                j -= 1
                continue
            else:
                newmp[q][i] = mp[j][i]
                q -= 1
                j -= 1
    for i in range(4):
        j = 2
        while j >= 0:
            if newmp[j][i] == 0:
                break
            else:
                if newmp[j][i] == newmp[j + 1][i]:
                    newmp[j + 1][i] = newmp[j][i] + newmp[j + 1][i]
                    newmp[j][i] = 0
            j -= 1
    if newmp == mp:
        return
    init_mp()
    for i in range(4):
        q = 3
        j = 3
        while j >= 0:
            if newmp[j][i] == 0:
                j -= 1
                continue
            else:
                mp[q][i] = newmp[j][i]
                vis[q][i] = 1
                q -= 1
            j -= 1
    random_num()
    gameover()
    return


def put_left():
    init()
    for i in range(4):
        q = 0
        for j in range(4):
            if mp[i][j] == 0:
                continue
            else:
                newmp[i][q] = mp[i][j]
                q += 1
    for i in range(4):
        for j in range(1, 4):
            if newmp[i][j] == 0:
                break
            else:
                if newmp[i][j] == newmp[i][j - 1]:
                    newmp[i][j - 1] = newmp[i][j] + newmp[i][j - 1]
                    newmp[i][j] = 0
    if newmp == mp:
        return
    init_mp()
    for i in range(4):
        q = 0
        for j in range(4):
            if newmp[i][j] == 0:
                continue
            else:
                mp[i][q] = newmp[i][j]
                vis[i][q] = 1
                q += 1
    random_num()
    gameover()
    return


def put_right():
    init()
    for i in range(4):
        q = 3
        j = 3
        while j >= 0:
            if mp[i][j] == 0:
                j -= 1
                continue
            else:
                newmp[i][q] = mp[i][j]
                q -= 1
                j -= 1
    for i in range(4):
        j = 2
        while j >= 0:
            if newmp[i][j] == 0:
                break
            else:
                if newmp[i][j] == newmp[i][j + 1]:
                    newmp[i][j + 1] = newmp[i][j] + newmp[i][j + 1]
                    newmp[i][j] = 0
            j -= 1
    if newmp == mp:
        return
    init_mp()
    for i in range(4):
        q = 3
        j = 3
        while j >= 0:
            if newmp[i][j] == 0:
                j -= 1
                continue
            else:
                mp[i][q] = newmp[i][j]
                vis[i][q] = 1
                q -= 1
            j -= 1
    random_num()
    gameover()
    return


random_num()
