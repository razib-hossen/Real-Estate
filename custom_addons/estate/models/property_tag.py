from odoo import models, fields


class PropertyTag(models.Model):
    _name = "estate.property.tag"
    _description = "The Property Tag Model"

    name = fields.Char("Name", required=True)
