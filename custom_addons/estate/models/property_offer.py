from odoo import models, fields


class PropertyOffer(models.Model):
    _name = "estate.property.offer"
    _description = "The Property Offer Model"

    price = fields.Float("Price")
    status = fields.Selection(
        string="Status",
        selection=[('refused', "Refused"), ('accepted', "Accepted")],
        help="Please select an option")
    partner_id = fields.Many2one("res.partner", string="Partner")
    property_id = fields.Many2one("estate.property", required=True)
    
