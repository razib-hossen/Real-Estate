from odoo import models, api


class EstateProperty(models.Model):
    _inherit = "estate.property"


    def action_sold(self):
        for record in self:
            
            if record.state == 'sold':
                return

            invoice_data = {
                'partner_id': record.buyer_id.id,
                'move_type': 'out_invoice',
                'journal_id': record.env['account.journal'].search([('type', '=', 'sale')], limit=1).id,
            }

            new_invoice = record.env['account.move'].create(invoice_data)

            line_data_1 = {
                'name': '6% of selling price',
                'quantity': 1,
                'price_unit': 0.06 * record.best_offer,
            }

            line_data_2 = {
                'name': 'Administrative Fees',
                'quantity': 1,
                'price_unit': 100.00,
            }

            new_invoice.write({'invoice_line_ids': [(0, 0, line_data_1), (0, 0, line_data_2)]})

            import pdb; pdb.set_trace()

            result = super(EstateProperty, record).action_sold()

        return result
