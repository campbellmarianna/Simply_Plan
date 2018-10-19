from tkinter import *

window = Tk()

window.title("Welcome to LikeGeeks app")

# set window size - sets window width to 350 pixels and the height to 200 pixels
window.geometry('350x200')

"""
Common Steps
    1. Create widget
    2. Position widget in grid
    3. Add attributes (font, forground color, background color)
"""
# create a label
lbl = Label(window, text="Hello", font=("Arial Bold", 50))

# Using the grid function set the labels position on the form
lbl.grid(column=0, row=0)

# create a textbox using Tkinter Entry class
txt = Entry(window, width=10, state="disabled")

# Using the grid function set the textboxs position on the form
txt.grid(column=1, row=0)

# execute a function when the button is clicked
def clicked():
    # get entry text using get function
    res = "Welcome to " + txt.get()
    # if you clikc the buttin and there is a text on the entry widget, it will
    # show "Welcome to" concatenated with the entered text.
    lbl.configure(text=res)
    txt.focus()

#create a button
    # change the foreground of any widget using fg property
    # change the background of any widget using bg property
btn = Button(window, text="Click Me", command = clicked)

# Using the grid function set the buttons position on the form
btn.grid(column=2, row=0)


window.mainloop()
