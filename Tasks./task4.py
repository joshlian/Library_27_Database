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
