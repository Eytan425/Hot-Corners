from packages import *

app = Tk()
app.title("Hot-Corners For Windows")
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

# Placement
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

# Create a new window for selecting options
def open_options_window(corner_variable, button):
    options_window = Toplevel(app)
    options_window.title("Select Action")
    options_window.geometry("400x300")

    options = ['None', 'Lock PC', 'Minimize', 'Open Browser', 'File Explorer', 'Shut Down', 'Close Windows', 'Sleep', 'Task Manager']

    def select_option(choice):
        corner_variable.set(choice)
        button.config(text=choice)
        options_window.destroy()

    for option in options:
        button_option = Button(options_window, text=option, command=lambda opt=option: select_option(opt))
        button_option.pack(fill=BOTH, expand=True)

# Function to update the button text and save to JSON
def Choices():
    global topRightChoice, topLeftChoice, bottomRightChoice, bottomLeftChoice
    
    # Fetch the values of the options
    topRightChoice = globals.topRight.get()
    topLeftChoice = globals.topLeft.get()
    bottomRightChoice = globals.bottomRight.get()
    bottomLeftChoice = globals.bottomLeft.get()

    # Update the text on the buttons
    top_left_button.config(text=topLeftChoice)
    top_right_button.config(text=topRightChoice)
    bottom_left_button.config(text=bottomLeftChoice)
    bottom_right_button.config(text=bottomRightChoice)

    # Save to JSON
    choices = {
        "Top-Left": topLeftChoice,
        "Top-Right": topRightChoice,
        "Bottom-Left": bottomLeftChoice,
        "Bottom-Right": bottomRightChoice
    }
    with open("hot_corners_choices.json", "w") as file:
        json.dump(choices, file)

# Function to load choices from JSON
def load_choices():
    try:
        with open("hot_corners_choices.json", "r") as file:
            choices = json.load(file)
            globals.topLeft.set(choices.get("Top-Left", 'None'))
            globals.topRight.set(choices.get("Top-Right", 'None'))
            globals.bottomLeft.set(choices.get("Bottom-Left", 'None'))
            globals.bottomRight.set(choices.get("Bottom-Right", 'None'))

            # Update buttons with loaded choices
            top_left_button.config(text=globals.topLeft.get())
            top_right_button.config(text=globals.topRight.get())
            bottom_left_button.config(text=globals.bottomLeft.get())
            bottom_right_button.config(text=globals.bottomRight.get())
    except FileNotFoundError:
        pass

# Function to reset the corners and update the buttons
def Reset():
    # Reset the values to default
    globals.topRight.set('Lock PC')
    globals.topLeft.set('Minimize')
    globals.bottomLeft.set('Open Browser')
    globals.bottomRight.set('File Explorer')

    # Call Choices to update button text and save to JSON
    Choices()

# Confirm reset
def confirm_reset():
    result = tkinter.messagebox.askyesno("Reset Confirmation", "Are you sure you want to reset the hot corner settings?")
    if result:
        Reset()

# Close app
def Close():
    app.destroy()
    print("Closing the app....")

button_frame = Frame(app, background="#141414")
button_frame.pack(side=BOTTOM, pady=20)

# Creating Buttons for Close and Reset
closeButton = Button(button_frame, text='Close', command=Close, justify='center', anchor='center')
resetButton = Button(button_frame, text="Reset", command=confirm_reset, justify='center', anchor='center')

# Placing Buttons
closeButton.pack(side=LEFT, padx=4, pady=20)
resetButton.pack(side=LEFT, padx=5, pady=20)

# Defining the labels and buttons for the corners
top_left_button = Button(frame, text=globals.topLeft.get(), command=lambda: open_options_window(globals.topLeft, top_left_button), font=("Arial", menu_font_size), width=menu_width)
top_right_button = Button(frame, text=globals.topRight.get(), command=lambda: open_options_window(globals.topRight, top_right_button), font=("Arial", menu_font_size), width=menu_width)
bottom_left_button = Button(frame, text=globals.bottomLeft.get(), command=lambda: open_options_window(globals.bottomLeft, bottom_left_button), font=("Arial", menu_font_size), width=menu_width)
bottom_right_button = Button(frame, text=globals.bottomRight.get(), command=lambda: open_options_window(globals.bottomRight, bottom_right_button), font=("Arial", menu_font_size), width=menu_width)

# Labels for each corner
Label(frame, text="Top-Left:", bg="#141414", fg="white", font=("Arial", label_font_size), width=label_width).grid(row=1, column=1, padx=(padding + label_padding_x, padding), pady=padding, sticky="w")
Label(frame, text="Top-Right:", bg="#141414", fg="white", font=("Arial", label_font_size), width=label_width).grid(row=1, column=3, padx=(padding + label_padding_x, padding), pady=padding, sticky="w")
Label(frame, text="Bottom-Left:", bg="#141414", fg="white", font=("Arial", label_font_size), width=label_width).grid(row=2, column=1, padx=(padding + label_padding_x, padding), pady=padding, sticky="w")
Label(frame, text="Bottom-Right:", bg="#141414", fg="white", font=("Arial", label_font_size), width=label_width).grid(row=2, column=3, padx=(padding + label_padding_x, padding), pady=padding, sticky="w")

# Buttons placement
top_left_button.grid(row=1, column=2, padx=padding, pady=padding, sticky="ew")
top_right_button.grid(row=1, column=4, padx=padding, pady=padding, sticky="ew")
bottom_left_button.grid(row=2, column=2, padx=padding, pady=padding, sticky="ew")
bottom_right_button.grid(row=2, column=4, padx=padding, pady=padding, sticky="ew")

# Configuring grid weights for square layout
for i in range(3):
    frame.grid_rowconfigure(i, weight=1)
    frame.grid_columnconfigure(i, weight=1)

# Tracing what each corner does
globals.topRight.trace('w', lambda *args: Choices())
globals.topLeft.trace('w', lambda *args: Choices())
globals.bottomRight.trace('w', lambda *args: Choices())
globals.bottomLeft.trace('w', lambda *args: Choices())

# Load from the JSON file the corners
load_choices()

# Starts the background functionality of hot corners
def start_hot_corners():
    import Hot_Corners
    Hot_Corners.Hot_Corners()

threading.Thread(target=start_hot_corners, daemon=True).start()

app.mainloop()
