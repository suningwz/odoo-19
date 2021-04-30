# -*- coding: utf-8 -*-

from odoo import models, fields, api
import datetime

PRIORITIES = [
    ('0', 'Baja'),
    ('1', 'Media'),
    ('2', 'Alta'),
    ('3', 'Muy Alta'),
]


class Task(models.Model):
    _name = 'dlg_tasks.task'
    _description = 'Tareas'

    id = fields.Integer(string='ID')
    name = fields.Char(string='Descripción')
    notes = fields.Text(string='Notas')
    date = fields.Date(string='Fecha creación')
    done = fields.Boolean(string='Realizada', readonly=True)
    image = fields.Binary(string='Imagen')
    phase = fields.Many2one('dlg_tasks.phase', string="Fase", required=True)
    color = fields.Integer()
    header = fields.Char('Cabecera')
    priority = fields.Selection(PRIORITIES, string='Prioridad', index=True, default=PRIORITIES[0][0])
    show = fields.Boolean('No Mostrar')
    actions = fields.One2many('dlg_tasks.action', 'task_id', string='Actions', copy=True, auto_join=True)
    user = fields.Char("Usuario", default=lambda self: self.env.user.name, readonly=True)
    user_assigned = fields.Many2one('res.users', sring="Asignado a")

    _order = 'header asc, priority desc'

    def toggle_state(self):
        self.done = not self.done

    # ORM
    def f_create(self):
        task = {
            'date': datetime.date.today(),
            'name': 'ORM test',
            'notes': 'ORM test',
            'done': False,
            'color': 0,
            'header': '',
            'priority': '1'
        }
        print(task)
        self.env['dlg_tasks.task'].create(task)

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

    def f_update_action(self):
        action = self.env['dlg_tasks.action'].browse([8])
        print('browse()', action, action.name)

    def f_search_update(self):
        task = self.env['dlg_tasks.task'].search([('name', '=', 'ORM test')])
        print('search()', task, task.name)

        task_b = self.env['dlg_tasks.task'].browse([8])
        print('browse()', task_b, task_b.name)

        task.write({
            'name': 'ORM test write'
        })

    def f_delete(self):
        task = self.env['dlg_tasks.task'].browse([8])
        task.unlink()


class TaskReport(models.AbstractModel):
    _name = 'report.dlg_tasks.report_task_card'

    @api.model
    def _get_report_values(self, docids, data=None):
        report_obj = self.env['ir.actions.report']
        report = report_obj._get_report_from_name('dlg_tasks.report_task_card')
        return {
            'doc_ids': docids,
            'doc_model': self.env['dlg_tasks.task'],
            'docs': self.env['dlg_tasks.task'].browse(docids)
        }
