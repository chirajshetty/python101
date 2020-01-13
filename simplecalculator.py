# importing TKinter 
from tkinter import *

#Open a window with title simple Calculator
window = Tk()
window.title("Simple Calculator")
window.geometry("400x400")
#window.resizable(0,0)

thickness = 13


########## FUNCTIONS #############

def btn_click(item):
    global expression
    expression = expression + str(item)
    input_text.set(expression)

def btn_clear():
    global expression
    expression = ""
    input_text.set("")

def btn_result():
    global expression
    expression = str(eval(expression))
    input_text.set(expression)

input_text = StringVar()
expression = ""



# Create input entry box
input_box = Entry(window, font= ('arial', 18, 'bold'), justify='right', textvariable = input_text)
input_box.grid(row=0, column=0, columnspan = 4)



# Create buttons 
number1 = Button(window,text = " 1 ",padx=40, pady=20, command = lambda:btn_click(1)).grid(column=0, row=1)
number2 = Button(window,text = " 2 ",padx=40, pady=20, command = lambda:btn_click(2)).grid(column=1, row=1)
number3 = Button(window,text = " 3 ",padx=40, pady=20, command = lambda:btn_click(3)).grid(column=2, row=1)
number4 = Button(window,text = " 4 ",padx=40, pady=20, command = lambda:btn_click(4)).grid(column=0, row=2)
number5 = Button(window,text = " 5 ",padx=40, pady=20, command = lambda:btn_click(5)).grid(column=1, row=2)
number6 = Button(window,text = " 6 ",padx=40, pady=20, command = lambda:btn_click(6)).grid(column=2, row=2)
number7 = Button(window,text = " 7 ",padx=40, pady=20, command = lambda:btn_click(7)).grid(column=0, row=3)
number8 = Button(window,text = " 8 ",padx=40, pady=20, command = lambda:btn_click(8)).grid(column=1, row=3)
number9 = Button(window,text = " 9 ",padx=40, pady=20, command = lambda:btn_click(9)).grid(column=2, row=3)
number0 = Button(window,text = " 0 ",padx=40, pady=20, command = lambda:btn_click(0)).grid(column=1,row=4)
clear = Button(window,text = " C ",padx=40, pady=20, command = lambda:btn_clear()).grid(column=0 , row=4)
answer = Button(window,text = " = ",padx=40, pady=20, command = lambda:btn_result()).grid(column=2 ,row=4)
ops_add = Button(window,text = " + ",padx=40, pady=20, command = lambda:btn_click("+")).grid(column=4,row=1)
ops_sub = Button(window,text = " - ",padx=40, pady=20, command = lambda:btn_click("-")).grid(column=4,row=2)
ops_mul = Button(window,text = " * ",padx=40, pady=20, command = lambda:btn_click("*")).grid(column=4,row=3)
ops_div = Button(window,text = " / ",padx=40, pady=20, command = lambda:btn_click("/")).grid(column=4,row=4)

window.mainloop() 


 
