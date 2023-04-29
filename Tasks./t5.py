from tkinter import *
import sqlite3

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
    search_cur.execute("SELECT book_id, branch_id, card_no, date_out, due_date, returned_date, (JULIANDAY(returned_date)- JULIANDAY(due_date)) AS Days_late FROM BOOK_LOANS WHERE returned_date > due_date AND (returned_date > ? AND returned_date < ?)", (date_from, date_to))


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