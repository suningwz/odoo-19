# -*- coding: utf-8 -*-

from odoo import models, fields, api
import datetime

PRIORITIES = [
    ('0', 'Baja'),
    ('1', 'Media'),
    ('2', 'Alta'),
    ('3', 'Muy Alta'),
]


class Opportunity(models.Model):
    _name = 'dlg_crm.opportunity'
    _description = 'Oportunidades'

    id = fields.Integer(string='ID')
    name = fields.Char(string='Descripción')
    notes = fields.Text(string='Notas')
    customer = fields.Many2one(string='Cliente', comodel_name='res.partner')
    date = fields.Date(string='Fecha creación')
    done = fields.Boolean(string='Realizada', readonly=True)
    image = fields.Binary(string='Imagen')
    phase = fields.Many2one('dlg_crm.phase', string="Fase", required=True)
    color = fields.Integer()
    header = fields.Char('Cabecera')
    priority = fields.Selection(PRIORITIES, string='Prioridad', index=True, default=PRIORITIES[0][0])
    volume_year = fields.Integer(String='€/año (estimación)')
    orders_year = fields.Integer(String='Pedidos/año (estimación)')
    show = fields.Boolean('No Mostrar')
    actions = fields.One2many('dlg_crm.action', 'opportunity_id', string='Actions', copy=True, auto_join=True)
    user = fields.Char("Usuario", default=lambda self: self.env.user.name)
    #user = fields.Many2one('res.users', 'Current User', default=lambda self: self.env.user)

    _order = 'header asc, priority desc'

    def toggle_state(self):
        self.done = not self.done

    # ORM
    def f_create(self):
        opportunity = {
            'date': datetime.date.today(),
            'name': 'ORM test',
            'notes': 'ORM test',
            'done': False,
            'color': 0,
            'header': '',
            'priority': '1'
        }
        print(opportunity)
        self.env['dlg_crm.opportunity'].create(opportunity)

    @staticmethod
    def f_create_action(self):
        return {
            'view_type': 'form',
            'view_mode': 'form',
            'res_model': 'dlg_crm.action',
            'view_id': self.env.ref("dlg_crm.view_dlg_crm_action_form").id,
            'type': 'ir.actions.act_window',
            'context': {},
        }

    def f_update_action(self):
        action = self.env['dlg_crm.action'].browse([8])
        print('browse()', action, action.name)

    def f_search_update(self):
        opportunity = self.env['dlg_crm.opportunity'].search([('name', '=', 'ORM test')])
        print('search()', opportunity, opportunity.name)

        opportunity_b = self.env['dlg_crm.opportunity'].browse([8])
        print('browse()', opportunity_b, opportunity_b.name)

        opportunity.write({
            'name': 'ORM test write'
        })

    def f_delete(self):
        opportunity = self.env['dlg_crm.opportunity'].browse([8])
        opportunity.unlink()


class OpportunityReport(models.AbstractModel):
    _name = 'report.dlg_crm.report_opportunity_card'

    @api.model
    def _get_report_values(self, docids, data=None):
        report_obj = self.env['ir.actions.report']
        report = report_obj._get_report_from_name('dlg_crm.report_opportunity_card')
        return {
            'doc_ids': docids,
            'doc_model': self.env['dlg_crm.opportunity'],
            'docs': self.env['dlg_crm.opportunity'].browse(docids)
        }
