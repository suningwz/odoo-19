# -*- coding: utf-8 -*-

from odoo import models, fields, api
import datetime


PRIORITIES = [
    ('0', 'Baja'),
    ('1', 'Media'),
    ('2', 'Alta'),
    ('3', 'Muy Alta'),
]

class Action(models.Model):
    _name = 'dlg_tasks.action'
    _description = 'Acciones'

    task = fields.Text(string='Tarea', readonly=True)
    task_id = fields.Integer(string="ID tarea", readonly=True)
    id = fields.Integer()
    name = fields.Char(string='Descripción')
    notes = fields.Text(string='Notas')
    date = fields.Date(string='Fecha creación')
    date_event = fields.Date(string='Fecha evento')
    date_end = fields.Date(string='Fecha fin')
    done = fields.Boolean(string='Finalizada')
    image = fields.Binary(string='Imagen')
    phase = fields.Many2one('dlg_tasks.phase', string="Fase", required=False)
    user = fields.Char("Creador", default=lambda self: self.env.user.name, readonly=True)
    user_assigned = fields.Many2one('res.users', sring="Asignado a")
    color = fields.Integer()
    priority = fields.Selection(PRIORITIES, string='Prioridad', index=True, default=PRIORITIES[0][0])
    show = fields.Boolean('No Mostrar')
    header = fields.Char('Cabecera')

    _order = 'header asc, priority desc, date_event desc'

    def toggle_state(self):
        self.done = not self.done

    # ORM
    @staticmethod
    def f_create_action(self):
        return {
            'view_type': 'form',
            'view_mode': 'form',
            'res_model': 'dlg_tasks.action',
            'view_id': self.env.ref("dlg_tasks.view_dlg_tasks_action_form").id,
            'type': 'ir.actions.act_window',
            'context': {},
        }

    def f_search_update(self):
        action = self.env['dlg_tasks.action'].search([('name', '=', 'ORM test')])
        print('search()', action, action.name)

        action_b = self.env['dlg_tasks.action'].browse([8])
        print('browse()', action_b, action_b.name)

        action.write({
            'name': 'ORM test write'
        })

    def f_delete(self):
        action = self.env['dlg_tasks.action'].browse([8])
        action.unlink()


class ActionReport(models.AbstractModel):
    _name = 'report.dlg_tasks.report_action_card'

    @api.model
    def _get_report_values(self, docids, data=None):
        report_obj = self.env['ir.actions.report']
        report = report_obj._get_report_from_name('dlg_tasks.report_action_card')
        return {
            'doc_ids': docids,
            'doc_model': self.env['dlg_tasks.action'],
            'docs': self.env['dlg_tasks.action'].browse(docids)
        }
