import pyautogui as py
import time
default = [0, 0]
window = py.size()
print(window)


def moveto(x, y):
    #print("Current: ", py.position())
    #print("move to: ", x, y)
    if py.onScreen(x, y):
        py.moveTo(x, y)
    # print("position: ", x, y)
    # print("screen: ",py.onScreen(x+py.position().x, y+py.position().y))
    # if py.position().x == 0 and py.position().y == 0:
    #     py.FAILSAFE = False
    #     x, y = 1, 1
    #     py.moveTo(x, y)
    #     py.FAILSAFE = True
    # elif py.onScreen(x+py.position().x, y+py.position().y):
    #     print(x+py.position().x, y+py.position().y)
    #     py.moveRel(x, y)



    # global default
    # x -= default[0]
    # y -= default[1]
    # default[0] += x
    # default[1] += y
    # print("cur position: ",py.position())
    # print("default: ", default)
    # if -1 < (default[0] + py.position().x) <= window[0] and -1 < (default[1] + py.position().y) <= window[1]:
    #     py.moveRel(default[0], default[1])
    # else:
    #     x = (default[0] + py.position().x)-window[0]
    #     y = (default[1] + py.position().y)-window[1]
    #     print(default[0]+x, default[1]+y)
    #     py.moveRel(default[0]+x, default[1]+y)

# print(type(py.position()))
#
# time.sleep(2)
# py.moveTo(100, 0)
# time.sleep(2)
# moveto(-100, 0)
# time.sleep(2)
#
# moveto(500, 600)
# time.sleep(2)
# moveto(300, 200)
# time.sleep(2)
# moveto(1000, 1000)
# time.sleep(2)
# moveto(1437, 2)
