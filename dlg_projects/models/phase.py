# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Phase(models.Model):
    _name = 'dlg_projects.phase'
    _description = 'Fase'

    id = fields.Integer(string='ID')
    name = fields.Char(string='Nombre')

    # ORM
    def f_create(self):
        phase = {
            'id': 'ORM test',
            'name': 'ORM test'
        }
        print(phase)
        self.env['dlg_projects.phase'].create(phase)

    def f_search_update(self):
        phase = self.env['dlg_projects.phase'].search([('name', '=', 'ORM test')])
        print('search()', phase, phase.name)

        phase_b = self.env['dlg_projects.phase'].browse([8])
        print('browse()', phase_b, phase_b.name)

        phase.write({
            'name': 'ORM test write'
        })

    def f_delete(self):
        phase = self.env['dlg_projects.phase'].browse([8])
        phase.unlink()


class PhaseReport(models.AbstractModel):
    _name = 'report.dlg_projects.report_phase_card'

    @api.model
    def _get_report_values(self, docids, data=None):
        report_obj = self.env['ir.phase.report']
        report = report_obj._get_report_from_name('dlg_projects.report_phase_card')
        return {
            'doc_ids': docids,
            'doc_model': self.env['dlg_projects.phase'],
            'docs': self.env['dlg_projects.phase'].browse(docids)
        }
