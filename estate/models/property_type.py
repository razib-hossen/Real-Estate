from odoo import models, fields, api


class PropertyType(models.Model):
    _name = "estate.property.type"
    _description = "The Property Type Model"
    _order = "sequence, name"

    name = fields.Char("Name", required=True)

    property_ids = fields.One2many(
        'estate.property', 'property_type_id', string="Properties"
    )
    offer_ids = fields.One2many(
        "estate.property.offer",
        "property_type_id",
        string="Offers"
    )
    offer_count = fields.Integer(
        string="Number of Offers",
        compute="_compute_offer_count",
        store=True,
    )

    sequence = fields.Integer('Sequence', default=1, help="Used to order stages. Lower is better.")

    _sql_constraints = [
        ('unique_name', 'unique(name)', 'The name already created'),
    ]


    @api.depends("offer_ids")
    def _compute_offer_count(self):
        for record in self:
            record.offer_count = len(record.offer_ids)
    
    def action_view_property_type_offers(self):
        action = self.env.ref("estate.action_estate_property_offer_tree").read()[0]
        action['domain'] = [('property_type_id', '=', self.id)]
        return action
