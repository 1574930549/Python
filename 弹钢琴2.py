import pyautogui
import time

# 8
# 24
#  ... ..   .       .   .. ...
# C 45 172 302 433 564 694 820
# D 64 191 322 454 582 711 840
# E 81 209 341 470 599 727 859
# F 98 229 359 488 617 747 876
# G 118 246 376 505 637 768 896
# A 135 266 395 525 653 787 913
# B 155 285 415 544 674 804 931
# 950
# pyautogui.click(, 520, clicks=1, interval=0.5, button='left')
def a():
    # 1.3.6.7.
    # 1..3.6.1..
    # 2..3.1..3.
    # 7.3.6.3.
    # 7.3.5.6.
    # 7.3.5.7.
    # 1..3.7.3.
    # 6.3.3..3.
    pyautogui.click(525, 520, clicks=1, interval=0.1, button='left')
if __name__=="__main__":
    start = time.perf_counter()
    a()
    end = time.perf_counter()
    print('运行' , (end - start))


