from odoo import models, fields


class Attachment(models.Model):
    _name = 'attachment'
    _inherit = 'ir.attachment'

    action_id = fields.Integer(string="ID acción", readonly=True)
