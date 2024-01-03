from odoo import models, fields, api, exceptions


class Property(models.Model):
    _name = "estate.property"
    _description = "The Real Estate Advertisement module."

    name = fields.Char("Title", required=True, translate=True)
    property_type_id = fields.Many2one('estate.property.type', string='Property Type')
    tag_ids = fields.Many2many("estate.property.tag", string="Tags")
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
    buyer_id = fields.Many2one('res.partner', string='Buyer')
    offer_ids = fields.One2many(
        'estate.property.offer',
        'property_id',
        string='Offers',
    )
    best_offer = fields.Float("Best Offer", compute="_compute_best_offer", store=True)
    total_area = fields.Integer("Total Area (sqm)", compute="_compute_total_area")
    state = fields.Selection(
        string='Status',
        selection=[('new', 'New'), ('canceled', 'Canceled'), ('sold', 'Sold')],
        default='new',
        readonly=True,
    )

    @api.depends('living_area', 'garden_area')
    def _compute_total_area(self):
        for property_record in self:
            property_record.total_area = property_record.living_area + property_record.garden_area

    @api.depends("offer_ids.price")
    def _compute_best_offer(self):
        for property_record in self:
            property_record.best_offer = sum(property_record.offer_ids.mapped("price"))

    
    @api.onchange("garden")
    def _ochange_garden(self):
        if self.garden:
            self.garden_area = 10
            self.garden_orientation = "north"
        else:
            self.garden_area = False
            self.garden_orientation = False


    def button_cancel(self):
        for record in self:
            if record.state == 'sold':
                raise exceptions.UserError("A sold property cannot be calceled.")
            record.write({'state': 'canceled'})


    def button_sold(self):
        for record in self:
            if record.state == 'canceled':
                raise exceptions.UserError("A canceled property cannot be sold.")
            record.write({'state': 'sold'})
