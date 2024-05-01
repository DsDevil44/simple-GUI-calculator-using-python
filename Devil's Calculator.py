from tkinter import *
exp=''
def press(num):
    global exp
    exp = exp + str(num)
    equation.set(exp)
def eq():
    try:
        global exp
        total=str(eval(exp))
        equation.set(total)
        exp=''
    except:
        equation.set(" error ")
        exp = ""
def clear():
    global exp
    exp = ""
    equation.set("")
def back():
    global exp
    exp=exp[:len(exp)-1]
    equation.set(exp)
if __name__ == "__main__":
    m=Tk()
    m.configure(background="black")
    m.title("Simple Calculator")
    m.geometry("500x175")
    equation=StringVar()
    expr_field = Entry(m, textvariable=equation)
    expr_field.grid(columnspan=5, ipadx=70)
    w=Button(m,text='1',width=7,command=lambda: press(1)).grid(row=2,column=0)
    w=Button(m,text='2',width=7,command=lambda: press(2)).grid(row=2,column=1)
    w=Button(m,text='3',width=7,command=lambda: press(3)).grid(row=2,column=2)
    w=Button(m,text='4',width=7,command=lambda: press(4)).grid(row=3,column=0)
    w=Button(m,text='5',width=7,command=lambda: press(5)).grid(row=3,column=1)
    w=Button(m,text='6',width=7,command=lambda: press(6)).grid(row=3,column=2)
    w=Button(m,text='7',width=7,command=lambda: press(7)).grid(row=4,column=0)
    w=Button(m,text='8',width=7,command=lambda: press(8)).grid(row=4,column=1)
    w=Button(m,text='9',width=7,command=lambda: press(9)).grid(row=4,column=2)
    w=Button(m,text='0',width=7,command=lambda: press(0)).grid(row=5,column=1)
    w=Button(m,text='.',width=7,command=lambda: press('.')).grid(row=5,column=0)
    w=Button(m,text='+',width=7,command=lambda: press('+')).grid(row=2,column=4)
    w=Button(m,text='-',width=7,command=lambda: press('-')).grid(row=3,column=4)
    w=Button(m,text='*',width=7,command=lambda: press('*')).grid(row=4,column=4)
    w=Button(m,text='/',width=7,command=lambda: press('/')).grid(row=5,column=4)
    w=Button(m,text='(',width=7,command=lambda: press('(')).grid(row=2,column=5)
    w=Button(m,text=')',width=7,command=lambda: press(')')).grid(row=3,column=5)
    w=Button(m,text='Clear',width=7,command=clear).grid(row=5,column=5)
    w=Button(m,text='Backspace',width=7,command=back).grid(row=4,column=5)
    w=Button(m,text='enter',width=7,command=eq).grid(row=5,column=2)
    m.mainloop()
