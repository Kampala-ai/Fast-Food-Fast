""" base tests"""
from unittest import TestCase
from flask import json
from main import views
from unittest import TestCase
from main.db import Database
from instance import myapp


class BaseTests(TestCase):
    """create a base test class"""
    def setUp(self):
      self.apps = myapp
      self.client = self.apps.test_client
      self.order={'location':'kampala',
                'payment_mode':'cash',
                'order_items':[{'items':'eggs','price':'1000'}]}
      self.customer={'phone_number':'0703455445',
                      'email':'opi@gmail.com',
                      'username':'opio',
                      'password':'opioqwt'
                  }
      self.login_add={'username':'opio','password':'opioqwt'}

    def signin_user(self,user):
        """ test for posting an order """
        add_result = self.client().post('/api/v1/auth/signup', content_type='application/json', data=json.dumps(user))
        return add_result

    def login(self,tp):
        respo=add_result=self.client().post('/api/v1/auth/login',content_type='application/json', data=json.dumps(self.login_add))
        respo_data=json.loads(respo.data.decode())
        token=respo_data['access_token']
        return token
    