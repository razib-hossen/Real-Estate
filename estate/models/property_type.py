from odoo import models, fields


class PropertyType(models.Model):
    _name = "estate.property.type"
    _description = "The Property Type Model"
    _order = "sequence, name"

    name = fields.Char("Name", required=True)

    property_ids = fields.One2many(
        'estate.property', 'property_type_id', string="Properties"
    )
    sequence = fields.Integer('Sequence', default=1, help="Used to order stages. Lower is better.")

    _sql_constraints = [
        ('unique_name', 'unique(name)', 'The name already created'),
    ]

