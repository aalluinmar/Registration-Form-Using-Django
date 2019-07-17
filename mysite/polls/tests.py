from django.test import TestCase
from unittest.mock import patch
import json

class Test_Register(TestCase):
    #checking with valid data
    def test_register_with_valid_data(self):
        """
            Validating data by giving valid data
        """
        payload = {
            "usertype": "Retailer",
            "name": "Test",
            "email": "alleba@gmail.com",
            "password": "Test@123"
        }
        response = self.client.post('/polls/register/', data=json.dumps(payload), content_type="application/json")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['email'], 'alleba@gmail.com')

    #checking with missing usertype
    def test_register_with_missing_usertype(self):
        """
            Validating data by missing Usertype
        """
        payload = {
            "name": "Test",
            "email": "alleba@gmail.com",
            "password": "Test@123"
        }
        response = self.client.post('/polls/register/', data=json.dumps(payload), content_type="application/json")
        # print(response.json())
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['result'], 'Please provide usertype')

    #checking with invalid data
    def test_register_with_invalid_data(self):
        """
            Validating data by giving not wrong Email
        """
        payload = {
            "usertype": "Retailer",
            "name": "Test",
            "email": "allebagmail.com",
            "password": "Test@123"
        }
        response = self.client.post('/polls/register/', data=json.dumps(payload), content_type="application/json")
        # print(response.json())
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['result'], 'Please provide valid email : allebagmail.com')

    #checking with invalid data of wrong usertype
    def test_register_with_invalid_data_Of_wrong_Usertype(self):
        """
            Validating data by giving not Usertype
        """
        payload = {
            "usertype": "etailer",
            "name": "Test",
            "email": "alleba@gmail.com",
            "password": "Test@123"
        }
        response = self.client.post('/polls/register/', data=json.dumps(payload), content_type="application/json")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['result'], 'Please provide valid usertype : etailer, should be in ['"'Retailer'"', '"'Customer'"']')
