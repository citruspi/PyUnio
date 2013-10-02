import json
import unittest
from pyunio import pyunio

pyunio.use('httpbin')

params = {
            'body': {
                        'name': 'James Bond'
                    }
         }

class pyuniotTest(unittest.TestCase): 

    def test_get(self):
        response = json.loads(pyunio.get('get', params).text)
        self.assertEqual(response['args']['name'], 'James Bond')


    def test_post(self):
        response = json.loads(pyunio.post('post', params).text)
        self.assertEqual(response['args']['name'], 'James Bond')


    def test_put(self):
        response = json.loads(pyunio.put('put', params).text)
        self.assertEqual(response['args']['name'], 'James Bond')


    def test_delete(self):
        response = json.loads(pyunio.delete('delete', params).text)
        self.assertEqual(response['args']['name'], 'James Bond')


if __name__ == '__main__':
    unittest.main()    
