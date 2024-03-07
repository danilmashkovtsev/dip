from fastapi import APIRouter

win = APIRouter()

@win.post("/energy/")
async def get_wins(proximal_left: int = 0, distal_left: int = 0, proximal_right: int = 0, distal_right: int = 0):
    # Проверка для левой стороны
    if proximal_left > 0 or distal_left == 0:
        left_winner = "Ян"
    else:
        left_winner = "Инь"

    # Проверка для правой стороны
    if proximal_right > 0 or distal_right == 0:
        right_winner = "Ян"
    else:
        right_winner = "Инь"

    # Проверка на равенство победителей слева и справа
    if left_winner == right_winner:
        return {"result": "Таблица заполнена верно"}
    else:
        return {"result": "Таблица заполнена неверно"}

@win.post("/P9/")
async def get_wins(left: int = 0, right :int = 0):
    # Проверка для левой стороны
    if right < left or right == 0:
        left_winner = "Ян"
    else:
        left_winner = "Инь"
    # Проверка для правой стороны
    if right > left or left == 0:
        right_winner = "Ян"
    else:
        right_winner = "Инь"

    # Проверка на равенство победителей слева и справа
    if left_winner == right_winner:
        return {"result": "Таблица заполнена верно"}
    else:
        return {"result": "Таблица заполнена неверно"}

@win.post("/E42/")
async def get_wins2(chi_cun_left: int = 0, e42_left: int = 0, chi_cun_right: int = 0, e42_right: int = 0):
    # Проверка для левой стороны
    if chi_cun_left == 1:
        left1_winner = "Чжун"
    else:
        left1_winner = "Вэй"

    if  e42_left == 1:
        left2_winner = "Чжун"
    else:
        left2_winner = "Вэй"

    # Проверка для правой стороны
    if chi_cun_right == 1:
        right1_winner = "Чжун"
    else:
        right1_winner = "Вэй"

    if e42_right == 1:
        right2_winner = "Чжун"
    else:
        right2_winner = "Вэй"

    # Проверка на равенство победителей слева и справа
    if left1_winner == right1_winner and left2_winner == right2_winner:
        return {"result": "Таблица заполнена верно"}
    else:
        return {"result": "Таблица заполнена неверно"}

