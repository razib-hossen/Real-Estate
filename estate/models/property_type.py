from odoo import models, fields


class PropertyType(models.Model):
    _name = "estate.property.type"
    _description = "The Property Type Model"

    name = fields.Char("Name")

    _sql_constraints = [
        ('unique_name', 'unique(name)', 'The name already created'),
    ]
