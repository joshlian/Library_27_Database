from tkinter import *
import sqlite3


root = Tk()

root.title('USER_OPTIONS')
root.geometry("530x510")


def option_one():
	print("one")
def option_two():
	print("two")

def option_three():
	print("three")

def option_four():

	option4 = Tk()
	option4.title('List number of copies')
	option4.geometry("450x400")

	def print_copy():
		space = Label(option4, text ="")
		space.grid(row = 5, column =1)

		conn4 = sqlite3.connect('library.db')
		conn4_curr = conn4.cursor()
		conn4_curr.execute("SELECT branch_id, num_of_copies FROM BOOK_COPIES NATURAL JOIN BOOK WHERE title = ? GROUP BY branch_id",(book.get(),))
		getall = conn4_curr.fetchall()
		print_record = ('branch_ID    Copies'+"\n")
		for pall in getall:
			print_record += (str(pall[0]) + "               " + str(pall[1]) + "\n")
		printIT = Label(option4, text = print_record)
		printIT.grid(row = 6 , column = 1, columnspan = 2)

		conn4.close()
	space = Label(option4, text ="Type the book title you want to find out about")
	space.grid(row = 0, column =1, padx = 10)

	space = Label(option4, text ="")
	space.grid(row = 1, column =1)

	book = Entry(option4, width = 40)
	book.grid(row = 2, column =1)

	booktitle = Label(option4, text ="Book Title")
	booktitle.grid(row = 2, column =0)

	space = Label(option4, text ="")
	space.grid(row = 3, column =1)

	Button(option4,text = "Look up book count", command = print_copy).grid(row = 4, column =1)
	option4.mainloop()

def option_five():
	print("five")

def option_sixA():
	option6 = Tk()
	option6.title('List number of copies')
	option6.geometry("600x700")
	option6.mainloop()
def option_sixB():
    print("hi")
    



#Tell users what they can do
Explain = Label(root, text ='Please pick an option from the available menu below')
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

sixth_optionA = Entry(root, width = 30)
sixth_optionA.grid(row = 12, column = 1)
sixth_optionA.insert(0,"Get borrowers information")

space = Label(root, text ="")
space.grid(row = 13, column =1)

sixth_optionB = Entry(root, width = 30)
sixth_optionB.grid(row = 14, column = 1)
sixth_optionB.insert(0,"Get book information")

#spaces before we add out names 

space = Label(root, text ="")
space.grid(row = 15, column =1)

name1 = Label(root, text = 'Joshua Lian')
name1.grid(row = 16, column =1)

space = Label(root, text ="")
space.grid(row = 17, column =1)

name2 = Label(root, text = 'Kierra Ashford')
name2.grid(row = 18, column =1)

space = Label(root, text ="")
space.grid(row = 19, column =1)

name3 = Label(root, text = 'Abhinav Shrestha')
name3.grid(row = 20, column =1)




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

opt6A = Label(root, text = 'OPTION 6 A')
opt6A.grid(row = 12, column =0)

opt6B = Label(root, text = 'OPTION 6 B')
opt6B.grid(row = 14, column =0)



#create buttons
Button(root, text = "select", command = option_one).grid(row = 2, column =2)
Button(root, text = "select", command = option_two).grid(row = 4, column =2)
Button(root, text = "select", command = option_three).grid(row = 6, column =2)
Button(root, text = "select", command = option_four).grid(row = 8, column =2)
Button(root, text = "select", command = option_five).grid(row = 10, column =2)
Button(root, text = "select", command = option_sixA).grid(row = 12, column =2)
Button(root, text = "select", command = option_sixB).grid(row = 14, column =2)
root.mainloop()