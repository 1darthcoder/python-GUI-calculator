# python-GUI-calculator
A simple desktop calculator built with Python and Tkinter. It opens in its own window with a clickable keypad and a display screen, and supports basic arithmetic plus a few extra tools like percentage, sign change and square root.

   ![Calculator screenshot](calculator-screenshot.png)

**FEATURES**
addition,subtraction,multiplication and division
decimal number support (only one decimal point allowed per number)
AC (all clear) to reset calculator
+/- to change number between positive and negative
% convert number to percent (divides by 100)
√ to calculate square root of number
Whole-number answers shown cleanly
Fixed-size window automatically opens in centre of the screen
Colour coded buttons

**Requirements**
Python 3.x
Tkinter (included with the standard Python installation on Windows and macOS; on some Linux systems you may need to install it separately, e.g. sudo apt install python3-tk)

No extra packages need to be installed.
How to Run
Download or clone this repository:
bash
   git clone https://github.com/1darthcoder/<python-GUI-calculator>.git
Open a terminal in the project folder.
Run the program:
bash
   python "calculator V2.py"



**How It Works**
The keypad is a list. The button layout is stored as a list of rows, and nested loops build every button from it, so the layout can be changed without rewriting the interface code.
Event-driven design. Every button calls the same function, button_clicked(), and passes in its own value. That function decides what to do depending on whether the button is a number, an operator or a tool.
The calculator remembers the sum. Three variables hold the first number (A), the chosen operator (operator) and the second number (B). When = is pressed, the calculation is carried out and the memory is cleared.
Window centring. The program measures the window and the screen, then works out where to place the window so it opens in the middle.
Project Structure
.
├── calculator.py   # the full program
└── README.md
Known Limitations

**These are things I know about and plan to improve:**

Dividing by zero crashes the program instead of showing an error message
Taking the square root of a negative number crashes the program
Calculations can't be chained (for example 5 + 3 + 2 before pressing =)
Keyboard input isn't supported yet, so buttons must be clicked with the mouse

**Future Improvements**
Add try/except error handling so invalid input shows "Error" instead of crashing
Support chained calculations
Add keyboard support

**What I Learned**
Building this project taught me both the basics of Python, how to import libraries and how to make clickable buttons. It reminded me how to create global variables helped show me the structure when coding a program in python such as creating variables, defining classes and basic python logic. I learnt how to use the square root function from importing it when importing it from the math library. I learnt how to make a list and array. I also learnt if, else, else if loops. Additionally i learnt how to make a window pop up and how to play around with the sizes of a window and the math behind making a window pop up in the centre of a screen. I also learnt floats, None, int and strings. I also discovered the modulo and lambda operators.

**Python fundamentals**
Working with variables and data types (strings, floats, integers and None) and converting between them with float(), int() and str()
Using nested lists (2D lists) and indexing to store and look up the keypad layout
Controlling program flow with if / elif / else chains and for loops, including nested loops to generate all the buttons automatically
Using the in operator to check whether a value belongs to a list or string
Using the modulo operator (%) to check whether a number is whole

**Functions and scope**
Writing functions with parameters and return values, and keeping each function focused on one job (clear_all, remove_decimal, button_clicked)
Understanding global variables and the global keyword so functions can update the calculator's stored values
Using lambda functions with default arguments so each button remembers its own value

**GUI programming with Tkinter**

Creating windows, frames, labels and buttons
Arranging widgets with the grid() layout manager, including columnspan and sticky
Styling widgets with fonts and hex colour codes
Event-driven programming: the program waits for clicks and responds through callback functions, and mainloop() keeps it running
Calculating screen positions to centre the window

**MY Biggest takeaways**
Programs that look like they work can still hide a ton of bugs in them until each feature is tested properly
Small mistakes (a wrong symbol or a wrong indentation level) can break an entire feature
Writing clear comments makes it far easier to understand my own code when I return to it later
Author
<Miekie Harris> GitHub: [@1darthcoder](https://github.com/1darthcoder)
