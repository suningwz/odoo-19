from odoo import models, fields


class Attachment(models.Model):
    _inherit = 'ir.attachment'

    attach_rel = fields.Many2many('dlg_crm.action', 'attachment', 'attachment_id3', 'document_id',
                                  string="Adjunto", invisible=1)
