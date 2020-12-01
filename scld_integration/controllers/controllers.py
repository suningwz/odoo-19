# -*- coding: utf-8 -*-
from datetime import date
from distutils.util import execute
from multiprocessing import connection

import requests
import argparse
import json
import xmlrpc.client

url = 'https://delegalog-odoo14.odoo.com:443'
db = 'delegalog-odoo14-main-1667547'
username = 'admin'
password = 'e40fdaf537b1a9b6e962d89a0a8bcffe8cf2fad6'
models = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(url))
common = xmlrpc.client.ServerProxy('{}/xmlrpc/2/common'.format(url))
uid = common.authenticate(db, username, password, {})


def create_parcel(publickey, secretkey, partnerid=None):
    # Example data for a minimal implementation.
    # Notice that you only need little information
    # to get started to be able to process a shipment
    # with the SendCloud platform.

    data = {
        "parcel": {
            "name": "John Doe",
            "company_name": "SendCloud",
            "address": "Insulindelaan",
            "postal_code": "5642CV",
            "house_number": "115",
            "city": "Eindhoven",
            "country": "NL",
            "telephone": "+31612345678",
            "email": "john.doe@example.com",
            "weight": "10.000",  # in KG
            "order_number": "1234567890",
        }
    }

    headers = {'Content-Type': 'application/json'}

    # Optional, but recommended for partners
    # This allows us to identify that your request
    # came from your platform.
    if partnerid:
        headers['Sendcloud-Partner-Id'] = partnerid

    response = requests.post(
        headers=headers,
        url='https://panel.sendcloud.sc/api/v2/parcels/',
        data=json.dumps(data),
        auth=(publickey, secretkey,)
    )

    # response.status_code should be HTTP 200,
    # if this is not the case. Throw a exception.
    response.raise_for_status()

    # Show the response on stdout.
    # It may be useful to remember the "parcel id".
    # This can be found in the response.
    print(response.json())


def cancel_parcel(publickey, secretkey, partnerid=None):
    # Very similar to the example above.
    headers = {'Content-Type': 'application/json'}
    if partnerid:
        headers['Sendcloud-Partner-Id'] = partnerid

    # Data can be a empty JSON response
    data = {}

    # Ask the script user to enter the parcel/shipment id.
    parcel_id = input('Enter the ID of the shipment that you want to cancel.')

    # Shipment/parcel id is part of the URL.
    base_url = 'https://panel.sendcloud.sc/api/v2/'
    url = base_url + 'parcels/{parcel_id}/cancel/'.format(
        parcel_id=parcel_id
    )
    response = requests.post(
        headers=headers,
        url=url,
        data=json.dumps(data),
        auth=(publickey, secretkey,)
    )

    try:
        # response.status_code should be HTTP 200,
        # if this is not the case. Throw a exception.
        response.raise_for_status()
    except requests.exceptions.HTTPError as e:
        if e.response.status_code not in [
            200,  # Cancelled
            202,  # Cancellation queued
            410  # Cancelled before label creation
        ]:
            raise e

    # Important to check the response as it may be different based on the state
    # of the shipment.
    print(response.json())


def get_integrations(publickey, secretkey, partnerid=None):
    try:
        SENDCLOUD_API_URL = 'https://panel.sendcloud.sc/api/v2/'
        response = requests.get(SENDCLOUD_API_URL + 'integrations', auth=(publickey, secretkey))
        assert response.status_code == 200
    except requests.exceptions.HTTPError as e:
        return e.response(json.dumps({'error': str(e)}), content_type='application/json;charset=utf-8', status=505)

    response.raise_for_status()
    print(response.json())


def get_parcel(publickey, secretkey):
    try:
        SENDCLOUD_API_URL = 'https://panel.sendcloud.sc/api/v2/'
        response = requests.get(SENDCLOUD_API_URL + 'parcels', auth=(publickey, secretkey))
        assert response.status_code == 200
    except requests.exceptions.HTTPError as e:
        return e.response()

    response.raise_for_status()
    print(response.json())


def is_partner(partner, env=None):
    Sql = "select name from public.res_partner where id = " + partner
    env.cr.execute(Sql)
    res = env.cr.fetchone()

    if res:
        return True
    else:
        return False


def get_max_partner_id(env=None):
    Sql = "select max(id) from public.res_partner where id = "
    env.cr.execute(Sql)
    return env.cr.fetchone() + 1


def get_connected(publickey=None, secretkey=None, partnerid=None):
    print("common", common.version())
    return common.login(db, username, password)


def exec_search_read(table, fields_values, i):
    return models.execute(db, uid, password, table, 'search_read', [[fields_values]])[i]


def exec_insert(table, fields_values):
    models.execute_kw(db, uid, password, table, 'create', [{fields_values}])


def get_shipment(publickey, secretkey, partnerid):
    try:
        SENDCLOUD_API_URL = 'https://panel.sendcloud.sc/api/v2/integrations/'
        response = requests.get(SENDCLOUD_API_URL + partnerid + '/' + 'shipments', auth=(publickey, secretkey))
        assert response.status_code == 200
    except requests.exceptions.HTTPError as e:
        return e.response(json.dumps({'error': str(e)}), content_type='application/json;charset=utf-8', status=505)

    headers = {'Content-Type': 'application/json'}

    if partnerid:
        headers['Sendcloud-Partner-Id'] = partnerid

    response.raise_for_status()
    print(response.json())

    # Insert the head of the order
    for i in response['results']:
        id = i['order_number']
        campaign_id = i['']
        source_id = i['']
        medium_id = i['']
        access_token = i['']
        message_main_attachment_id = i['']
        name = i['']
        origin = i['']
        client_order_ref = i['']
        reference = i['']
        state = i['']
        date_order = i['']
        validity_date = i['']
        require_signature = i['']
        require_payment = i['']
        create_date = i['']
        user_id = i['']
        partner_id = i['']
        partner_invoice_id = i['']
        partner_shipping_id = i['']
        pricelist_id = i['']
        currency_id = i['']
        analytic_account_id = i['']
        invoice_status = i['']
        note = i['']
        amount_untaxed = i['']
        amount_tax = i['']
        amount_total = i['']
        currency_rate = i['']
        payment_term_id = i['']
        fiscal_position_id = i['']
        company_id = i['']
        team_id = i['']
        signed_by = i['']
        signed_on = i['']
        commitment_date = i['']
        show_update_pricelist = i['']
        create_uid = i['']
        write_uid = i['']
        write_date = i['']
        sale_order_template_id = i['']
        incoterm = i['']
        picking_policy = i['']
        warehouse_id = i['']
        procurement_group_id = i['']
        effective_date = i['']
        opportunity_id = i['']


if __name__ == '__main__':
    # Parse the command line arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('--action')
    parser.add_argument('--public')
    parser.add_argument('--secret')
    parser.add_argument('--partner_id')
    args = parser.parse_args()

    action = args.action
    public_key = args.public
    secret_key = args.secret
    partner_id = args.partner_id

    # Map arguments to actions
    actions = {
        'create_parcel': create_parcel,
        'cancel_parcel': cancel_parcel,
        'get_integrations': get_integrations,
        'get_shipment': get_shipment,
        'get_parcel': get_parcel,
        'get_connected': get_connected
    }

    action_func = actions[action]
    action_func(public_key, secret_key, partner_id)
