__title__ = 'PyUnio'
__version__ = '1.1.0'
__author__ = 'Mihir Singh (citruspi)'
__license__ = 'MIT License'
__copyright__ = 'Copyright 2013 Mihir Singh'

try:

    import json
    import requests
    from inspect import stack
    from requests_oauthlib import OAuth1

except ImportError as e:

    raise Exception(e)


class pyunio(object):

    def __init__(self):

        self.specs = dict

    def use(self, service):

        try:

            with open('specs/' + service + '.json') as service_definition:
                self.specs = json.load(service_definition)

        except Exception as e:

            raise Exception(e)

    def get(self, route, params):

        if 'body' not in params: params['body'] = {}
        if 'header' not in params: params['header'] = {}

        try:

            if stack()[0][3] in self.specs['resources'][route]['methods']:

                if 'oauth' in params:

                    return getattr(
                        requests, stack()[0][3])(self.specs['api_root'] + '/' + self.specs['resources'][route]['path'],
                                                 data=params['body'],
                                                 headers=params['header'],
                                                 auth=self.oauth_handle(params))

                else:

                    return getattr(
                        requests, stack()[0][3])(self.specs['api_root'] + '/' + self.specs['resources'][route]['path'],
                                                 data=params['body'],
                                                 headers=params['header'])

            else:

                raise Exception("The HTTP verb '%s' is not defined for '%s'.") % (
                    stack()[0][3], route)

        except KeyError as e:

            raise Exception(e)

    def post(self, route, params):

        if 'body' not in params: params['body'] = {}
        if 'header' not in params: params['header'] = {}

        try:

            if stack()[0][3] in self.specs['resources'][route]['methods']:

                if 'oauth' in params:

                    return getattr(
                        requests, stack()[0][3])(self.specs['api_root'] + '/' + self.specs['resources'][route]['path'],
                                                 data=params['body'],
                                                 headers=params['header'],
                                                 auth=self.oauth_handle(params))

                else:

                    return getattr(
                        requests, stack()[0][3])(self.specs['api_root'] + '/' + self.specs['resources'][route]['path'],
                                                 data=params['body'],
                                                 headers=params['header'])

            else:

                raise Exception("The HTTP verb '%s' is not defined for '%s'.") % (
                    stack()[0][3], route)

        except KeyError as e:

            raise Exception(e)

    def put(self, route, params):

        if 'body' not in params: params['body'] = {}
        if 'header' not in params: params['header'] = {}

        try:

            if stack()[0][3] in self.specs['resources'][route]['methods']:

                if ('oauth') in params:

                    return getattr(
                        requests, stack()[0][3])(self.specs['api_root'] + '/' + self.specs['resources'][route]['path'],
                                                 data=params['body'],
                                                 headers=params['header'],
                                                 auth=self.oauth_handle(params))

                else:

                    return getattr(
                        requests, stack()[0][3])(self.specs['api_root'] + '/' + self.specs['resources'][route]['path'],
                                                 data=params['body'],
                                                 headers=params['header'])

            else:

                raise Exception("The HTTP verb '%s' is not defined for '%s'.") % (
                    stack()[0][3], route)

        except KeyError as e:

            raise Exception(e)

    def delete(self, route, params):

        if 'body' not in params: params['body'] = {}
        if 'header' not in params: params['header'] = {}

        try:

            if stack()[0][3] in self.specs['resources'][route]['methods']:

                if ('oauth') in params:

                    return getattr(
                        requests, stack()[0][3])(self.specs['api_root'] + '/' + self.specs['resources'][route]['path'],
                                                 data=params['body'],
                                                 headers=params['header'],
                                                 auth=self.oauth_handle(params))

                else:

                    return getattr(
                        requests, stack()[0][3])(self.specs['api_root'] + '/' + self.specs['resources'][route]['path'],
                                                 data=params['body'],
                                                 headers=params['header'])

            else:

                raise Exception("The HTTP verb '%s' is not defined for '%s'.") % (
                    stack()[0][3], route)

        except KeyError as e:

            raise Exception(e)

    def oauth_handle(self, params):

        try:

            oauth = OAuth1(params['ouath']['consumer_key'],
                           params['ouath']['consumer_secret'],
                           params['ouath']['access_token'],
                           params['ouath']['access_token_secret'],
                           signature_type='auth_header')

            return (oauth)

        except Exception as e:

            raise Exception(e)

pyunio = pyunio()
