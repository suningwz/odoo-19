# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Phase(models.Model):
    _name = 'dlg_crm.phase'
    _description = 'Fase'

    id = fields.Integer(string='ID')
    name = fields.Char(string='Nombre')
    total_volume = fields.Integer(string='Total €/año')
    total_orders = fields.Integer(string='Total pedidos/año')

    # ORM
    def f_create(self):
        phase = {
            'id': 'ORM test',
            'name': 'ORM test'
        }
        print(phase)
        self.env['dlg_crm.phase'].create(phase)

    def f_search_update(self):
        phase = self.env['dlg_crm.phase'].search([('name', '=', 'ORM test')])
        print('search()', phase, phase.name)

        phase_b = self.env['dlg_crm.phase'].browse([8])
        print('browse()', phase_b, phase_b.name)

        phase.write({
            'name': 'ORM test write'
        })

    def f_delete(self):
        phase = self.env['dlg_crm.phase'].browse([8])
        phase.unlink()


class PhaseReport(models.AbstractModel):
    _name = 'report.dlg_crm.report_phase_card'

    @api.model
    def _get_report_values(self, docids, data=None):
        report_obj = self.env['ir.actions.report']
        report = report_obj._get_report_from_name('dlg_crm.report_phase_card')
        return {
            'doc_ids': docids,
            'doc_model': self.env['dlg_crm.phase'],
            'docs': self.env['dlg_crm.phase'].browse(docids)
        }
