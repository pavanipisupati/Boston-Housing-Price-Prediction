import json
import unittest
import requests

''' This test class is used to test the api against different incoming JSON formats '''

server_url="http://0.0.0.0:8080/predict"

class ApiTest(unittest.TestCase):

    ''' Function for testing api with recommended JSON format as input request'''
    def test_good_request(self):
        json1 = {
            "CRIM" : 0.02731,
            "ZN" : 18.0,
            "INDUS" : 3.14,
            "CHAS" : 0.0,
            "NOX" : 0.546,
            "RM" : 5.654,
            "AGE" : 34.4,
            "DIS" : 4.9874,
            "RAD" : 3.0,
            "TAX" : 234.0,
            "PTRATIO" : 18,
            "B" : 384.90,          
            "LSTAT" : 284.55
        }
        res = requests.post(server_url,json=json1)
        self.assertEqual(200, res.status_code)
        self.assertEqual('20.277903803113965\n',res.text)

    ''' Function to test api with empty request body'''
    def test_request_without_body(self):
        response = requests.post(server_url)
        self.assertEqual("Missing request body", response.text)

    ''' Function to test incomplete input request '''
    def test_request_with_invalid_json(self):
        bad_json={"CRIM" : 0.02731}
        response = requests.post(server_url,json=bad_json)
        self.assertEqual("Incoming json format is invalid", response.text)        

if __name__ == '__main__':
    unittest.main()
