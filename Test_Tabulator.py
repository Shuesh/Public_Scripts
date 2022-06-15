import requests
import bs4 as Soup
from tkinter import *
from functools import partial
import xlsxwriter as xl


def main():
    login_url = r'https://hardwareticketsystem.starkey.com/login'
    ticket_url = r'https://hardwareticketsystem.starkey.com/rf-design/ticket-editor/'
    api_url = r'https://wtedev.ms.starkey.com/api'

    # Check wifi connection


    # Ask for credentials and ticket number
    get_ticket()


    # GET from ticket API
    # print(ticket.get())
    # print(ticket_url + ticket.get())
    # session = requests.Session()
    # response = session.get(ticket_url + ticket.get())
    # print(response)

    # Loop through requests


    # Check if request is "Open"


    #Log by SN


    # Tabulate in CSV/Excel

def check_wifi():
    pass


def get_ticket():
    #window
    tk_login = Tk()  
    tk_login.geometry('250x150')  
    tk_login.title('Ticket Tabulator')
    Label(tk_login, text="Enter ticket number(s)").pack()
    Label(tk_login, text="").pack()

    global ticket
    ticket = StringVar()

    # Ticket #
    Label(tk_login, text="Ticket Number:").pack()
    ticket_login_entry = Entry(tk_login, textvariable=ticket)
    ticket_login_entry.pack()
    Label(tk_login, text="").pack()

    #Login Button
                                                                                            #This produces an error (tk_login)
    Button(tk_login, text="Login", width=10, height=1, command=lambda: (tk_login.destroy(), tk_login)[ticket.get()]).pack()
    tk_login.mainloop()



def tabulate():
    pass




if __name__ == '__main__':
    main()