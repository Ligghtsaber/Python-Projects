from tkinter import *
import calendar

text = calendar.calendar(2024)

root = Tk()
root.geometry("600x700")
root.title("CALENDAR")
label1=Label(root,text="CALENDAR", bg='dark gray', font=("times", 28, 'bold', 'underline'))
label1.grid(row=1, column=1)
root.config(background="white")
l1 = Label(root,text=text,font=('courier', 12, 'bold'), justify=LEFT, bg='light gray')
l1.grid(row=2, column=1, padx=50)
root.mainloop()