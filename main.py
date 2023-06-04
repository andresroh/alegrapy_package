from alegra import invoices, contacts, session
from decouple import config

if __name__ == '__main__':

    session.user = config("ALEGRA_USER")  # use your_email@domnain.com
    session.token = config("TOKEN")  # use you token

    invoice = invoices()
    invoice.read(1, fields='pdf')
    invoice.list(0, 3)

    contact = contacts()
    contact.read(5000)
    contact.list(0, 2)
