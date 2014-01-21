import json
import unittest
import sys
if sys.version_info[0] == 2:
    from urllib import urlencode
else:
    from urllib.parse import urlencode

from pyunio import pyunio

pyunio.use('httpbin')

params_get = {
            'params': {
                        'name': 'James Bond'
                    }
        }

params_body = {
            'body': {
                        'name': 'James Bond'
                    }
         }

class pyuniotTest(unittest.TestCase): 

    def test_get(self):
        response = json.loads(pyunio.get('get', params_get).text)
        self.assertEqual(response['args']['name'], 'James Bond')


    def test_post(self):
        response = json.loads(pyunio.post('post', params_body).text)
        self.assertEqual(response['form']['name'],'James Bond')


    def test_put(self):
        response = json.loads(pyunio.put('put', params_body).text)
        self.assertEqual(response['form']['name'], 'James Bond')


    def test_delete(self):
        response = json.loads(pyunio.delete('delete', params_body).text)
        self.assertEqual(response['data'], urlencode({'name':'James Bond'}))


if __name__ == '__main__':
    unittest.main()    
