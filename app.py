from tkinter import *
import calendar

text=calendar.calendar(2020)

root=Tk()
root.geometry("500X600")
root.title("CALENDER")
label=Label(root, text="CALENDER",bg='dark gray', font=("times",28,'bold'))
label1.grid(row=1,column=1)
root.config(background="white")
l1=Label(root,text=text,font="Consoles 10")
L1.grid(row=2,column=1,padx=20)
root.mainloop()