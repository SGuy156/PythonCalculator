from tkinter import *

screen = Tk() #creates window
screen.title("Calculator") # Title
screen.geometry('180x230') #window dimensions - megethos
screen.resizable(height=False, width=False)
screen.configure(background="Black")

def clear():
    e.delete(0 , END)

# Function to evaluate the expression in the entry field
def equal():
    try:
        a = e.get()
        result = eval(a)
        e.delete(0, END)
        e.insert(END, result)
    except:
        e.delete(0,END)
        e.insert(END,"Err")

# Function to insert a number or operator into the entry field when a button is pressed
def press(number):
    e.insert(END, number)






#Gui
e = Entry(screen, width=15,font='Impact')
btn1 = Button(screen,text="1",bg="Black",fg="Green", width= 5, height = 2,command=lambda: press("1"))
btn2 = Button(screen,text="2",bg="Black",fg="Green", width= 5, height = 2,command=lambda: press("2"))
btn3 = Button(screen,text="3",bg="Black",fg="Green", width= 5, height = 2,command=lambda: press("3"))
btn4 = Button(screen,text="4",bg="Black",fg="Green", width= 5, height = 2,command=lambda: press("4"))
btn5 = Button(screen,text="5",bg="Black",fg="Green", width= 5, height = 2,command=lambda: press("5"))
btn6 = Button(screen,text="6",bg="Black",fg="Green", width= 5, height = 2,command=lambda: press("6"))
btn7 = Button(screen,text="7",bg="Black",fg="Green", width= 5, height = 2,command=lambda: press("7"))
btn8 = Button(screen,text="8",bg="Black",fg="Green", width= 5, height = 2,command=lambda: press("8"))
btn9 = Button(screen,text="9",bg="Black",fg="Green", width= 5, height = 2,command=lambda: press("9"))
btn0 = Button(screen,text="0",bg="Black",fg="Green", width= 5, height = 2,command=lambda: press("0"))
btndot = Button(screen,text=".",bg="Black",fg="Green", width= 5, height = 2,command=lambda: press("."))
btnclear = Button(screen,text="Clear",bg="Black",fg="Green", width= 5, height = 2,command=clear)
btnequal = Button(screen,text="=",bg="Black",fg="Green", width= 15, height = 2,command=equal)
btnplus = Button(screen,text="+",bg="Black",fg="Green", width= 5, height = 2,command=lambda: press("+"))
btnminus = Button(screen,text="-",bg="Black",fg="Green", width= 5, height = 2,command=lambda: press("-"))
btndivide = Button(screen,text="/",bg="Black",fg="Green", width= 5, height = 2,command=lambda: press("/"))
btnmultiply = Button(screen,text="*",bg="Black",fg="Green", width= 5, height = 2,command=lambda: press("*"))

#grid placement
e.grid(row=0,column=0,columnspan=6)
btn7.grid(row=1,column=0)
btn8.grid(row=1,column=1)
btn9.grid(row=1,column=2)
btndivide.grid(row=1,column=3)

btn4.grid(row=2,column=0)
btn5.grid(row=2,column=1)
btn6.grid(row=2,column=2)
btnmultiply.grid(row=2,column=3)

btn1.grid(row=3,column=0)
btn2.grid(row=3,column=1)
btn3.grid(row=3,column=2)
btnminus.grid(row=3,column=3)

btnclear.grid(row=4,column=0)
btn0.grid(row=4,column=1)
btndot.grid(row=4,column=2)
btnplus.grid(row=4,column=3)

btnequal.grid(row=5,column=0,columnspan=6)







screen.mainloop() #teleftaia entolh klenei programma

