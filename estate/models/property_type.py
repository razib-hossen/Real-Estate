from odoo import models, fields, api, exceptions


class PropertyType(models.Model):
    _name = "estate.property.type"
    _description = "The Property Type Model"
    _order = "sequence, name"

    name = fields.Char("Name")

    property_ids = fields.One2many(
        'estate.property', 'property_type_id', string="Properties"
    )
    sequence = fields.Integer('Sequence', default=1, help="Used to order stages. Lower is better.")

    _sql_constraints = [
        ('unique_name', 'unique(name)', 'The name already created'),
    ]


    @api.constrains('name')
    def _check_name(self):
        for record in self:
            if not record.name:
                raise exceptions.ValidationError("This field is required.")
