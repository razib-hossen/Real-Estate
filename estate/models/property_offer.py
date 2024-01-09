from odoo import models, fields, api
from datetime import timedelta


class PropertyOffer(models.Model):
    _name = "estate.property.offer"
    _description = "The Property Offer Model"
    _order = "price desc"

    price = fields.Float("Price")
    status = fields.Selection(
        string="Status",
        selection=[('refused', "Refused"), ('accepted', "Accepted")],
        help="Please select an option")
    partner_id = fields.Many2one("res.partner", string="Partner")
    property_id = fields.Many2one("estate.property", required=True)
    validity = fields.Integer("Validity (days)", compute='_compute_validity', inverse='_inverse_validity', store=True)
    deadline = fields.Date("Deadline", compute='_compute_deadline', inverse='_inverse_deadline', store=True)

    @api.depends('validity')
    def _compute_deadline(self):
        for offer in self:
            if offer.validity:
                offer.deadline = fields.Date.today() + timedelta(days=offer.validity)

    @api.onchange('deadline')
    def _inverse_deadline(self):
        for offer in self:
            if offer.deadline:
                offer.validity = (offer.deadline - fields.Date.today()).days

    @api.depends('deadline')
    def _compute_validity(self):
        for offer in self:
            if offer.deadline:
                offer.validity = (offer.deadline - fields.Date.today()).days

    @api.onchange('validity')
    def _inverse_validity(self):
        for offer in self:
            if offer.validity:
                offer.deadline = fields.Date.today() + timedelta(days=offer.validity)

    is_offer_accepted = fields.Boolean(compute="_is_offer_accepted")
    
    @api.depends('property_id.state')
    def _is_offer_accepted(self):
        for record in self:
            record.is_offer_accepted = record.property_id.state == 'offer_accepted'
    
    def action_accepted(self):
        for offer in self:
            offer.write({'status': 'accepted'})
            offer.property_id.selling_price = offer.property_id.best_offer
            offer.property_id.buyer_id = offer.partner_id
            offer.property_id.write({'state': 'offer_accepted'})

    def action_refused(self):
        for offer in self:
            offer.write({'status': 'refused'})
