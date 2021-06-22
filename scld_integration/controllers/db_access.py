# -*- coding: utf-8 -*-
import argparse


def select(public_key, secret_key, partner_id=None):
    print(response.json())


if __name__ == '__main__':
    # Parse the command line arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('--action')
    parser.add_argument('--public')
    parser.add_argument('--secret')
    parser.add_argument('--sentence')
    args = parser.parse_args()

    action = args.action
    public_key = args.public
    secret_key = args.secret
    sentence = args.sentence

    # Map arguments to actions
    actions = {
        'select': select,
    }

    action_func = actions[action]
    action_func(public_key, secret_key, sentence)
