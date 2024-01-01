from odoo import models, fields

class Property(models.Model):
    _name = "estate.property"
    _description = "The Real Estate Advertisement module."

    name = fields.Char("Title", required=True, translate=True)
    property_type_id = fields.Many2one('estate.property.type', string='Property Type')
    description = fields.Text("Description", )
    postcode = fields.Char("Postcode")
    date_availability = fields.Date("Available From")
    expected_price = fields.Float("Expected Price", required=True)
    selling_price = fields.Float("Selling Price")
    bedrooms = fields.Integer("Bedrooms")
    living_area = fields.Integer("Living Area (sqm)")
    facades = fields.Integer("Facades")
    garage = fields.Boolean("Garage")
    garden = fields.Boolean("Garden")
    garden_area = fields.Integer("Garden Area (sqm)")
    garden_orientation = fields.Selection(
        string='Type',
        selection=[('north', 'North'), ('south', 'South'), ('east', 'East'), ('west', 'West')],
        help="Type is used to separate Leads and Opportunities")
    salesman_id = fields.Many2one('res.users', string='Salesman', index=True, default=lambda self: self.env.user)
    buyer_id = fields.Many2one('res.users', string='Buyer')
