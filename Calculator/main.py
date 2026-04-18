import tkinter as tk

# Initialize the main window
root = tk.Tk()
root.title("Simple Calculator")
root.geometry("300x400")
root.resizable(0, 0) # Prevent resizing the window

# Global variable to store the mathematical expression
expression = ""

# Function to update the display when a button is clicked
def btn_click(item):
    global expression
    expression = expression + str(item)
    input_text.set(expression)

# Function to clear the input field
def btn_clear():
    global expression
    expression = ""
    input_text.set("")

# Function to calculate the final result
def btn_equal():
    global expression
    try:
        # eval() evaluates the string as a mathematical formula
        result = str(eval(expression))
        input_text.set(result)
        expression = result  # Allow further operations on the result
    except Exception:
        input_text.set("Error")
        expression = ""

# Tkinter variable to track input text
input_text = tk.StringVar()

# Create the display field
input_frame = tk.Frame(root, width=312, height=50, bd=0, highlightbackground="black", highlightthickness=1)
input_frame.pack(side=tk.TOP)

input_field = tk.Entry(input_frame, font=('arial', 18, 'bold'), textvariable=input_text, width=50, bg="#eee", bd=0, justify=tk.RIGHT)
input_field.grid(row=0, column=0)
input_field.pack(ipady=10)

# Create a frame for the buttons
btns_frame = tk.Frame(root, width=312, height=272.5, bg="grey")
btns_frame.pack()

# Define button layout: (Text, Row, Column, ColumnSpan)
buttons = [
    ('C', 0, 0, 3), ('/', 0, 3, 1),
    ('7', 1, 0, 1), ('8', 1, 1, 1), ('9', 1, 2, 1), ('*', 1, 3, 1),
    ('4', 2, 0, 1), ('5', 2, 1, 1), ('6', 2, 2, 1), ('-', 2, 3, 1),
    ('1', 3, 0, 1), ('2', 3, 1, 1), ('3', 3, 2, 1), ('+', 3, 3, 1),
    ('0', 4, 0, 2), ('.', 4, 2, 1), ('=', 4, 3, 1),
]

# Loop to create and place buttons in the grid
for (text, row, col, colspan) in buttons:
    action = lambda x=text: btn_click(x)
    if text == '=': action = btn_equal
    elif text == 'C': action = btn_clear
    
    tk.Button(btns_frame, text=text, width=10 if colspan == 1 else 21, height=3, bd=0, bg="#fff", 
              cursor="hand2", command=action).grid(row=row, column=col, columnspan=colspan, padx=1, pady=1)

root.mainloop() # Run the application