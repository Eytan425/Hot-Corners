from packages import *


# Get the screen dimensions
screen_width, screen_height = pyautogui.size()

def close_all_windows():
    os.system('taskkill /F /FI "IMAGENAME ne explorer.exe" /FI "WINDOWTITLE ne eq"')





def cornerActions(action):
    if action == 'Minimize':
        print("Showing Desktop")
        os.system('powershell -command "(new-object -ComObject shell.application).minimizeall()"')
    elif action == 'Lock PC':
        print("Locking your PC")
        os.system("rundll32.exe user32.dll,LockWorkStation")
    elif action == 'Open Browser':
        print("Opening Default Web Browser")
        webbrowser.open("https://google.com")
    elif action == 'File Explorer':
        print("Opening File Explorer")
        os.system('explorer')
    elif action == 'Shut Down':
        COMMAND = "Stop-Computer -Force"
        subprocess.run(['powershell', '-command', COMMAND], shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)    
    elif action == 'Close Windows':
        print("Closing all windows")
    elif action == 'Sleep':
        os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")
        close_all_windows()    
def top_left_corner():
    action = globals.topLeft.get()
    cornerActions(action)  


def top_right_corner():
    action = globals.topRight.get()
    cornerActions(action) 

def bottom_left_corner():
    action = globals.bottomLeft.get()
    cornerActions(action) 

def bottom_right_corner():
    action = globals.bottomRight.get()
    cornerActions(action) 

def Hot_Corners():
    while True:
        x, y = pyautogui.position()
        if x == 0 and y == 0:
            top_left_corner()
        elif x == screen_width - 1 and y == 0:
            top_right_corner()
        elif x == 0 and y == screen_height - 1:
            bottom_left_corner()
        elif x == screen_width - 1 and y == screen_height - 1:
            bottom_right_corner()

        time.sleep(0.5)

if __name__ == '__main__':
    print("Hot Corners started....")
    Hot_Corners()
