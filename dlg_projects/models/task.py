# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Task(models.Model):
    _name = 'dlg_projects.task'
    _description = 'Tareas'

    project = fields.Text(string='Proyecto', readonly=True)
    project_id = fields.Integer(string="ID proyecto", readonly=True)
    id = fields.Integer()
    name = fields.Char(string='Descripción')
    notes = fields.Text(string='Notas')
    date = fields.Date(string='Fecha creación')
    date_end = fields.Date(string='Fecha fin')
    type = fields.Selection([('C', 'Call'), ('R', 'Reunión'), ('L', 'Llamada'),
                             ('D', 'Comida'), ('E', 'email')], string='Tipo', required=False)
    done = fields.Boolean(string='Finalizada')
    phase = fields.Many2one('dlg_projects.phase', string="Fase", required=False)
    file = fields.Binary("Attachment")
    file_name = fields.Char("File Name")
    url_field = fields.Char("Archivo")
    user = fields.Char("Usuario", default=lambda self: self.env.user.name)
    #user = fields.Many2one('res.users', 'Current User', default=lambda self: self.env.user)
    color = fields.Integer()

    _order = 'date_end desc'

    def toggle_state(self):
        self.done = not self.done

    # ORM
    @staticmethod
    def f_create_task(self):
        return {
            'view_type': 'form',
            'view_mode': 'form',
            'res_model': 'dlg_projects.task',
            'view_id': self.env.ref("dlg_projects.view_dlg_projects_task_form").id,
            'type': 'ir.actions.act_window',
            'context': {},
        }

    def f_search_update(self):
        task = self.env['dlg_projects.task'].search([('name', '=', 'ORM test')])
        print('search()', task, task.name)

        task_b = self.env['dlg_projects.task'].browse([8])
        print('browse()', task_b, task_b.name)

        task.write({
            'name': 'ORM test write'
        })

    def f_delete(self):
        task = self.env['dlg_projects.task'].browse([8])
        task.unlink()


class TaskReport(models.AbstractModel):
    _name = 'report.dlg_projects.report_task_card'

    @api.model
    def _get_report_values(self, docids, data=None):
        report_obj = self.env['ir.tasks.report']
        report = report_obj._get_report_from_name('dlg_projects.report_task_card')
        return {
            'doc_ids': docids,
            'doc_model': self.env['dlg_projects.task'],
            'docs': self.env['dlg_projects.task'].browse(docids)
        }
