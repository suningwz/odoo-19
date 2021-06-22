from odoo import models, fields, api

class ParcelReport(models.AbstractModel):

    _name='report.scld_integration.report_parcel_card'
    _description='Parcel report'

    @api.model
    def _get_report_values(self, docids, data=None):
        report_obj = self.env['ir.actions.report']
        report = report_obj._get_report_from_name('scld_integration.report_parcel_card')
        return {
            'doc_ids': docids,
            'doc_model': self.env['scld_integration.parcel'],
            'docs': self.env['scld_integration.parcel'].browse(docids)
        }