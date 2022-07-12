from tkinter import*

root = Tk()
root.title("Simple Calculator")
operator = ""
text_input = StringVar()
display = Entry (root,font = ("arial",20,"bold"),textvariable = text_input,insertwidth=4,bd=20,bg="powder blue")
display.grid(columnspan=4)

#first row beginning
btnclear =Button(root,text="C",padx=16,pady=16,bd=8,fg="black",bg="red",font=("arial",20,'bold'))
btnclear.grid(row = 1, column = 0)
btnmemory =Button(root,text="M",padx=16,pady=16,bd=8,fg="black",bg="red",font=("arial",20,'bold'))
btnmemory.grid(row = 1,column= 1 )
btnopen =Button(root,text="(",padx=16,pady=16,bd=8,fg="black",bg="red",font=("arial",20,'bold'))
btnopen.grid(row=1,column=2)
btnclose=Button(root,text=")",padx=16,pady=16,bd=8,fg="black",bg="red",font=("arial",20,'bold'))
btnclose.grid(row=1,column=3)

#first roll ending


# second row beginning
btn1=Button(root,text="1",padx=16,pady=16,bd=8,fg="white",bg="black",font=("arial",20,'bold'))
btn1.grid(row=2,column=0)
btn2=Button(root,text="2",padx=16,pady=16,bd=8,fg="white",bg="black",font=("arial",20,'bold'))
btn2.grid(row=2,column=1)
btn3=Button(root,text="3",padx=16,pady=16,bd=8,fg="white",bg="black",font=("arial",20,'bold'))
btn3.grid(row=2,column=2)
btn4=Button(root,text="+",padx=16,pady=16,bd=8,fg="white",bg="black",font=("arial",20,'bold'))
btn4.grid(row=2,column=3)
# second row ending

# third row beginning
btn8=Button(root,text="4",padx=16,pady=16,bd=8,fg="white",bg="black",font=("arial",20,'bold'))
btn8.grid(row=3,column=0)
btn9=Button(root,text="5",padx=16,pady=16,bd=8,fg="white",bg="black",font=("arial",20,'bold'))
btn9.grid(row=3,column=1)
btn3=Button(root,text="6",padx=16,pady=16,bd=8,fg="white",bg="black",font=("arial",20,'bold'))
btn3.grid(row=3,column=2)
btn4=Button(root,text="-",padx=16,pady=16,bd=8,fg="white",bg="black",font=("arial",20,'bold'))
btn4.grid(row=3,column=3)

# third row ending

# forth row beginning
btn1=Button(root,text="7",padx=16,pady=16,bd=8,fg="white",bg="black",font=("arial",20,'bold'))
btn1.grid(row=4,column=0)
btn2=Button(root,text="8",padx=16,pady=16,bd=8,fg="white",bg="black",font=("arial",20,'bold'))
btn2.grid(row=4,column=1)
btn3=Button(root,text="9",padx=16,pady=16,bd=8,fg="white",bg="black",font=("arial",20,'bold'))
btn3.grid(row=4,column=2)
btn4=Button(root,text="x",padx=16,pady=16,bd=8,fg="white",bg="black",font=("arial",20,'bold'))
btn4.grid(row=4,column=3)

# forth row ending

# fifth row beginning
btn1=Button(root,text="00",padx=16,pady=16,bd=8,fg="white",bg="black",font=("arial",20,'bold'))
btn1.grid(row=5,column=0)
btn2=Button(root,text="0",padx=16,pady=16,bd=8,fg="white",bg="black",font=("arial",20,'bold'))
btn2.grid(row=5,column=1)
btn3=Button(root,text=". ",padx=16,pady=16,bd=8,fg="white",bg="black",font=("arial",20,'bold'))
btn3.grid(row=5,column=2)
btn4=Button(root,text="=",padx=16,pady=16,bd=8,fg="white",bg="black",font=("arial",20,'bold'))
btn4.grid(row=5,column=3)
root.mainloop()
# fifth row ending
