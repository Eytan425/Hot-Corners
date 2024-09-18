# globals.py
from tkinter import StringVar

# Initialize global variables
topRight = None
topLeft = None
bottomRight = None
bottomLeft = None

def initialize_globals(app):
    global topRight, topLeft, bottomRight, bottomLeft
    topRight = StringVar(app)
    topLeft = StringVar(app)
    bottomRight = StringVar(app)
    bottomLeft = StringVar(app)

    # Set default values
    topRight.set('Lock PC')
    topLeft.set('Minimize')
    bottomLeft.set('Open Browser')
    bottomRight.set('File Explorer')
