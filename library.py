from tkinter import *
import sqlite3

conn = sqlite3.connect('library.db')

conn.close()
root = Tk()

root.title('USER_OPTIONS')
root.geometry("600x600")


def option_one():
	print("this really sucks")



#Tell users what they can do
Explain = Label(root, text ="Please pick an option from the available menu below")
Explain.grid(row = 0, column = 1, padx = 10)

#printf a space between the rows for better look
space = Label(root, text ="")
space.grid(row = 1, column =1)

#Enters the info about the option in Entry for better clarity
first_option = Entry(root, width = 30)
first_option.grid(row = 2, column = 1)
first_option.insert(0,"Check out a book")

#lables before the entry explanation
opt1 = Label(root, text = 'OPTION 1')
opt1.grid(row = 2, column =0)

#create buttons
Button(root, text = "select", command = option_one).grid(row = 2, column =2)
root.mainloop()
