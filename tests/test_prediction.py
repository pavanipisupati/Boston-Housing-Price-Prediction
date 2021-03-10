from app.server_app import do_prediction
import json
import unittest
import requests

''' This test case takes different json data points and tests against the prediction function '''

class PredictionTest(unittest.TestCase):

    def test_pred(self):
        json1 = {
            "CRIM" : 0.02731,
            "ZN" : 18.0,
            "INDUS" : 3.14,
            "CHAS" : 0.0,
            "NOX" : 0.546,
            "RM" : 1.654,
            "AGE" : 34.4,
            "DIS" : 4.9874,
            "RAD" : 3.0,
            "TAX" : 234.0,
            "PTRATIO" : 18,
            "B" : 384.90,          
            "LSTAT" : 284.55
        }
        self.assertEqual(2.522563005061876, do_prediction(json1))
        
    def test_big_home(self):
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
        self.assertEqual(20.277903803113965, do_prediction(json1))

 

if __name__ == '__main__':
    unittest.main()
