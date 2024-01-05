from odoo import models, fields


class PropertyTag(models.Model):
    _name = "estate.property.tag"
    _description = "The Property Tag Model"

    name = fields.Char("Name", required=True)

    _sql_constraints = [
        ('unique_name', 'unique(name)', 'The tag name already created'),
    ]
