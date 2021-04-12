# -*- coding: utf-8 -*-

from odoo import models, fields, api
import datetime

PRIORITIES = [
    ('0', 'Baja'),
    ('1', 'Media'),
    ('2', 'Alta'),
    ('3', 'Muy Alta'),
]


class Project(models.Model):
    _name = 'dlg_projects.project'
    _description = 'Proyectos'

    id = fields.Integer(string='ID')
    name = fields.Char(string='Descripción')
    notes = fields.Text(string='Notas')
    date = fields.Date(string='Fecha creación')
    done = fields.Boolean(string='Realizada', readonly=True)
    phase = fields.Many2one('dlg_projects.phase', string="Fase", required=True)
    color = fields.Integer()
    header = fields.Char('Cabecera')
    priority = fields.Selection(PRIORITIES, string='Prioridad', index=True, default=PRIORITIES[0][0])
    show = fields.Boolean('No Mostrar')
    tasks = fields.One2many('dlg_projects.task', 'project_id', string='Tareas', copy=True, auto_join=True)
    user = fields.Char("Usuario", default=lambda self: self.env.user.name)
    #user = fields.Many2one('res.users', 'Current User', default=lambda self: self.env.user)

    _order = 'header asc, priority desc'

    def toggle_state(self):
        self.done = not self.done

    # ORM
    def f_create(self):
        project = {
            'date': datetime.date.today(),
            'name': 'ORM test',
            'notes': 'ORM test',
            'done': False,
            'color': 0,
            'header': '',
            'priority': '1'
        }
        print(project)
        self.env['dlg_projects.project'].create(project)

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

    def f_update_task(self):
        task = self.env['dlg_projects.task'].browse([8])
        print('browse()', task, task.name)

    def f_search_update(self):
        project = self.env['dlg_projects.project'].search([('name', '=', 'ORM test')])
        print('search()', project, project.name)

        project_b = self.env['dlg_projects.project'].browse([8])
        print('browse()', project_b, project_b.name)

        project.write({
            'name': 'ORM test write'
        })

    def f_delete(self):
        project = self.env['dlg_projects.project'].browse([8])
        project.unlink()


class ProjectReport(models.AbstractModel):
    _name = 'report.dlg_projects.report_project_card'

    @api.model
    def _get_report_values(self, docids, data=None):
        report_obj = self.env['ir.project.report']
        report = report_obj._get_report_from_name('dlg_projects.report_project_card')
        return {
            'doc_ids': docids,
            'doc_model': self.env['dlg_projects.project'],
            'docs': self.env['dlg_projects.project'].browse(docids)
        }
