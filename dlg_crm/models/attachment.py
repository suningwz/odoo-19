from odoo import models, fields


class Attachment(models.Model):
    _inherit = 'ir.attachment'

    action_id = fields.Integer(string="ID acción", readonly=True)
