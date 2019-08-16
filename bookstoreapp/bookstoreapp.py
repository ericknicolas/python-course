"""
A program that stores this book info:
Title, Author, Year, ISBN

User can:
View all records
Search an entry
Add an entry
Update an entry
Delete an entry
Close
"""

from tkinter import *

window = Tk()

lblTitle = Label(window, text = "Title")
lblTitle.grid(row = 0, column = 0)

lblAuthor = Label(window, text = "Author")
lblAuthor.grid(row = 0, column = 2)

lblYear = Label(window, text = "Year")
lblYear.grid(row = 1, column = 0)

lblISBN = Label(window, text = "ISBN")
lblISBN.grid(row = 1, column = 2)

title_text = StringVar()
enTitle = Entry(window, textvariable = title_text)
enTitle.grid(row = 0, column = 1)

author_text = StringVar()
enAuthor = Entry(window, textvariable = author_text)
enAuthor.grid(row = 0, column = 3)

year_text = StringVar()
enYear = Entry(window, textvariable = year_text)
enYear.grid(row = 1, column = 1)

isbn_text = StringVar()
enISBN = Entry(window, textvariable = isbn_text)
enISBN.grid(row = 1, column = 3)

lsBox = Listbox(window, height = 6, width = 35)
lsBox.grid(row = 2, column = 0, rowspan = 6, columnspan = 2)

sb = Scrollbar(window)
sb.grid(row = 2, column = 2, rowspan = 6)

lsBox.configure(yscrollcommand = sb.set)
sb.configure(command = lsBox.yview)

btnViewAll = Button(window, text = "View All", width = 12)
btnViewAll.grid(row = 2, column = 3)

btnSearch = Button(window, text = "Search Entry", width = 12)
btnSearch.grid(row = 3, column = 3)

btnAdd = Button(window, text = "Add Entry", width = 12)
btnAdd.grid(row = 4, column = 3)

btnUpdate = Button(window, text = "Update Entry", width = 12)
btnUpdate.grid(row = 5, column = 3)

btnDelete = Button(window, text = "Delete Entry", width = 12)
btnDelete.grid(row = 6, column = 3)

btnDelete = Button(window, text = "Close", width = 12)
btnDelete.grid(row = 7, column = 3)

window.mainloop()