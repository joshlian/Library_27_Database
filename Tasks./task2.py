from tkinter import *
import sqlite3

def option2():
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
        

