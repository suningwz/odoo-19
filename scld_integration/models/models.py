# -*- coding: utf-8 -*-

from odoo import models, fields, api
import datetime


class Parcel(models.Model):
    _name = 'scld_integration.parcel'
    _description = 'Parcel'

    name = fields.Char(string='Descripción')
    customer = fields.Many2one(string='Cliente', comodel_name='res.partner')
    date = fields.Datetime(string='Fecha')
    type = fields.Selection([('P', 'Presencial'), ('W', 'WhatsApp'), ('T', 'Telefónico')], string='Tipo', required=True)
    done = fields.Boolean(string='Realizada', readonly=True)
    image = fields.Binary(string='Imagen')

    def toggle_state(self):
        self.done = not self.done

    # ORM
    def f_create(self):
        parcel = {
            'name': 'ORM test',
            'customer': 1,
            'date': str(datetime.date(2020, 8, 6)),
            'type': 'P',
            'done': False
        }
        print(parcel)
        self.env['scld_integration.parcel'].create(parcel)

    def f_search_update(self):
        parcel = self.env['scld_integration.parcel'].search([('name', '=', 'ORM test')])
        print('search()', parcel, parcel.name)

        parcel_b = self.env['scld_integration.parcel'].browse([8])
        print('browse()', parcel_b, parcel_b.name)

        parcel.write({
            'name': 'ORM test write'
        })

    def f_delete(self):
        parcel = self.env['scld_integration.parcel'].browse([8])
        parcel.unlink()
