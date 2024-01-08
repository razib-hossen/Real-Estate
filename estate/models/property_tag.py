from random import randint
from odoo import models, fields


class PropertyTag(models.Model):
    _name = "estate.property.tag"
    _description = "Property Tag"
    _order = "sequence"

    def _default_color(self):
        return randint(1, 11)

    name = fields.Char("Name", required=True)
    sequence = fields.Integer('Sequence', default=0)
    property_id = fields.Many2one("estate.property", string="Property", ondelete='cascade')
    color = fields.Integer(
        string='Color Index', default=lambda self: self._default_color(),
        help='Tag color. No color means no display in kanban or front-end, to distinguish internal tags from public categorization tags.')

    _sql_constraints = [
        ('unique_name', 'unique(name)', 'The tag name already created'),
    ]
