from tkinter import *
from datetime import date

root = Tk()

root.geometry("400x300")
root.minsize(400,300)
root.maxsize(400,600)
root.title("Age Calculater")

f = Frame(root,bg="black")
f.pack(padx=20,pady=3)

main_lable = Label(f,text="Age Calculater",bg="orchid",fg="white",font="arial 20 bold",borderwidth=3,relief=SUNKEN)
main_lable.pack(pady=4,padx=5)

f1 = Frame(root,bg="purple",borderwidth=3,relief=GROOVE)
f1.pack(ipadx=200,ipady=1)

lable1 = Label(f1,text="Enter your date of birth",bg="navy blue",fg="white",font="lucida 12 bold",borderwidth=3,relief=SUNKEN)
lable1.pack(anchor="nw",fill=X,pady=5)

f2 = Frame(root,borderwidth=3,relief=GROOVE,bg="purple")
f2.pack(anchor="nw",pady=5,padx=3,ipadx=2,ipady=2)

calculate_button = Button(root,text="CALCULATE",bg="navy blue",fg="red",font="lucida 15 bold",borderwidth=3,relief=GROOVE)
calculate_button.pack(pady=40)

lable2 = Label(f2,text="Date:",bg="white",fg="navy blue",font="lucida 10 bold",borderwidth=3,relief=GROOVE)
lable2.pack(anchor="nw",pady=3,ipadx=28,padx=6)

date_entry = Entry(f2,width=8,borderwidth=3,relief=GROOVE)
date_entry.pack(anchor="n",ipadx=20)

f3 = Frame(root,bg="purple",borderwidth=3,relief=GROOVE)
f3.pack()

lable3 = Label(f3,text="Month:",bg="white",fg="navy blue",font="lucida 10 bold",borderwidth=3,relief=GROOVE)
lable3.pack(side=TOP,pady=3,ipadx=28,padx=6)

root.mainloop()