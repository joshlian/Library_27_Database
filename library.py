from tkinter import *
import sqlite3

conn = sqlite3.connect('library.db')

conn.close()
root = Tk()

root.title('USER_OPTIONS')
root.geometry("550x500")


def option_one():
	option1 = Tk()
	option1.title('First Option')
	option1.geometry("200x200")
	option1.mainloop()

def option_two():
	print("two")

def option_three():
	print("three")

def option_four():
	print("four")

def option_five():
	print("five")

def option_six():
	print("six")



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

space = Label(root, text ="")
space.grid(row = 3, column =1)

second_option = Entry(root, width = 30)
second_option.grid(row = 4, column = 1)
second_option.insert(0,"Add a new borrower")

space = Label(root, text ="")
space.grid(row = 5, column =1)

third_option = Entry(root, width = 30)
third_option.grid(row = 6, column = 1)
third_option.insert(0,"Add a book and publisher")

space = Label(root, text ="")
space.grid(row = 7, column =1)

fourth_option = Entry(root, width = 30)
fourth_option.grid(row = 8, column = 1)
fourth_option.insert(0,"List book copies per branch")

space = Label(root, text ="")
space.grid(row = 9, column =1)

fifth_option = Entry(root, width = 30)
fifth_option.grid(row = 10, column = 1)
fifth_option.insert(0,"Book return information")

space = Label(root, text ="")
space.grid(row = 11, column =1)

sixth_option = Entry(root, width = 30)
sixth_option.grid(row = 12, column = 1)
sixth_option.insert(0,"Get a view result")

#spaces before we add out names 
space = Label(root, text ="")
space.grid(row = 13, column =1)

space = Label(root, text ="")
space.grid(row = 14, column =1)

name1 = Label(root, text = 'Joshua Lian')
name1.grid(row = 15, column =1)

space = Label(root, text ="")
space.grid(row = 16, column =1)

name2 = Label(root, text = 'Kierra Ashford')
name2.grid(row = 17, column =1)

space = Label(root, text ="")
space.grid(row = 18, column =1)

name3 = Label(root, text = 'Abhinav Shrestha')
name3.grid(row = 19, column =1)




#lables before the entry explanation
opt1 = Label(root, text = 'OPTION 1')
opt1.grid(row = 2, column =0)

opt2 = Label(root, text = 'OPTION 2')
opt2.grid(row = 4, column =0)

opt3 = Label(root, text = 'OPTION 3')
opt3.grid(row = 6, column =0)

opt4 = Label(root, text = 'OPTION 4')
opt4.grid(row = 8, column =0)

opt5 = Label(root, text = 'OPTION 5')
opt5.grid(row = 10, column =0)

opt6 = Label(root, text = 'OPTION 6')
opt6.grid(row = 12, column =0)




#create buttons
Button(root, text = "select", command = option_one).grid(row = 2, column =2)
Button(root, text = "select", command = option_two).grid(row = 4, column =2)
Button(root, text = "select", command = option_three).grid(row = 6, column =2)
Button(root, text = "select", command = option_four).grid(row = 8, column =2)
Button(root, text = "select", command = option_five).grid(row = 10, column =2)
Button(root, text = "select", command = option_six).grid(row = 12, column =2)

root.mainloop()
