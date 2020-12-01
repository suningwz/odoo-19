#! /bin/env python3
from datetime import date

import psycopg2
import requests
from requests import post, exceptions, Response
import argparse
import json


def is_partner_company(cr, partner):
    sql = "select name from res_partner where id = " + partner
    cr.execute(sql)
    record = cr.fetchone()

    print("You are connected to - ", record, "\n")

    if record:
        return True
    else:
        return False


def get_shipment(public_key, secret_key, partner_id):
    try:
        SENDCLOUD_API_URL = 'https://panel.sendcloud.sc/api/v2/integrations/'
        response = requests.get(SENDCLOUD_API_URL + partner_id + '/' + 'shipments', auth=(public_key, secret_key))
        assert response.status_code == 200
    except Exception as e:
        return Response(json.dumps({'error': str(e)}), content_type='application/json;charset=utf-8', status=505)

    headers = {'Content-Type': 'application/json'}

    if partner_id:
        headers['Sendcloud-Partner-Id'] = partner_id

    response.raise_for_status()
    res_dict = json.loads(response.text)
    print(response.json())

    #1. Conectar con la base de datos
    try:
        connection = psycopg2.connect(user="odoo",
                                      password="odoo",
                                      host="127.0.0.1",
                                      port="5432",
                                      database="odoo14")

        cr = connection.cursor()
    except (Exception, psycopg2.Error) as error:
        print("Error while connecting to PostgreSQL", error)

    #2. El partner compañía se crea a mano y tiene su propio código. Ahora hay que recoger su id de la tabla de mapeo.
    sql = "select partner_id from map_id_partner where sendcloudid = " + partner_id
    cr.execute(sql)
    record = cr.fetchone()


    if is_partner(cursor, partner_id):
        print(partner_id)
        partner_exist = True
    else:
        print("partner does not exist")
        return

    #3. El partner compañía se crea a mano y tiene su propio código. Ahora hay que recoger su id de la tabla de mapeo.


    for i in res_dict['results']:
        company_name = i['company_name']
        address = i['address']
        postal_code = i['postal_code']

    if not partner_exist:
        sql =   " INSERT INTO res_partner (" \
                "id, name, comnpany_id, create_date, display_name, lang" \
                "tz, active, type, street, zip"
                ") " \
        " VALUES (%s,%s,%s,%s,%s,%s) "
        record = \
                (
                partner_id, company_name, date.today(), partner_id, 'es_ES'
                'Europe/Madrid', '1', 'contact', address, postal_code
                )
        cursor.execute(sql, record)
        connection.commit()




    # 2. luego hay que generar la cabecera del pedido
    for i in res_dict['results']:
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

    try:
        sql = " INSERT INTO sale_order (id) " \
              " VALUES (%s,%s,%s,%s) "
        record = (new_id)
        cursor.execute(sql, record)
        connection.commit()
    except:
        print("error insert")

    # 4. luego las líneas

    # tabla sales_order


def get_parcel(public_key, secret_key, partner_id=None):
    try:
        SENDCLOUD_API_URL = 'https://panel.sendcloud.sc/api/v2/'
        response = requests.get(SENDCLOUD_API_URL + 'parcels', auth=(public_key, secret_key))
        assert response.status_code == 200
    except Exception as e:
        return Response(json.dumps({'error': str(e)}), content_type='application/json;charset=utf-8', status=505)

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

    headers = {'Content-Type': 'application/json'}

    if partner_id:
        headers['Sendcloud-Partner-Id'] = partner_id

    response.raise_for_status()

    print(response.json())


def create_parcel(public_key, secret_key, partner_id=None):
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
        'get': get_parcel,
        'getshipment': get_shipment,
        'getintegrations': get_integrations,
        'cancel': cancel_parcel
    }

    action_func = actions[action]
    action_func(public_key, secret_key, partner_id)





    # Para rellenar un Pedido
    # 2. El partner compañía se crea a mano y tiene su propio código. Ahora hay que recoger su id de la tabla de mapeo.
    Sql = "select partner_id from map_id_partner where sendcloud_id = " + partnerid
    env.cr.execute(Sql)
    Record = env.cr.fetchone()

    if is_partner(partnerid):
        print(partnerid)
        partner_exist = True
    else:
        print("partner does not exist")
        return

    # 3. El partner compañía se crea a mano y tiene su propio código. Ahora hay que recoger su id de la tabla de mapeo.
    for _i in Record['results']:
        company_name = _i['company_name']
        address = _i['address']
        postal_code = _i['postal_code']

    if not partner_exist:
        client = get_max_partner_id()
        Sql = "INSERT INTO res_partner (id, name, company_id, create_date, display_name, lang, tz, active, type, " \
              "street, zip) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) "
        Record = (client, company_name, partnerid, date.today(), partnerid, 'es_ES', 'Europe/Madrid', '1', 'contact', address, postal_code)

        execute(Sql, Record)
        connection.commit()

    # 2. luego hay que generar la cabecera del pedido
    for i in Record['results']:
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

    try:
        Sql = " INSERT INTO sale_order (id) " \
          " VALUES (%s,%s,%s,%s) "
        record = (new_id)
        cursor.execute(sql, record)
        connection.commit()
    except:


    print("error insert")

# 4. luego las líneas

# tabla sales_order
