from tkinter import *
import sqlite3


root = Tk()

root.title('Library Management System')
root.geometry("530x510")

def option_one():
	option1 = Tk()
	option1.title('Check out a boox')
	option1.geometry("400x400")


	#create the labels for check out a book

	bookid_label = Label (option1, text = 'Book ID: ')
	bookid_label.grid(row = 0, column = 0)

	branchid_label = Label (option1, text = 'Branch ID: ')
	branchid_label.grid(row = 1, column = 0)

	cardno_label = Label (option1, text = 'Card No.: ')
	cardno_label.grid(row = 2, column = 0)
	
	#building the GUI componenets (text boxes) for check out a book

	bookid = Entry(option1, width = 30)
	bookid.grid(row = 0, column = 1, padx = 20)

	branchid = Entry(option1, width = 30)
	branchid.grid(row = 1, column = 1, padx = 20)

	cardno = Entry(option1, width = 30)
	cardno.grid(row = 2, column = 1, padx = 20)


	def Insert():
    	#Connect to the databse
		check_conn = sqlite3.connect('library.db')
		check_cur = check_conn.cursor()

		#Get values from the text entry
		book_id = bookid.get()
		branch_id = branchid.get()
		card_no = cardno.get()

		check_cur.execute("INSERT INTO BOOK_LOANS (book_id, branch_id, card_no, date_out, due_date) VALUES (?,?,?, DATE('now'), DATE('now', '+30 days'))", (book_id, branch_id, card_no))
		#commit changes
		check_conn.commit()
		check_conn.close()

	#Creating a button to insert the values
	Button(option1, text = "Add Loan", command=Insert).grid(row = 5, column = 0, columnspan = 2, padx = 10, pady = 10)
	
	option1.mainloop()

def option_two():
	option2 = Tk()
	option2.title("Insert Borrower")
	option2.geometry("400x400")

	option_conn = sqlite3.connect('library.db')
	option_two_cur = option_conn.cursor()


	def addBorrower():
		submit_conn = sqlite3.connect('library.db')

		submit_cur = submit_conn.cursor()
		submit_cur.execute("INSERT INTO BORROWERS (name,phone,address) VALUES (:name, :phone, :address) ",
		{   
			'name': name.get(),
			'phone': phone.get(),
			'address': address.get(),
		})
	
		submit_conn.commit()
		submit_conn.close()
	
	name = Entry(option2, width = 30)
	name.grid(row = 3, column = 1)
        
	name_label = Label(option2, text = 'Name') 
	name_label.grid(row = 3, column = 0)
	space = Label(option2, text ="")
	space.grid(row = 4, column =0)


	phone= Entry(option2, width = 30)
	phone.grid(row = 5, column = 1)
        
	phone_label = Label(option2, text = 'Phone') 
	phone_label.grid(row = 5, column = 0)
	space = Label(option2, text ="")
	space.grid(row = 6, column =0)

        
	address = Entry(option2, width = 30)
	address.grid(row = 7, column = 1)
        
	address_label = Label(option2, text = 'Address') 
	address_label.grid(row = 7, column = 0)
	space = Label(option2, text ="")
	space.grid(row = 8, column =0)


	submit_btn = Button(option2, text ='Add Borrower ', command = addBorrower)
	submit_btn.grid(row = 10, column =0, columnspan = 2, pady = 10, padx = 10, ipadx = 140)


	option_conn.commit()
	#close the DB connection
	option_conn.close()
	option2.mainloop()

def option_three():
	def option_three_submit():
		option_conn = sqlite3.connect('library.db')
		option_three_cur = option_conn.cursor()
		option_three_cur.execute("INSERT INTO BOOK VALUES (:book_id, :title, :book_publisher) ",
		{   'book_id': book_id.get(),
			'title': title.get(),
			'book_publisher': book_publisher.get(),
			
			
			
		})
		option_three_cur.execute("INSERT INTO BOOK_AUTHORS VALUES (:book_id, :author)",
			  {
				  'book_id': book_id.get(),
				  'author' : author.get(),
			  })
		option_conn.commit()
		option_conn.close()
	
	option3 = Tk()
	option3.title( "Add a Book")
	option3.geometry("400x400")

	option_conn = sqlite3.connect('library.db')
	option_three_cur = option_conn.cursor()

	book_id = Entry(option3, width = 30)
	book_id.grid(row = 1, column = 1)
	
	book_id_label = Label(option3, text ='book_id') 
	book_id_label.grid(row = 1, column = 0)
	space = Label(option3, text ="")
	space.grid(row = 2, column =0)


	title = Entry(option3, width = 30)
	title.grid(row = 3, column = 1)
	
	title_label = Label(option3, text = 'title') 	

	title_label.grid(row = 3, column = 0)
	space = Label(option3, text ="")
	space.grid(row = 4, column =0)


	book_publisher= Entry(option3, width = 30)
	book_publisher.grid(row = 5, column = 1)
	
	book_publisher_label = Label(option3, text = 'book_publisher') 	
	book_publisher_label.grid(row = 5, column = 0)
	space = Label(option3, text ="")
	space.grid(row = 6, column =0)
       
	 
    
	author = Entry(option3, width = 30)
	author.grid(row = 7, column = 1)
	
	author_label = Label(option3, text = 'author') 	
	author_label.grid(row = 7, column = 0)
	space = Label(option3, text ="")
	space.grid(row = 8, column =0)
       

	submit_btn = Button(option3, text ='Add Book ', command = option_three_submit)
	submit_btn.grid(row = 10, column =0, columnspan = 2, pady = 10, padx = 10, ipadx = 140)


	option_conn.commit()
	option_conn.close()
	option3.mainloop()


def option_four():
#created a new Tkinter GUI
	option4 = Tk()
	option4.title('List number of copies')
	option4.geometry("450x400")

	def print_copy():

		conn4 = sqlite3.connect('library.db')
		conn4_curr = conn4.cursor()
		conn4_curr.execute("SELECT branch_id, num_of_copies FROM BOOK_COPIES NATURAL JOIN BOOK WHERE title = ? GROUP BY branch_id",(book.get(),))
		getall = conn4_curr.fetchall()
        
        #writes the names of the heading 
		space = Label(option4, text ="")
		space.grid(row = 5, column =1)
		Printing = Label(option4, text = "Branch_ID")
		Printing.grid(row = 6, column = 0)
		Printing = Label(option4, text = "Book_Count")
		Printing.grid(row = 6, column = 1)
		space = Label(option4, text ="")
		space.grid(row = 7, column =1)
		count = 8
        #looks for instances where the branch ID is in match with the book title 
		for pall in getall:
			Printing1 = Entry(option4, width = 0)
			Printing1.grid(row =count, column = 0)
			Printing = Label(option4, text = pall[0])
			Printing.grid(row = count, column = 0)
			Printing = Label(option4, text = pall[1])
			Printing.grid(row = count, column = 1)
			count += 1

		conn4.close()
        
    #set up the Entires and lables for task 4
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
	option5 = Tk()
	option5.title('Check Late Books')
	option5.geometry("800x400")

	#Hint for the GUI interface
	hint = Label(option5, text = "Please enter a range of dates below to check if books are returned late")
	hint.grid (row = 0, column = 1, padx = 10)
	
	#Create labels for the options for the GUI
	datefrom_label = Label(option5, text = 'Date From: ')
	datefrom_label.grid(row = 1, column = 0, padx = 10, pady = 10)

	dateto_label = Label (option5, text = 'Date To: ')
	dateto_label.grid(row = 2, column = 0, padx= 10, pady =10)

	#Create text boxes for GUI
	datefrom = Entry(option5, width = 30)
	datefrom.grid(row = 1, column = 1, padx = 20)

	dateto = Entry(option5, width = 30)
	dateto.grid(row = 2, column = 1, padx = 20)


	def Search():
		#Connect to database
		search_conn = sqlite3.connect('library.db')
		search_cur = search_conn.cursor()

		#Get values entered in the text box
		date_from = datefrom.get()
		date_to = dateto.get()

		#Execute the sqlite command here
		search_cur.execute("SELECT book_id, branch_id, card_no, date_out, due_date, returned_date, (JULIANDAY(returned_date)- JULIANDAY(due_date)) AS Days_late FROM BOOK_LOANS WHERE returned_date > due_date AND (due_date >= ? AND due_date <= ?)", (date_from, date_to))


		search_records = search_cur.fetchall()

		header_label = Label(option5, text = 'book_id\t\tbranch_id\t\tcard_no\t\tdate_out\t\tdue_date\t\treturned date\t\tDays Late')
		header_label.grid(row = 6, column = 1, padx = 10)

		print_record = ''

		for search_record in search_records:
			print_record += "\t\t" + str(search_record[0]) + "\t\t" + str(search_record[1]) + "\t\t" + str(search_record[2]) + "\t\t" + str(search_record[3]) + "\t\t" + str(search_record[4]) + "\t\t" + str(search_record[5]) + "\t\t" + str(search_record[6]) + "\n"
    
		search_label = Label(option5, text = print_record)
		search_label.grid(row = 7, column = 1, padx = 10, pady= 10)
		#commit changes
		search_conn.commit()
		search_conn.close()
    
	#Creating a button for searching late books within the entered date range
	search_btn = Button (option5, text = "Search", command = Search)
	search_btn.grid (row = 4, column = 0, columnspan = 2, padx = 10, pady = 10)

	option5.mainloop()

def option_sixA():
	option6A = Tk()
	option6A.title('Get borrowers info')
	option6A.geometry("600x850")

	def FunctionSixA(num):
		submit_conn = sqlite3.connect('library.db')
		submit_cur = submit_conn.cursor()
        
        #if statement that runs a query depending on what number is passed in
		if num == 0:
			submit_cur.execute("select Borrower_name, card_no, Total_Late_Fee_Balance FROM vBookLoanInfo WHERE Borrower_name LIKE '%'||:name||'%'",(name.get(),))
            
		if num == 1:
			submit_cur.execute("select Borrower_name, card_no, Total_Late_Fee_Balance from vBookLoanInfo where card_no = :card_no" ,
			{
				'card_no':ID.get(),
			})
            
		if num == 2:
			submit_cur.execute("SELECT Borrower_name, card_no, Total_late_Fee_Balance FROM vBookLoanInfo ORDER BY Total_Late_Fee_Balance")
            
		getRecords = submit_cur.fetchall()
        
        #used a to line the titles up in the printout 
		space = Label(option6A, text ="")
		space.grid(row = 8, column =1)
		Printing = Label(option6A, text = "Borrower_name")
		Printing.grid(row = 9, column = 0)
		Printing = Label(option6A, text = "Card_no")
		Printing.grid(row = 9, column = 1)
		Printing = Label(option6A, text = "Total_Late_Fee_Balance")
		Printing.grid(row = 9, column = 2)
		space = Label(option6A, text ="")
		space.grid(row = 10, column =1)
		
        #this is to help keep increment the rows so things print nicely 
        #stored the values in an array and gave that value to a lable. Used entry to help line up 
		count = 11
		for evsky in getRecords:
			Printing1 = Entry(option6A, width = 0)
			Printing1.grid(row =count, column = 0)
			Printing = Label(option6A, text = evsky[0])
			Printing.grid(row = count, column = 0)
			Printing = Label(option6A, text = evsky[1])
			Printing.grid(row = count, column = 1)
			Printing = Label(option6A, text = "$" + str(format(evsky[2],".2f")))
			Printing.grid(row = count, column = 2)
			count +=1
		submit_conn.close()

    #setting up the entries and lables for Option 6
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

	#buttons and pass in vale into the function
	Button(option6A, text="Search Name", command=lambda: FunctionSixA(0)).grid(row=1, column=2)
	Button(option6A, text="Search ID", command=lambda: FunctionSixA(1)).grid(row=3, column=2)
	Button(option6A, text="Search All", command=lambda: FunctionSixA(2)).grid(row=5, column=1)

	space = Label(option6A, text ="")
	space.grid(row = 6, column =1)

def option_sixB():
	option6B = Tk()
	option6B.title('Get book info')
	option6B.geometry("800x900")

	def FunctionSixB(num):
		submit_conn = sqlite3.connect('library.db')
		submit_cur = submit_conn.cursor()
        #same form of if statement as 6A
		if num == 0:
			submit_cur.execute("SELECT BV.title, B.book_id, Total_late_Fee_Balance FROM (vBookLoanInfo AS BV JOIN BOOK AS B on B.title = BV.title) WHERE BV.title LIKE '%'||:name||'%'",(B_name.get(),))
            
		if num == 1:
			submit_cur.execute("SELECT BV.title, B.book_id, Total_late_Fee_Balance FROM (vBookLoanInfo AS BV JOIN BOOK AS B on B.title = BV.title) WHERE book_id = :book_id" ,
		{
			'book_id':B_ID.get(),
		})

		if num == 2:
			submit_cur.execute("SELECT BV.title, B.book_id, Total_late_Fee_Balance FROM (vBookLoanInfo AS BV JOIN BOOK AS B on B.title = BV.title) ORDER BY Total_Late_Fee_Balance DESC")
            
		getRecords = submit_cur.fetchall()
        
        #used a to line the titles up in the printout 
		space = Label(option6B, text ="")
		space.grid(row = 8, column =1)
		Printing = Label(option6B, text = "Borrower_name")
		Printing.grid(row = 9, column = 0)
		Printing = Label(option6B, text = "Card_no")
		Printing.grid(row = 9, column = 1)
		Printing = Label(option6B, text = "Total_Late_Fee_Balance")
		Printing.grid(row = 9, column = 2)
		space = Label(option6B, text ="")
		space.grid(row = 10, column =1)
		
        #this is to help keep increment the rows so things print nicely 
        #stored the values in an array and gave that value to a lable. Used entry to help line up 
		count = 11
		for evsky in getRecords:
			Printing1 = Entry(option6B, width = 0)
			Printing1.grid(row =count, column = 0)
			Printing = Label(option6B, text = evsky[0])
			Printing.grid(row = count, column = 0)
			Printing = Label(option6B, text = evsky[1])
			Printing.grid(row = count, column = 1)
            
            #if the late balance is 0 then it will print "not_apppliciable
			Printing = Label(option6B, text = ("Non-Applicable" if evsky[2] == 0 else ("$" + str(format(evsky[2],".2f")))))
			Printing.grid(row = count, column = 2)
			count +=1
		submit_conn.close()


    #sets up entries and lables for task 6B
	Instruct = Label(option6B, text = "Enter a Title or book ID or hit Search All")
	Instruct.grid(row = 0, column =1, padx = 10)

	space = Label(option6B, text ="")
	space.grid(row = 1, column =1)

	B_name = Entry(option6B, width = 30)
	B_name.grid(row = 1, column = 1)  

	space = Label(option6B, text ="")
	space.grid(row = 2, column =1)

	B_ID = Entry(option6B, width  = 30)
	B_ID.grid(row = 3, column = 1)  

	space = Label(option6B, text ="")
	space.grid(row = 4, column =1)

	nameLabel = Label(option6B, text = "Book Name")
	nameLabel.grid(row = 1 , column =0)

	IDLabel = Label(option6B, text = "Book ID")
	IDLabel.grid(row = 3, column =0)

	#buttons and passes in number into the function 
	Button(option6B,text="Search Book",command=lambda: FunctionSixB(0)).grid(row = 1, column =2)
	Button(option6B,text="Search ID",command=lambda: FunctionSixB(1)).grid(row = 3, column =  2)
	Button(option6B,text="Search All",command=lambda: FunctionSixB(2)).grid(row = 5, column =  1)
	space = Label(option6B, text ="")
	space.grid(row = 6, column =1)
    



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
