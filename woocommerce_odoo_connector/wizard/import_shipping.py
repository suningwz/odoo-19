import logging
_logger = logging.getLogger(__name__)
from odoo import models, fields, api
from odoo.exceptions import UserError

class ImportWoocommerceShipping(models.TransientModel):
    _name = "import.woocommerce.shipping"
    _inherit = "import.operation"
    _description = "Import Woocommerce Shipping"

    def import_now(self, **kwargs):
        data_list = []
        woocommerce = self._context.get("woocommerce")
        channel_id = self._context.get("channel_id")
        if kwargs.get("woocommerce_object_id"):
            vals = self.get_shipping_by_id(woocommerce, channel_id, **kwargs)
            data_list.append(vals)
        else:
            data_list = self.get_shipping_all(woocommerce, channel_id,**kwargs)
        return data_list

    def get_shipping_by_id(self,woocommerce,channel_id,**kwargs):
        shipping_data = woocommerce.get("shipping_methods/{}".format(kwargs.get("woocommerce_object_id"))).json()
        if "message" in shipping_data:
            _logger.info("Error in Importing Shipping : %r",shipping_data["message"])
            raise UserError("Error in importing shipping {}".format(str(shipping_data["message"]))) 
        vals = self.get_shipping_vals(channel_id,shipping_data)
        return vals

    def get_shipping_all(self,woocommerce ,channel_id, **kwargs):
        vals_list = []
        url = 'shipping_methods?page={}&per_page={}&order=asc'.format(kwargs.get("page"),kwargs.get("page_size"))
        shipping_data = woocommerce.get(url).json()
        if "message" in shipping_data:
            _logger.info("Error in Importing Shipping : %r",shipping_data["message"])
            raise UserError("Error in importing shipping {}".format(str(shipping_data["message"]))) 
        vals_list = list(map(lambda x: self.get_shipping_vals(channel_id,x),shipping_data))
        return vals_list

    def get_shipping_vals(self, channel_id, shipping_data):
        return {
                   "name": shipping_data.get("title"),
                   "store_id": shipping_data.get("id"),
                   "shipping_carrier": shipping_data.get("title"),
                   "channel_id": channel_id.id,
                   "channel": channel_id.channel,
                   "description": shipping_data.get("description",False)
                }