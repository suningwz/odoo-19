from odoo import models, fields


class Attachment(models.Model):
    _name = 'dlg_crm.attachment'
    _inherit = 'ir.attachment'
    _description = 'Adjuntos'

    action_id = fields.Many2one('dlg_crm.action', 'attachments', string="Adjunto")
