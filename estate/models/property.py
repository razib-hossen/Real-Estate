from odoo import models, fields, api, exceptions
from odoo.tools.float_utils import float_compare, float_is_zero


class Property(models.Model):
    _name = "estate.property"
    _description = "The Real Estate Advertisement module."
    _order = "id desc"

    name = fields.Char("Title", required=True, translate=True)
    property_type_id = fields.Many2one('estate.property.type', string='Property Type')
    tag_ids = fields.One2many('estate.property.tag', 'property_id', string="Tags")
    description = fields.Text("Description", )
    postcode = fields.Char("Postcode")
    date_availability = fields.Date("Available From")
    expected_price = fields.Float("Expected Price", required=True)
    selling_price = fields.Float("Selling Price", required=True)
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
        selection=[('new', 'New'), ('offer_received', 'Offer Received'), ('offer_accepted', 'Offer Accepted'), ('canceled', 'Canceled'), ('sold', 'Sold')],
        default='new',
        readonly=True,
    )


    _sql_constraints = [
        ('positive_expected_price', 'CHECK(expected_price > 0)', 'Expected price must be strictly positive.'),
        ('positive_selling_price', 'CHECK(selling_price > 0)', 'Selling price must be strictly positive.'),
    ]
    

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
    

    @api.constrains('expected_price', 'selling_price')
    def _check_selling_price(self):
        for property_record in self:
            if float_is_zero(property_record.expected_price, precision_digits=2):
                # If expected price is zero, skip the check
                continue

            lower_limit = property_record.expected_price * 0.9
            if float_compare(property_record.selling_price, lower_limit, precision_digits=2) == -1:
                raise exceptions.ValidationError("Selling price cannot be lower than 90% of the expected price.")
    

    @api.constrains('best_offer')
    def _check_best_offer(self):
        for record in self:
            if record.best_offer <= 0:
                raise exceptions.ValidationError("Best offer price must be positive.")
        
