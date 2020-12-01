import argparse

from odoo.addons.scld_integration.controllers.controllers import ScldIntegrationController


def integrate():
    integrator = ScldIntegrationController();





    if __name__ == '__main__':
        # Parse the command line arguments
        parser = argparse.ArgumentParser()
        parser.add_argument('--action')
        parser.add_argument('--public')
        parser.add_argument('--secret')
        parser.add_argument('--integration_id')
        parser.add_argument('--partner_id')
        args = parser.parse_args()

        action = args.action
        public_key = args.public
        secret_key = args.secret
        partner_id = args.partner_id
        integration_id = args.integration_id

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
