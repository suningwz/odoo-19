from odoo import models, fields


class Attachment(models.Model):
    _inherit = 'ir.attachment'
    _name = 'dlg_crm.attachment'
    _description = 'Adjuntos'

    action_id = fields.Integer(string="ID acción", readonly=True)
