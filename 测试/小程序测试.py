import pyautogui
import time


def daka():
    pyautogui.click(688, 266, clicks=1, interval=1, button='left')
    pyautogui.click(754, 414, clicks=1, interval=1, button='left')
    pyautogui.click(676, 181, clicks=1, interval=1, button='left')
    pyautogui.click(681, 275, clicks=1, interval=1, button='left')
    pyautogui.click(676, 468, clicks=1, interval=1, button='left')
    pyautogui.click(676, 663, clicks=1, interval=1, button='left')
    pyautogui.click(676, 694, clicks=1, interval=1, button='left')
    # 返回
    pyautogui.click(501, 22, clicks=1, interval=1, button='left')


def jiankang():
    # 健康值排名
    pyautogui.click(584, 387, clicks=1, interval=1, button='left')


def geren():
    # 个人健康值排名
    pyautogui.click(680, 315, clicks=1, interval=1, button='left')


def saiqu():
    # 赛区
    pyautogui.click(680, 406, clicks=1, interval=1, button='left')


def shequ():
    # 社区
    pyautogui.click(680, 507, clicks=1, interval=1, button='left')


def diqu():
    # 地区
    pyautogui.click(680, 605, clicks=1, interval=1, button='left')


def paiming():
    # 实时排名
    pyautogui.click(555, 78, clicks=1, interval=1, button='left')
    #
    pyautogui.click(526, 130, clicks=1, interval=1, button='left')
    pyautogui.click(606, 130, clicks=1, interval=1, button='left')
    pyautogui.click(683, 130, clicks=1, interval=1, button='left')
    pyautogui.click(759, 130, clicks=1, interval=1, button='left')
    pyautogui.click(836, 130, clicks=1, interval=1, button='left')
    # 本周排名
    pyautogui.click(682, 78, clicks=1, interval=1, button='left')
    #
    pyautogui.click(526, 130, clicks=1, interval=1, button='left')
    pyautogui.click(606, 130, clicks=1, interval=1, button='left')
    pyautogui.click(683, 130, clicks=1, interval=1, button='left')
    pyautogui.click(759, 130, clicks=1, interval=1, button='left')
    pyautogui.click(836, 130, clicks=1, interval=1, button='left')
    # 本周排名
    pyautogui.click(810, 78, clicks=1, interval=1, button='left')
    #
    pyautogui.click(526, 130, clicks=1, interval=1, button='left')
    pyautogui.click(606, 130, clicks=1, interval=1, button='left')
    pyautogui.click(683, 130, clicks=1, interval=1, button='left')
    pyautogui.click(759, 130, clicks=1, interval=1, button='left')
    pyautogui.click(836, 130, clicks=1, interval=1, button='left')
    pyautogui.click(685, 437, clicks=1, interval=1, button='left')
    # 返回
    pyautogui.click(501, 22, clicks=1, interval=1, button='left')


if __name__ == "__main__":
    start = time.perf_counter()
    daka()
    # jiankang()
    # geren()
    # paiming()
    # saiqu()
    # paiming()
    # shequ()
    # paiming()
    # diqu()
    # paiming()
    end = time.perf_counter()
    print('运行', (end - start))
