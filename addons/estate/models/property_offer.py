from odoo import models, fields, api, exceptions
from datetime import timedelta
import logging

logging.basicConfig(level=logging.DEBUG)

class PropertyOffer(models.Model):
    _name = "estate.property.offer"
    _description = "The Property Offer Model"
    _order = "price"

    price = fields.Float("Price")
    status = fields.Selection(
        string="Status",
        selection=[('refused', "Refused"), ('accepted', "Accepted")],
        help="Please select an option")
    partner_id = fields.Many2one("res.partner", string="Partner")
    property_id = fields.Many2one("estate.property", required=True, ondelete="cascade")
    validity = fields.Integer("Validity (days)", compute='_compute_validity', inverse='_inverse_validity', store=True)
    deadline = fields.Date("Deadline", compute='_compute_deadline', inverse='_inverse_deadline', store=True)
    property_type_id = fields.Many2one(
        "estate.property.type",
        string="Property Type",
        related="property_id.property_type_id",
        store=True,
    )

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
            record.is_offer_accepted = (
                record.property_id.state == 'offer_accepted'\
                    or record.property_id.state == 'canceled'\
                        or record.property_id.state == 'sold'
                )
    
    @api.model_create_multi
    def create(self, values_list):
        for values in values_list:
            # Check if there are existing offers with a higher price
            existing_offers = self.search([
                ('property_id', '=', values.get('property_id')),
            ])

            if existing_offers:
                existing_min_price = min(existing_offers.mapped('price'))
                if existing_min_price > values.get('price'):
                    raise exceptions.UserError("Cannot create offer with a lower price than existing offers.")

        new_offers = super(PropertyOffer, self).create(values_list)

        for new_offer in new_offers:
            record = new_offer.property_id
            record.write({'state': 'offer_received'})

        return new_offers


    def action_accepted(self):
        for offer in self:
            offer.write({'status': 'accepted'})
            offer.property_id.selling_price = offer.property_id.best_offer
            offer.property_id.buyer_id = offer.partner_id
            offer.property_id.write({'state': 'offer_accepted'})

    def action_refused(self):
        for offer in self:
            offer.write({'status': 'refused'})

