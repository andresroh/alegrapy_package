# AlegraPy

Este paquete nos permite consumir el API del la plataforma de facturacion Alegra mediante python 🐍

## Características

- Permite leer facturas, pagos, productos, contactos
- Permite crear facturas, pagos, productos, contactos
- Permite borrar facturas, pagos, productos, contactos

## Instalación

En construcción...

## Uso

```py
from alegra import invoices,contacts, session

session.user = "your_email@domnain.com"
session.token = "your_token"

invoice = invoices()
invoice.read(1,fields='pdf')
invoice.list(0,3)

contact = contacts()
contact.read(12)
contact.list(0,2)
```

## Créditos

Camilo Andrés Rodriguez

## Licencia

Este proyecto está bajo la Licencia [MIT].

---

¡Puedes personalizarlo según las necesidades específicas de tu proyecto!

