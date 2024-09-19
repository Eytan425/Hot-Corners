from packages import *


app = Tk()
app.title("Hot-Corners For Windows")
# app.geometry("800x600")
app.minsize(1200, 400)
app.configure(bg="#141414")
title_font = tkFont.Font(family="Helvetica", size=24, weight="bold")

def on_ctrl_r(event):
    confirm_reset()

# Bind Ctrl+R to the confirm_reset function
app.bind('<Control-r>', on_ctrl_r)

def download_instructions():
    source = "instructions.txt"
    downloads_folder = os.path.join(os.path.expanduser("~"), "Downloads")
    destination = os.path.join(downloads_folder, "instructions.txt")
    shutil.copy(source, destination)
    print(f"Instructions downloaded to {destination}")
    tkinter.messagebox.showinfo("Instructions download", f"Instructions downloaded to {destination}")
downloadButton = Button(app, text="Click here for instructions", command=download_instructions, bg="#141414", fg="white")


# Create the title label
title = Label(app, text='Hot Corners!', font=title_font, bg="#141414", fg="white")
title.pack(ipadx=10, ipady=10)
downloadButton.pack(ipadx=10, ipady=10)


globals.initialize_globals(app)

#Placement
windowWidth = 800
windowHeight = 600
positionRight = int(app.winfo_screenwidth() / 2 - windowWidth / 2)
positionDown = int(app.winfo_screenheight() / 2 - windowHeight / 2)
app.geometry(f"{windowWidth}x{windowHeight}+{positionRight}+{positionDown}")

label_font_size = 14
menu_font_size = 12
padding = 20
label_width = 20
menu_width = 25
label_padding_x = 10

frame = Frame(app, bg="#141414")
frame.pack(expand=True, fill=BOTH, padx=padding, pady=padding)


# Define the labels and option menus
labels = [
    Label(frame, text="Top-Left:", bg="#141414", fg="white", font=("Arial", label_font_size), width=label_width),
    Label(frame, text="Top-Right:", bg="#141414", fg="white", font=("Arial", label_font_size), width=label_width),
    Label(frame, text="Bottom-Left:", bg="#141414", fg="white", font=("Arial", label_font_size), width=label_width),
    Label(frame, text="Bottom-Right:", bg="#141414", fg="white", font=("Arial", label_font_size), width=label_width)
]

option_menus = [
    OptionMenu(frame, globals.topLeft, 'None', 'Lock PC', 'Minimize', 'Open Browser', 'File Explorer', 'Shut Down', 'Close Windows','Sleep', 'Task Manager'),
    OptionMenu(frame, globals.topRight, 'None', 'Lock PC', 'Minimize', 'Open Browser', 'File Explorer', 'Shut Down', 'Close Windows', 'Sleep', 'Task Manager'),
    OptionMenu(frame, globals.bottomLeft, 'None', 'Lock PC', 'Minimize', 'Open Browser', 'File Explorer', 'Shut Down', 'Close Windows', 'Sleep', 'Task Manager'),
    OptionMenu(frame, globals.bottomRight, 'None', 'Lock PC', 'Minimize', 'Open Browser', 'File Explorer', 'Shut Down', 'Close Windows', 'Sleep', 'Task Manager')
]

# Configure the option menus
for menu in option_menus:
    menu.config(font=("Arial", menu_font_size))
    menu.config(width=menu_width)

# Move the top labels and menus down by adjusting row indices
for i, label in enumerate(labels):
    row, col = divmod(i, 2)
    label.grid(row=row * 2 + 1, column=col * 2 + 1, padx=(padding + label_padding_x, padding), pady=padding, sticky="w")

for i, menu in enumerate(option_menus):
    row, col = divmod(i, 2)
    menu.grid(row=row * 2 + 1, column=col * 2 + 2, padx=padding, pady=padding, sticky="ew")

# Adjust the row and column configurations
for i in range(6):  # Increased range to account for the extra rows
    frame.grid_rowconfigure(i, weight=1)
for i in range(4):
    frame.grid_columnconfigure(i * 2 + 1, weight=1)
    frame.grid_columnconfigure(i * 2 + 2, weight=1)

# You can also configure the first row to give more space for the title
frame.grid_rowconfigure(0, minsize=60)

def Choices(*args):
    global topRightChoice, topLeftChoice, bottomRightChoice, bottomLeftChoice
    topRightChoice = str(globals.topRight.get())
    topLeftChoice = str(globals.topLeft.get())
    bottomRightChoice = str(globals.bottomRight.get())
    bottomLeftChoice = str(globals.bottomLeft.get())
    
    choices = {
        "Top-Left": topLeftChoice,
        "Top-Right": topRightChoice,
        "Bottom-Left": bottomLeftChoice,
        "Bottom-Right": bottomRightChoice
    }
    with open("hot_corners_choices.json", "w") as file:
        json.dump(choices, file)

def load_choices():
    try:
        with open("hot_corners_choices.json", "r") as file:
            choices = json.load(file)
            globals.topLeft.set(choices.get("Top-Left", 'None'))
            globals.topRight.set(choices.get("Top-Right", 'None'))
            globals.bottomLeft.set(choices.get("Bottom-Left", 'None'))
            globals.bottomRight.set(choices.get("Bottom-Right", 'None'))
    except FileNotFoundError:
        pass
def Reset():
    globals.topRight.set('Lock PC')
    globals.topLeft.set('Minimize')
    globals.bottomLeft.set('Open Browser')
    globals.bottomRight.set('File Explorer')

def confirm_reset():
    result = tkinter.messagebox.askyesno("Reset Confirmation", "Are you sure you want to reset the hot corner settings?")
    if result:
        Reset()
       

def Close():
    app.destroy()
    print("Closing the app....")
    

button_frame = Frame(app, background="#141414")
button_frame.pack(side=BOTTOM, pady=20)

#Creating Buttons
closeButton = Button(button_frame, text='Close', command=Close, justify='center', anchor='center')    

resetButton = Button(button_frame, text="Reset", command=confirm_reset,justify='center', anchor='center')

#Placing Buttons
closeButton.pack(side=LEFT, padx = 4,pady=20)
resetButton.pack(side=LEFT, padx = 5, pady=20)



#Tracing what each corner does
globals.topRight.trace('w', Choices)
globals.topLeft.trace('w', Choices)
globals.bottomRight.trace('w', Choices)
globals.bottomLeft.trace('w', Choices)

#Loads from the json file the corners
load_choices()

#Starts the brains of the app
def start_hot_corners():
    import Hot_Corners
    Hot_Corners.Hot_Corners()

threading.Thread(target=start_hot_corners, daemon=True).start()

app.mainloop()