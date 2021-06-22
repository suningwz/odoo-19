# -*- coding: utf-8 -*-
import requests
from requests import post, exceptions, Response
import argparse
import json

from odoo.addons.web.controllers.main import env


def is_partner(self, partner):
    sql = "select name from public.res_partner where id = " + partner
    self.env.cr.execute(sql)
    res = self.env.cr.fetchone()

    if res:
        return True
    else:
        return False


def get_parcel(public_key, secret_key, partner_id=None):
    try:
        SENDCLOUD_API_URL = 'https://panel.sendcloud.sc/api/v2/'
        response = requests.get(SENDCLOUD_API_URL + 'parcels', auth=(public_key, secret_key))
        assert response.status_code == 200
    except exceptions.HTTPError as e:
        return Response()

    response.raise_for_status()

    print(response.json())


def cancel_parcel(public_key, secret_key, partner_id=None):
    headers = {'Content-Type': 'application/json'}
    if partner_id:
        headers['Sendcloud-Partner-Id'] = partner_id

    # Data can be a empty JSON response
    data = {}

    # Ask the script user to enter the parcel/shipment id.
    parcel_id = input('Enter the ID of the shipment that you want to cancel.')

    # Shipment/parcel id is part of the URL.
    base_url = 'https://panel.sendcloud.sc/api/v2/'
    url = base_url + 'parcels/{parcel_id}/cancel/'.format(
        parcel_id=parcel_id
    )
    response = post(
        headers=headers,
        url=url,
        data=json.dumps(data),
        auth=(public_key, secret_key,)
    )

    try:
        # response.status_code should be HTTP 200,
        # if this is not the case. Throw a exception.
        response.raise_for_status()
    except exceptions.HTTPError as e:
        if e.response.status_code not in [
            200,  # Cancelled
            202,  # Cancellation queued
            410  # Cancelled before label creation
        ]:
            raise e

    # Important to check the response as it may be different based on the state
    # of the shipment.
    print(response.json())


def get_integrations(public_key, secret_key, partner_id=None):
    try:
        SENDCLOUD_API_URL = 'https://panel.sendcloud.sc/api/v2/'
        response = requests.get(SENDCLOUD_API_URL + 'integrations', auth=(public_key, secret_key))
        assert response.status_code == 200
    except Exception as e:
        return Response(json.dumps({'error': str(e)}), content_type='application/json;charset=utf-8', status=505)

    #headers = {'Content-Type': 'application/json'}

    #if partner_id:
     #   headers['Sendcloud-Partner-Id'] = partner_id

    response.raise_for_status()

    print(response.json())


def get_shipment(public_key, secret_key, partner_id):
    try:
        SENDCLOUD_API_URL = 'https://panel.sendcloud.sc/api/v2/integrations/'
        response = requests.get(SENDCLOUD_API_URL + partner_id + '/' + 'shipments', auth=(public_key, secret_key))
        assert response.status_code == 200
    except Exception as e:
        return Response(json.dumps({'error': str(e)}), content_type='application/json;charset=utf-8', status=505)

    # headers = {'Content-Type': 'application/json'}

    # if partner_id:
    #   headers['Sendcloud-Partner-Id'] = partner_id

    response.raise_for_status()

    print(response.text)

    # Para rellenar un Pedido
    # 1. hay que comprobar si el CLIENTE INTEGRADO existe en Odoo
    # el id es el id dado por la integración
    # conn = psycopg2.connect("odoo14","odoo","odoo")

    # if (is_partner(self, partner_id)):
    #   print(partner_id)
    # else:
    #   print("partner no existe")

    # 2. luego hay que generar la cabecera del pedido
    sql = "select name from public.res_partner where id = " + partner_id
    env.cr.execute(sql)
    res = env.cr.fetchone()



    # 4. luego las líneas

    # tabla sales_order


def create_parcel(public_key, secret_key, integration_id=None, partner_id=None):
    try:
        SENDCLOUD_API_URL = 'https://panel.sendcloud.sc/api/v2/'
        parcels = requests.get(SENDCLOUD_API_URL + 'parcels', auth=(public_key, secret_key))
        assert parcels.status_code == 200
    except Exception as e:
        return Response(json.dumps({'error': str(e)}), content_type='application/json;charset=utf-8', status=505)

    data = parcels.json()

    headers = {'Content-Type': 'application/json'}

    if partner_id:
        headers['Sendcloud-Partner-Id'] = partner_id

    response = post(
        headers=headers,
        url='https://panel.sendcloud.sc/api/v2/parcels/',
        data=json.dumps(data),
        auth=(public_key, secret_key,)
    )

    # response.status_code should be HTTP 200,
    # if this is not the case. Throw a exception.
    response.raise_for_status()

    # Show the response on stdout.
    # It may be useful to remember the "parcel id".
    # This can be found in the response.
    print(response.json())
    # print(paquetes)

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
            'create': create_parcel,
            'get_parcel': get_parcel,
            'get_shipment': get_shipment,
            'get_integrations': get_integrations,
            'cancel': cancel_parcel
        }

        action_func = actions[action]
        action_func(public_key, secret_key, partner_id)
