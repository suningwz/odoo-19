from odoo import models, fields


class Attachment(models.Model):
    _name = 'attachment'
    _inherit = 'ir.attachment'

    action_id = fields.Many2one('dlg_crm.action', 'attachments', string="Attachment", invisible=1)
