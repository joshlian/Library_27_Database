from tkinter import  *
import sqlite3
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