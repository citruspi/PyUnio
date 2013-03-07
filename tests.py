import json
import unittest
from pyunio import pyunio

pyunio.use('httpbin')

params = {
            'body': {
                        'name': 'James Bond'
                    }
         }


def test_get():

    response = json.loads(pyunio.get('get', params).text)

    assert(response['args']['name'] == 'James Bond')


def test_post():

    response = json.loads(pyunio.post('post', params).text)

    assert(response['args']['name'] == 'James Bond')


def test_put():

    response = json.loads(pyunio.put('put', params).text)

    assert(response['args']['name'] == 'James Bond')


def test_delete():

    response = json.loads(pyunio.delete('delete', params).text)

    assert(response['args']['name'] == 'James Bond')
