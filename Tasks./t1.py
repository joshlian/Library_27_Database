from tkinter import *
import sqlite3

option1 = Tk()
option1.title('Check out a boox')
option1.geometry("400x400")

user = Label(option1, text = "Please enter the Book_loan Information below")
user.grid (row = 0, column = 1, padx = 10)



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
insert_btn = Button(option1, text = "Add Loan", command=Insert)
insert_btn.grid(row = 5, column = 0, columnspan = 2, padx = 10, pady = 10)

option1.mainloop()