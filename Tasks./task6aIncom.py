
def option6A():
	option6A = Tk()
	option6A.title('Get borrowers info')
	option6A.geometry("600x700")

	def searchName():
		submit_conn = sqlite3.connect('library.db’')
		submit_cur = submit_conn.cursor()
		submit_cur.execute("select card_no, Borrower_name, Total_Late_Fee_Balance from vBookLoanInfo where name = %:name%;"  ,
		{
			'name': name.get(),

		})
		getRecords = submit_conn.fetchall()
		print_record = ("Card_no    |  Borrower_Name     | Total_Late_Fee_Balance" + "\n")
		for  evsky in getRecords:
				print_record += (str(evsky[0]) + "       "  + str(evsky[1]) + "      $" str(evsky[2]) + "\n")
		printFinal = Label(option6A, text = print_record)
		printFinal.grid(row = 7, column = 1, columnspan = 3)
		submit_conn.close()
                                    



	def searchID():
		IDsearch_conn = sqlite3.connect('library.db')
	
		submit_cur = IDsearch_conn.cursor()
		submit_cur.execute("select card_no, Borrower_name, Total_Late_Fee_Balance from vBookLoanInfo where card_no = :card_no;"  ,
		{
			'card_no':ID.get(),

		})
		getRecords = IDsearch_conn.fetchall()
		print_record = ("Card_no    |  Borrower_Name     | Total_Late_Fee_Balance" + "\n")
		for  evsky in getRecords:
			print_record+= (str(evsky[0]) + "        "  + str(evsky[1]) + "      $" + str(evsky[2]) + "\n")
			printFinal = Label(option6A, text = print_record)
			printFinal.grid(row = 7, column = 1, columnspan = 3)
			IDsearch_conn.close()


#Def search_everyhting():
	#Everyhting_conn = sqlite3.connection


	Instruct = Label(option6A, text = "Enter a name or an ID or hit Search All")
	Instruct.grid(row = 0, column =1, padx = 10)

	space = Label(option6A, text ="")
	space.grid(row = 1, column =1)

	name = Entry(option6A, width = 30)
	name.grid(row = 1, column = 1)  

	space = Label(option6A, text ="")
	space.grid(row = 2, column =1)

	ID = Entry(option6A, width  = 30)
	ID.grid(row = 3, column = 1)  

	space = Label(option6A, text ="")
	space.grid(row = 4, column =1)

	nameLabel = Label(option6A, text = "Enter Name")
	nameLabel.grid(row = 1 , column =0)

	IDLabel = Label(option6A, text = "Enter ID")
	IDLabel.grid(row = 3, column =0)

	#buttons
	Button(option6A,text="Search Name",command= searchName).grid(row = 1, column =2)
	Button(option6A,text="Search ID",command= searchID).grid(row = 3, column =  2)
	Button(option6A,text="Search All",command= search_everything).grid(row = 5, column =  1)

	print("six")