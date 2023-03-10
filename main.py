from alegra import invoices,contacts, session

# this module contains login info, delete it and use you information
from keys import user, token 

if __name__ == '__main__':

    session.user = user # use your_email@domnain.com
    session.token = token # use you token

    invoice = invoices()
    invoice.read(1,fields='pdf')
    invoice.list(0,3)

    contact = contacts()
    contact.read(5000)
    contact.list(0,2)
