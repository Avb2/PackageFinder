from tkinter import *
from bs4 import BeautifulSoup
import requests
import pyperclip as pc

# Initiate tkinter
root = Tk()


# Function that will be initiated when the enter button is clicked
def SearchIt():
    # Clears the label that displays the pip command
    def clear_text():
        display.destroy()

    # User search takes the users search and adds it to the url
    search = SearchBox.get()

    # Requests and Beautifulsoup the url + the user search
    req = requests.get(f'https://pypi.org/project/{search}')
    result = BeautifulSoup(req.text, 'html.parser')

    try:

        # Scrape for the pip command
        pip_command = result.find('span', {'id': 'pip-command'})
        found = pip_command.text

        # If command is found, it will be displayed
        display = Label(root, text=found)
        display.grid(row=1, column=1)

        # Clear button gains the clear_text() command
        Clear = Button(text='Clear', command=lambda: clear_text())
        Clear.grid(row=1, column=0)

        # Copy button
        Copy = Button(root, text='Copy', command=pc.copy(found))
        Copy.grid(row=3, column=0)


    # If the user search can't be found
    except:

        # Display label will show the user the cant find variable
        cant_find = "Sorry I couldn't find that"
        print(cant_find)
        display = Label(root, text=cant_find)
        display.grid(row=1, column=1)

        # Clear button gains the clear_text() command
        Clear = Button(text='Clear', command=lambda: clear_text())
        Clear.grid(row=1, column=0)


# The search box where the user can input the packages they are looking for
SearchBox = Entry(root)
SearchBox.grid(row=0, column=1)

# Enter button
Enter = Button(root, text='Enter', command=lambda: SearchIt())
Enter.grid(row=0, column=0)

# Run loop
root.mainloop()
