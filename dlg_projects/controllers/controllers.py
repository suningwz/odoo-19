# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import Response
import json


class ProjectController(http.Controller):

    @http.route('/api/project', auth='public', method=['GET'], csrf=False)
    def get_task(self, **kw):
        try:
            project = http.request.env['dlg_projects.project'].sudo().search_read([], ['id',
                                                                                       'name',
                                                                                       'notes',
                                                                                       'phase',
                                                                                       'done',
                                                                                       'header',
                                                                                       'priority',
                                                                                       'show',
                                                                                       'tasks',
                                                                                       'user'])
            res = json.dumps(project, ensure_ascii=False).encode('utf-8')
            return Response(res, content_type='application/json;charset=utf-8', status=200)
        except Exception as e:
            return Response(json.dumps({'error': str(e)}), content_type='application/json;charset=utf-8', status=505)


class PhaseController(http.Controller):

    @http.route('/api/phase', auth='public', method=['GET'], csrf=False)
    def get_phase(self, **kw):
        try:
            phase = http.request.env['dlg_projects.phase'].sudo().search_read([], ['id',
                                                                                   'name'])
            res = json.dumps(phase, ensure_ascii=False).encode('utf-8')
            return Response(res, content_type='application/json;charset=utf-8', status=200)
        except Exception as e:
            return Response(json.dumps({'error': str(e)}), content_type='application/json;charset=utf-8', status=505)


class TaskController(http.Controller):

    @http.route('/api/task', auth='public', method=['GET'], csrf=False)
    def get_phase(self, **kw):
        try:
            task = http.request.env['dlg_projects.task'].sudo().search_read([], ['project',
                                                                                 'id',
                                                                                 'name',
                                                                                 'notes',
                                                                                 'date',
                                                                                 'date_end',
                                                                                 'type',
                                                                                 'done',
                                                                                 'project_id',
                                                                                 'phase',
                                                                                 'file',
                                                                                 'file_name',
                                                                                 'color', 'user'])
            res = json.dumps(task, ensure_ascii=False).encode('utf-8')
            return Response(res, content_type='application/json;charset=utf-8', status=200)
        except Exception as e:
            return Response(json.dumps({'error': str(e)}), content_type='application/json;charset=utf-8', status=505)
