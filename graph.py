
from tkinter import *
import tkinter.font as font
import turtle

from tkinter import ttk

from multiplication import multimatrix
from addition import addmatrix
from Rotation import rotatematrix

from drawing_history import patterns, save_pattern
from pattern_selection import enable_pattern_selection


# --------------------------------------------------
# MAIN WINDOW
# --------------------------------------------------

root = Tk()

root.title("Animation Window")
root.minsize(1000, 700)
root.state("zoomed")  # Open the application in maximized mode.


# --------------------------------------------------
# FONTS
# --------------------------------------------------

# Creating fonts separately so we can reuse them in widgets.

title_font = font.Font(
    family="Helvetica",
    size=22,
    weight="bold"
)

heading_font = font.Font(
    family="Helvetica",
    size=13,
    weight="bold"
)

button_font = font.Font(
    family="Helvetica",
    size=11,
    weight="bold"
)


# --------------------------------------------------
# MAIN SCROLLABLE CANVAS
# --------------------------------------------------

# Main Canvas:
# It will contain the complete application interface.

main_canvas = Canvas(
    root,
    highlightthickness=0
)


# Main vertical scrollbar:
# It controls the vertical movement of the main Canvas.

main_scrollbar = ttk.Scrollbar(
    root,
    orient="vertical",
    command=main_canvas.yview
)


# Frame that will contain all application widgets.

main_frame = Frame(main_canvas)


# Put the main Frame inside the Canvas.
# create_window() embeds a widget inside a Canvas.

main_window = main_canvas.create_window(
    (0, 0),
    window=main_frame,
    anchor="nw"
)


# Update the scrolling region whenever the Frame size changes.
# Configure event occurs when the widget's size or configuration changes.

def update_scroll_region(event):

    main_canvas.configure(
        scrollregion=main_canvas.bbox("all")
    )


main_frame.bind(
    "<Configure>",
    update_scroll_region
)


# Make the main Frame width equal to the Canvas width.
# This helps prevent unnecessary horizontal scrolling.

def update_main_width(event):

    main_canvas.itemconfig(
        main_window,
        width=event.width
    )


main_canvas.bind(
    "<Configure>",
    update_main_width
)


# Connect the Canvas and scrollbar.
# yscrollcommand updates the scrollbar position.

main_canvas.configure(
    yscrollcommand=main_scrollbar.set
)


# Place the main Canvas and scrollbar inside the root window.

main_canvas.pack(
    side="left",
    fill="both",
    expand=True
)

main_scrollbar.pack(
    side="right",
    fill="y"
)


# --------------------------------------------------
# MOUSE WHEEL SCROLLING
# --------------------------------------------------

# This function is called when the mouse wheel is used.

def scroll_main_window(event):

    main_canvas.yview_scroll(

        int(-1 * (event.delta / 120)),

        "units"

    )

    # event.delta indicates the direction of scrolling.
    # Positive delta means scrolling upward.
    # Negative delta means scrolling downward.
    #
    # -1 reverses the direction because Canvas scrolling
    # uses positive and negative movement differently.


# Bind the mouse wheel event to the main Canvas.

main_canvas.bind_all(
    "<MouseWheel>",
    scroll_main_window
)


# --------------------------------------------------
# MAIN TITLE
# --------------------------------------------------

title_label = Label(
    main_frame,
    text="GRAPH MAKER",
    font=title_font,
    fg="darkblue",
    pady=12
)

# columnspan=2 means this widget occupies two columns.

title_label.grid(
    row=0,
    column=0,
    columnspan=2,
    sticky="ew"
)


# --------------------------------------------------
# LEFT PANEL - TRANSFORMATION CONTROLS
# --------------------------------------------------

# LabelFrame groups related widgets together
# and displays a heading around them.

left_panel = LabelFrame(
    main_frame,
    text="2D Transformation Controls",
    font=heading_font,
    padx=12,
    pady=12
)


# Left panel occupies column 0.
# sticky="nw" aligns it towards the top-left.

left_panel.grid(
    row=1,
    column=0,
    sticky="nw",
    padx=10,
    pady=10
)


# --------------------------------------------------
# MATRIX INPUT
# --------------------------------------------------

L1 = Label(
    left_panel,
    text="Matrix",
    font=heading_font
)

L1.grid(
    row=0,
    column=0,
    sticky="w",
    pady=(5, 3)
)


# Text widget for entering the original matrix.

T1 = Text(
    left_panel,
    bd=2,
    height=8,
    width=28,
    font=("Consolas", 11)
)

T1.grid(
    row=1,
    column=0,
    sticky="ew",
    pady=5
)


# --------------------------------------------------
# TRANSFORMATION MATRIX
# --------------------------------------------------

L2 = Label(
    left_panel,
    text="Transformation Matrix",
    font=heading_font
)

L2.grid(
    row=2,
    column=0,
    sticky="w",
    pady=(12, 3)
)


# Text widget for entering the transformation matrix.

T2 = Text(
    left_panel,
    bd=2,
    height=8,
    width=28,
    font=("Consolas", 11)
)

T2.grid(
    row=3,
    column=0,
    sticky="ew",
    pady=5
)


# --------------------------------------------------
# ROTATION DEGREE SELECTION
# --------------------------------------------------

L3 = Label(
    left_panel,
    text="Select Rotation Degree",
    font=heading_font,
    fg="purple"
)

L3.grid(
    row=4,
    column=0,
    sticky="w",
    pady=(12, 5)
)


# Listbox allows the user to select one rotation degree.

ListBox1 = Listbox(
    left_panel,
    selectmode="single",
    height=5,
    width=25,
    font=("Arial", 11)
)


# Insert rotation options into the Listbox.

ListBox1.insert(1, "30 degree")
ListBox1.insert(2, "45 degree")
ListBox1.insert(3, "60 degree")
ListBox1.insert(4, "90 degree")
ListBox1.insert(5, "180 degree")
ListBox1.insert(6, "270 degree")


ListBox1.grid(
    row=5,
    column=0,
    sticky="ew",
    pady=5
)


# --------------------------------------------------
# OPERATION BUTTONS
# --------------------------------------------------

# Separate Frame to group all transformation buttons.

button_frame = Frame(left_panel)

button_frame.grid(
    row=6,
    column=0,
    sticky="ew",
    pady=15
)


# Scale button:
# Calls multimatrix() from multiplication.py.
#
# T1              = Original matrix
# T2              = Transformation matrix
# ab              = Turtle object
# refresh_history = Function to update the history table

B1 = Button(
    button_frame,
    text="Scale",
    font=button_font,
    width=12,
    bd=3,
    command=lambda: multimatrix(
        T1,
        T2,
        ab,
        refresh_history
    )
)

B1.grid(
    row=0,
    column=0,
    padx=4,
    pady=4
)


# Translate button:
# Calls addmatrix() from addition.py.

B2 = Button(
    button_frame,
    text="Translate",
    font=button_font,
    width=12,
    bd=3,
    command=lambda: addmatrix(
        T1,
        T2,
        ab,
        refresh_history
    )
)

B2.grid(
    row=0,
    column=1,
    padx=4,
    pady=4
)


# Rotate button:
# Calls rotatematrix() from Rotation.py.
# ListBox1 provides the selected rotation degree.

B3 = Button(
    button_frame,
    text="Rotate",
    font=button_font,
    width=12,
    bd=3,
    command=lambda: rotatematrix(
        T1,
        ListBox1,
        ab,
        refresh_history
    )
)

B3.grid(
    row=1,
    column=0,
    columnspan=2,
    padx=4,
    pady=5
)


# --------------------------------------------------
# RIGHT PANEL
# --------------------------------------------------

# This Frame contains two main sections:
# 1. Turtle drawing area.
# 2. Pattern history table.

right_panel = Frame(main_frame)

right_panel.grid(
    row=1,
    column=1,
    sticky="nsew",
    padx=10,
    pady=10
)


# --------------------------------------------------
# GRAPH / TURTLE DRAWING AREA
# --------------------------------------------------

graph_frame = LabelFrame(
    right_panel,
    text="Graph / Drawing Area",
    font=heading_font,
    padx=5,
    pady=5
)


# fill="both" allows the graph area to expand horizontally
# and vertically.
#
# expand=True allows it to receive additional available space.

graph_frame.pack(
    fill="both",
    expand=True,
    pady=(0, 10)
)


# Canvas where Turtle will draw.
# RawTurtle will use this Canvas instead of opening
# a separate Turtle window.

draw_canvas = Canvas(
    graph_frame,
    width=700,
    height=500,
    bg="white",
    highlightthickness=1,
    highlightbackground="gray"
)


draw_canvas.pack(
    fill="both",
    expand=True
)


# Create Turtle inside the Tkinter Canvas.

ab = turtle.RawTurtle(draw_canvas)

ab.speed(2)


# getScreen() returns the Turtle Screen object.
# We need this object to register mouse-click events.

screen = ab.getscreen()


# --------------------------------------------------
# PATTERN SELECTION
# --------------------------------------------------

# This function enables the user to click on a drawn pattern.
# It checks the clicked coordinates against saved patterns.
# If a pattern is selected, its matrix is displayed in T1.

enable_pattern_selection(
    screen,
    patterns,
    T1
)


# --------------------------------------------------
# PATTERN HISTORY TABLE
# --------------------------------------------------

# LabelFrame groups the history table and its scrollbar.

history_frame = LabelFrame(
    right_panel,
    text="Pattern History",
    font=heading_font,
    padx=5,
    pady=5
)


# History table is placed below the graph.
# fill="x" allows it to occupy the available horizontal space.

history_frame.pack(
    fill="x",
    expand=False
)


# Columns that will be displayed in the Treeview.

columns = (
    "Serial No.",
    "Operation",
    "Matrix"
)


# Create Treeview to display drawing history.

history_table = ttk.Treeview(
    history_frame,
    columns=columns,
    show="headings",
    height=8
)


# --------------------------------------------------
# HISTORY TABLE HEADINGS
# --------------------------------------------------

history_table.heading(
    "Serial No.",
    text="Serial No."
)

history_table.heading(
    "Operation",
    text="Operation"
)

history_table.heading(
    "Matrix",
    text="Matrix"
)


# --------------------------------------------------
# HISTORY TABLE COLUMNS
# --------------------------------------------------

# Configure the width and alignment of each column.

history_table.column(
    "Serial No.",
    width=80,
    minwidth=70,
    anchor="center",
    stretch=False
)

history_table.column(
    "Operation",
    width=120,
    minwidth=100,
    anchor="center",
    stretch=False
)

history_table.column(
    "Matrix",
    width=400,
    minwidth=150,
    anchor="w",
    stretch=True
)


# --------------------------------------------------
# HISTORY TABLE SCROLLBAR
# --------------------------------------------------

# Vertical scrollbar for the history table.

history_scrollbar = ttk.Scrollbar(
    history_frame,
    orient="vertical",
    command=history_table.yview
)


# Connect Treeview and scrollbar.

history_table.configure(
    yscrollcommand=history_scrollbar.set
)


# Place the table and scrollbar side by side.

history_table.grid(
    row=0,
    column=0,
    sticky="nsew"
)

history_scrollbar.grid(
    row=0,
    column=1,
    sticky="ns"
)


# Allow the history table to expand inside its Frame.

history_frame.grid_rowconfigure(
    0,
    weight=1
)

history_frame.grid_columnconfigure(
    0,
    weight=1
)


# --------------------------------------------------
# REFRESH HISTORY FUNCTION
# --------------------------------------------------

# This function performs two tasks:
#
# 1. Removes all existing rows from the Treeview.
#    We remove them because we need to display the latest history.
#
# 2. Adds all patterns from the patterns list.
#    Each pattern contains its ID, operation and matrix.


def refresh_history():

    # Remove existing rows from the history table.

    for item in history_table.get_children():

        history_table.delete(item)


    # Insert all saved patterns into the history table.

    for pattern in patterns:

        matrix_text = str(pattern["matrix"])

        history_table.insert(
            "",
            "end",

            # Use pattern ID as the unique Treeview item ID.
            iid=str(pattern["id"]),

            values=(

                pattern["id"],

                pattern["operation"],

                matrix_text

            )
        )


# Display previously saved patterns when application starts.

refresh_history()


# --------------------------------------------------
# GRID CONFIGURATION
# --------------------------------------------------

# Left column:
# weight=0 means it does not receive additional horizontal space.
# It occupies the space required by its widgets.

main_frame.grid_columnconfigure(
    0,
    weight=0
)


# Right column:
# weight=1 means it receives the remaining horizontal space.
# This gives more room to the graph and history table.

main_frame.grid_columnconfigure(
    1,
    weight=1
)


# Allow the main content row to expand vertically.

main_frame.grid_rowconfigure(
    1,
    weight=1
)


# --------------------------------------------------
# START APPLICATION
# --------------------------------------------------

root.mainloop()
