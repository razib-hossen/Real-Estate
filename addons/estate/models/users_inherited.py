from odoo import models, fields

class ResUsers(models.Model):
    _inherit = "res.users"

    property_ids = fields.One2many(
        'estate.property',
        'salesman_id',
        string='Properties',
        domain="[('salesman_id', '=', id)]",
    )
