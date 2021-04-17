# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import Response
import json


class OpportunityController(http.Controller):

    @http.route('/api/opportunity', auth='public', method=['GET'], csrf=False)
    def get_opportunity(self, **kw):
        try:
            opportunity = http.request.env['dlg_crm.opportunity'].sudo().search_read([], ['id', 'name', 'customer',
                                                                                          'notes', 'image',
                                                                                          'phase', 'done', 'header',
                                                                                          'priority',
                                                                                          'show', 'orders_year',
                                                                                          'volume_year',
                                                                                          'actions', 'user'])
            res = json.dumps(opportunity, ensure_ascii=False).encode('utf-8')
            return Response(res, content_type='application/json;charset=utf-8', status=200)
        except Exception as e:
            return Response(json.dumps({'error': str(e)}), content_type='application/json;charset=utf-8', status=505)


class PhaseController(http.Controller):

    @http.route('/api/phase', auth='public', method=['GET'], csrf=False)
    def get_phase(self, **kw):
        try:
            phase = http.request.env['dlg_crm.phase'].sudo().search_read([], ['id', 'name', 'total_orders',
                                                                              'total_volume'])
            res = json.dumps(phase, ensure_ascii=False).encode('utf-8')
            return Response(res, content_type='application/json;charset=utf-8', status=200)
        except Exception as e:
            return Response(json.dumps({'error': str(e)}), content_type='application/json;charset=utf-8', status=505)


class ActionController(http.Controller):

    @http.route('/api/action', auth='public', method=['GET'], csrf=False)
    def get_phase(self, **kw):
        try:
            action = http.request.env['dlg_crm.action'].sudo().search_read([], ['opportunity',
                                                                                'id',
                                                                                'name',
                                                                                'notes',
                                                                                'customer',
                                                                                'date',
                                                                                'date_event',
                                                                                'date_end',
                                                                                'type',
                                                                                'done',
                                                                                'image',
                                                                                'opportunity_id',
                                                                                'phase',
                                                                                'color', 'user'])
            res = json.dumps(action, ensure_ascii=False).encode('utf-8')
            return Response(res, content_type='application/json;charset=utf-8', status=200)
        except Exception as e:
            return Response(json.dumps({'error': str(e)}), content_type='application/json;charset=utf-8', status=505)
