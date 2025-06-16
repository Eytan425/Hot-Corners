# Hot Corners for Windows

This program allows you to assign custom actions to each corner of your screen. When you move your mouse to a specific corner, the program detects it and performs the action you selected (such as minimizing windows, locking the PC, opening a browser, etc.).

---

## 1. Prerequisites
- This program is designed for Windows.
- You need Python 3.8 or newer installed. Download from: https://www.python.org/downloads/

## 2. Install Required Python Modules
Open a terminal (Command Prompt or PowerShell) in this project directory and run:

```
pip install pyautogui pygetwindow psutil keyboard
```

Tkinter is also required. It comes pre-installed with Python on Windows. If you are on Linux and get errors about Tkinter, install it with:
- **Debian/Ubuntu:**
  ```
  sudo apt-get install python3-tk
  ```
- **Fedora:**
  ```
  sudo dnf install python3-tkinter
  ```

## 3. Running the Program
- To start the graphical interface, run:

```
python UI.py
```

- This will open the Hot Corners configuration window. Here you can assign actions to each screen corner using the provided buttons.
- Your choices are saved automatically.
- The background process that detects mouse position and triggers actions will start automatically when you launch the UI.

## 4. Actions Available
- Minimize (Show Desktop)
- Lock PC
- Open Browser
- File Explorer
- Shut Down
- Close Windows
- Sleep
- Task Manager

## 5. Resetting to Defaults
- Use the "Reset" button in the UI to restore default actions for all corners.
- You can also press Ctrl+R in the UI window to reset.

## 6. Exiting the Program
- Use the "Close" button in the UI to exit the program.

## 7. Troubleshooting
- If you get errors about missing modules, make sure you have installed all required packages with `pip install ...` as above.
- Some actions (like Lock PC, Shut Down, etc.) may require administrator privileges.
- This program is not designed for Linux or MacOS.

---

Enjoy using Hot Corners for Windows!
