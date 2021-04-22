# -*- coding: utf-8 -*-

from odoo import models, fields, api
import datetime


class Action(models.Model):
    _name = 'dlg_crm.action'
    _description = 'Acciones'

    opportunity = fields.Text(string='Oportunidad', readonly=True)
    opportunity_id = fields.Integer(string="ID oportunidad", readonly=True)
    id = fields.Integer()
    name = fields.Char(string='Descripción')
    notes = fields.Text(string='Notas')
    customer = fields.Many2one(string='Cliente', comodel_name='res.partner', readonly=True)
    date = fields.Date(string='Fecha creación')
    date_event = fields.Date(string='Fecha evento')
    date_end = fields.Date(string='Fecha fin')
    type = fields.Selection([('C', 'Call'), ('R', 'Reunión'), ('L', 'Llamada'),
                             ('D', 'Comida'), ('E', 'email')], string='Tipo', required=False)
    done = fields.Boolean(string='Finalizada')
    image = fields.Binary(string='Imagen')
    phase = fields.Many2one('dlg_crm.phase', string="Fase", required=False)
    user = fields.Char("Usuario", default=lambda self: self.env.user.name)
    #user = fields.Many2one('res.users', 'Current User', default=lambda self: self.env.user)
    color = fields.Integer()
    attachments = fields.One2many('ir.attachment', 'res_id', string='Attachments', copy=True, auto_join=True)

    _order = 'date_event desc'

    def toggle_state(self):
        self.done = not self.done

    # ORM
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

    def f_search_update(self):
        action = self.env['dlg_crm.action'].search([('name', '=', 'ORM test')])
        print('search()', action, action.name)

        action_b = self.env['dlg_crm.action'].browse([8])
        print('browse()', action_b, action_b.name)

        action.write({
            'name': 'ORM test write'
        })

    def f_delete(self):
        action = self.env['dlg_crm.action'].browse([8])
        action.unlink()


class ActionReport(models.AbstractModel):
    _name = 'report.dlg_crm.report_action_card'

    @api.model
    def _get_report_values(self, docids, data=None):
        report_obj = self.env['ir.actions.report']
        report = report_obj._get_report_from_name('dlg_crm.report_action_card')
        return {
            'doc_ids': docids,
            'doc_model': self.env['dlg_crm.action'],
            'docs': self.env['dlg_crm.action'].browse(docids)
        }
