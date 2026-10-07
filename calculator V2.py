#==================
#What this program does:
#This is a mini calculator that opens its own mini window like the
#calculator app on the phone
#==================

#tkinter --> built in library in python to build windows buttons,
# and text labels
import tkinter 

#math also a built in python library used in square root funct
import math


#------------
#BUTTON LAYOUT
#This list is the map of the buttons on the calc keypad
#------------
button_values = [
    ["AC", "+/-", "%", "÷"], 
    ["7", "8", "9", "×"], 
    ["4", "5", "6", "-"],
    ["1", "2", "3", "+"],
    ["0", ".", "√", "="]
]

right_symbols = ["÷", "×", "-", "+", "="]
top_symbols = ["AC", "+/-", "%", "√"]

#counts num of rows and coloumns keypad has to build
#right amount of buttons without having us type out each one
row_count = len(button_values) #5
column_count = len(button_values[0]) #4


#Colours of the calc
colour_grey = "#5F6368"
colour_light_grey = "#80868B"
colour_black = "#3C4043"
colour_blue = "#4285F4"
colour_white = "#FFFFFF"

#window setup
window = tkinter.Tk() #creates main window
window.title("Calculator")
window.resizable(False, False) #stops user from making window bigger or smaller

frame = tkinter.Frame(window) 
#label is name of our calc display screen, starts by showing 0
#anchor e pushes text to right side of label
label = tkinter.Label(frame, text="0", font=("Arial", 30), background=colour_black,
                     foreground=colour_white, anchor="e")

#places screen in top row of frame and stretches across all 4 coloumns
label.grid(row=0, column=0, columnspan=column_count, sticky="we")

#BUTTONS
#instead of creating 20 indiv buttons, 2 loops go through keypad map 
#row by row and coloumn by coloumn and make button for each entry
for row in range(row_count):
    for column in range(column_count):
        value = button_values[row][column]
        button = tkinter.Button(frame, text=value, font=("Arial", 20),
                                width=column_count-1, height=1,
                                command=lambda value=value: button_clicked(value)) #command says what should happen when button clicked
        if value in top_symbols:
            button.config(foreground=colour_black, background=colour_light_grey)
        elif value in right_symbols:
            button.config(foreground=colour_white, background=colour_blue)
        else:
            button.config(foreground=colour_white, background=colour_grey)
        button.grid(row=row+1, column=column)

#makes frame (screen+buttons) actually show in window
frame.pack()


#calculator memory 
#these 3 variables act as notepad calc uses to remember what going on
#math functions A+B, A-B, A*B, A/B
A = "0" #1st num
operator = None #operation (+,-,etc)
B = None #2nd num

#Function to wipe calc memory clean so ready for new sum
def clear_all():
    global A, B, operator
    A = "0"
    operator = None
    B = None 

def remove_decimal(num):
    if num % 1 == 0:     #is there nothing after decimal?
        num = int(num)  #if so turn into whole num
    return str(num)     #hand answet back as text

#BRAIN of calc
# everytime button clicked function i stold which button it was and what to do 
def button_clicked(value):
    global right_symbols, top_symbols, label, A, B, operator

    #CASE 1 
    if value in right_symbols:
        if value == "=":
            if A is not None and operator is not None:
                B = label["text"]
                numA = float(A)
                numB = float(B)

            if operator == "+":
                label["text"] = remove_decimal(numA + numB)
            elif operator == "-":
                label["text"] = remove_decimal(numA - numB)
            elif operator == "×":
                label["text"] = remove_decimal(numA * numB)
            elif operator == "÷":
                label["text"] = remove_decimal(numA / numB)

            clear_all()
            
        elif value in "+-×÷":
            if operator is None:
                A = label["text"]       #save curr num as 1st 
                label["text"] = "0"     #reset screen so 2nd num can be typed
                B = "0"                 

            operator = value            #remem what sign chosen

    #CASE 2
    elif value in top_symbols:
        if value == "AC": # wipe memory put back to 0
            clear_all()
            label["text"] = "0"

        elif value == "+/-": # flip num from positive to negative
            result = float(label["text"]) * -1
            label["text"] = remove_decimal(result)

        elif value == "%":
            result = float(label["text"]) / 100
            label["text"] = remove_decimal(result)

        elif value == "√":
            result = math.sqrt(float(label["text"]))
            label["text"] = remove_decimal(result)

    #CASE 3
    else: #digits or decimal buttons
        if value == ".":
            if value not in label["text"]:
                label["text"] += value
        elif value in "0123456789":
            if label["text"] == "0": #if current label is 0 dont want to add num to zero but replace it 
                label["text"] = value
            else:
                label["text"] += value 

#Recentering the window
window.update() #updates the window proeprties with size dimension
window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

#Math to put calc in the middle of the screen
window_x = int((screen_width/2) - (window_width/2))     #distance from left edge
window_y = int((screen_height/2) - (window_height/2))   #distance from top edge

#formatting (w)x(h) + (x)+(y)
window.geometry(f"{window_width}x{window_height}+{window_x}+{window_y}")

window.mainloop()