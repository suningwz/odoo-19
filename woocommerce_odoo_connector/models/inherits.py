# -*- coding: utf-8 -*-
#################################################################################
#
#   Copyright (c) 2016-Present Webkul Software Pvt. Ltd. (<https://webkul.com/>)
#    See LICENSE file for full copyright and licensing details.
##########H#########Y#########P#########N#########O#########S###################

import logging

_logger = logging.getLogger(__name__)
from odoo import models, fields, api, _


class OrderFeed(models.Model):
    _inherit = "order.feed"

    def get_taxes_ids(self, line_taxes, channel_id):
        if channel_id.channel == "woocommerce":
            if line_taxes:
                tax_record = self.env['account.tax']
                tax_mapping_obj = self.env['channel.account.mappings']
                tax_list = []
                domain = []
                for tax in eval(line_taxes):
                    flag = 0
                    if "id" in tax:
                        domain = [('channel_id', '=', channel_id.id), ('store_id', '=', tax['id'])]
                        tax_rec = channel_id._match_mapping(tax_mapping_obj, domain)
                        if tax_rec:
                            tax_list.append(tax_rec.tax_name.id)
                            flag = 1
                    if 'rate' in tax:
                        if not tax['rate'] == 0.0 and not flag:
                            domain = []
                            name = ""
                            tax_type = "percent"
                            inclusive = False
                            if 'name' in tax:
                                name = tax['name']
                            else:
                                name = str(channel) + "_" + str(channel_id.id) + "_" + str(float(tax['rate']))
                            if 'include_in_price' in tax:
                                inclusive = tax['include_in_price']
                                # domain += [('include_in_price','=',tax['include_in_price'])]
                            if 'type' in tax:
                                tax_type = tax['type']
                                domain += [('tax_type', '=', tax['type'])]
                            domain += [('store_tax_value_id', '=', (tax['rate']))]
                            tax_rec = channel_id._match_mapping(tax_mapping_obj, domain)
                            tax_rate = float(tax['rate'])
                            if tax_rec:
                                # tax_rec.tax_name.price_include = inclusive
                                tax_list.append(tax_rec.tax_name.id)
                            else:
                                tax_dict = {
                                    'name': name,
                                    'amount_type': tax_type,
                                    'price_include': inclusive,
                                    'amount': tax_rate,
                                }
                                tax_id = tax_record.search([('name', '=', tax_dict['name'])])
                                if not tax_id:
                                    tax_id = tax_record.create(tax_dict)
                                    tax_map_vals = {
                                        'channel_id': channel_id.id,
                                        'tax_name': tax_id.id,
                                        'store_tax_value_id': str(tax_id.amount),
                                        'tax_type': tax_id.amount_type,
                                        'include_in_price': tax_id.price_include,
                                        'odoo_tax_id': tax_id.id,
                                    }
                                    channel_id._create_mapping(tax_mapping_obj, tax_map_vals)
                                tax_list.append(tax_id.id)
                return [(6, 0, tax_list)]
            return False
        else:
            return super(OrderFeed, self).get_taxes_ids(line_taxes, channel_id)
