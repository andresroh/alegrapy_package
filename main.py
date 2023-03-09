from alegra.invoices import invoices
from alegra.contacts import contacts
from alegra.session import session

# this module contains login info,delete it and use you information
from keys import user, token 

if __name__ == '__main__':

    session.user = user # use your_email@domnain.com
    session.token = token # use you token

    invoice = invoices()
    invoice.read(1)

    contact = contacts()
    contact.read(12)
