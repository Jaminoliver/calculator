from tkinter import*

root = Tk()
root.geometry("500x500")
root.title("Welcome ")
txt = Label(root,text = "Testing entry")
txt.pack()
e=Entry(root, width= 50)
e.pack()

def myclick():
    hello = e.get()
    myresult = Label (root, text= hello)
    myresult.pack()
btn1 =Button(root,text= "submit",command = myclick)
btn1.pack()
root.mainloop()