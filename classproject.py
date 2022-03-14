from tkinter import *

def btnclick(numbers):
    global operator
    operator = operator + str(numbers)
    text_input.set(operator)

def btnClear():
    global operator
    operator=""
    text_input.set("")


def btnEquals():
    global operator
    sump = str(eval(operator))
    text_input.set(sump)
    operator=""


root =Tk ()
root.title("calculator")
operator= ""
text_input = StringVar()
display = Entry(root,font=('arial',20,'bold'),insertwidth=4,textvariable=text_input,bd=30,bg='powder blue',justify="right")
display.grid(columnspan=4)

btnclear = Button(root,text="C",padx=16,pady=16,bd=8,fg="black",bg='powder blue',font=('arial',20,'bold'),command=btnClear)
btnclear.grid(row=1,column=0)

btnmemory = Button(root,text="M",padx=16,pady=16,bd=8,fg="black",bg='powder blue',font=('arial',20,'bold'))
btnmemory.grid(row=1,column=1)

btnopen = Button(root,text="(",padx=16,pady=16,bd=8,fg="black",bg='powder blue',font=('arial',20,'bold'))
btnopen.grid(row=1,column=2)

btnclose = Button(root,text=")",padx=16,pady=16,bd=8,fg="black",bg='powder blue',font=('arial',20,'bold'))
btnclose.grid(row=1,column=3)

btn9 = Button(root,text="9",padx=16,bd=8,fg="black",font=('arial',20,'bold'),bg='powder blue',command=lambda:btnclick(9))
btn9.grid(row=2,column=0)

btn8 = Button(root,text="8",padx=16,bd=8,fg="black",font=('arial',20,'bold'),bg='powder blue',command=lambda:btnclick(8))
btn8.grid(row=2,column=1)

btn7 = Button(root,text="7",padx=16,bd=8,fg="black",font=('arial',20,'bold'),bg='powder blue',command=lambda:btnclick(7))
btn7.grid(row=2,column=2)

btndiv = Button(root,text="/",padx=16,bd=8,fg="black",font=('arial',20,'bold'),bg='powder blue',command=lambda:btnclick("/"))
btndiv.grid(row=2,column=3)

btn6 = Button(root,text="6",padx=16,bd=8,fg="black",font=('arial',20,'bold'),bg='powder blue',command=lambda:btnclick(6))
btn6.grid(row=3,column=0)

btn5 = Button(root,text="5",padx=16,bd=8,fg="black",font=('arial',20,'bold'),bg='powder blue',command=lambda:btnclick(5))
btn5.grid(row=3,column=1)

btn4 = Button(root,text="4",padx=16,bd=8,fg="black",font=('arial',20,'bold'),bg='powder blue',command=lambda:btnclick(4))
btn4.grid(row=3,column=2)

btnsub = Button(root,text="-",padx=16,bd=8,fg="black",font=('arial',20,'bold'),bg='powder blue',command=lambda:btnclick("-"))
btnsub.grid(row=3,column=3)

btn3 = Button(root,text="3",padx=16,bd=8,fg="black",font=('arial',20,'bold'),bg='powder blue',command=lambda:btnclick(3))
btn3.grid(row=4,column=0)

btn2 = Button(root,text="2",padx=16,bd=8,fg="black",font=('arial',20,'bold'),bg='powder blue',command=lambda:btnclick(2))
btn2.grid(row=4,column=1)

btn1 = Button(root,text="1",padx=16,bd=8,fg="black",font=('arial',20,'bold'),bg='powder blue',command=lambda:btnclick(1))
btn1.grid(row=4,column=2)

btnmult = Button(root,text="*",padx=16,bd=9,fg="black",font=('arial',20,'bold'),bg='powder blue',command=lambda:btnclick("*"))
btnmult.grid(row=4,column=3)

btn0 = Button(root,text="0",padx=16,bd=8,fg="black",font=('arial',20,'bold'),bg='powder blue',command=lambda:btnclick(0))
btn0.grid(row=5,column=0)

btndot = Button(root,text=".",padx=16,bd=8,fg="black",font=('arial',20,'bold'),bg='powder blue',command=lambda:btnclick("."))
btndot.grid(row=5,column=1)

btnEqual = Button(root,text="=",padx=16,bd=8,fg="black",font=('arial',20,'bold'),bg='powder blue',command=btnEquals)
btnEqual.grid(row=5,column=2)

btnadd = Button(root,text="+",padx=16,bd=8,fg="black",font=('arial',20,'bold'),bg='powder blue',command=lambda:btnclick("+"))
btnadd.grid(row=5,column=3)

root.mainloop()