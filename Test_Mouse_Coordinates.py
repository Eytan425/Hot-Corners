import pyautogui as pyautogui

screen_width, screen_height = pyautogui.size()
print(screen_height, screen_width)
#height 1080
#width = 1920
def MouseCoordinates():
    while True:
        x, y = pyautogui.position()
        print(x,y)

MouseCoordinates()