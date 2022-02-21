from odoo import fields, models, api


class Plants(models.Model):
    _name = 'nursery.plant'
    _description = 'Nursery Plant'

    name = fields.Char("Plant Name")
    price = fields.Float()

    class Customer(models.Model):

        _name = 'nursery.customer'

        name = fields.Char("Customer Names", required=True)
        email = fields.char(help="To recieve newsletters")
