# coding=utf-8
"""
This code was generated by
\ / _    _  _|   _  _
 | (_)\/(_)(_|\/| |(/_  v1.0.0
      /       /       
"""

from tests import IntegrationTestCase
from tests.holodeck import Request
from twilio.base.exceptions import TwilioException
from twilio.http.response import Response


class ApplicationTestCase(IntegrationTestCase):

    def test_create_request(self):
        self.holodeck.mock(Response(500, ''))
        
        with self.assertRaises(TwilioException):
            self.client.api.v2010.accounts(sid="ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
                                 .applications.create(friendly_name="friendly_name")
        
        values = {
            'FriendlyName': "friendly_name",
        }
        
        self.holodeck.assert_has_request(Request(
            'post',
            'https://api.twilio.com/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Applications.json',
            data=values,
        ))

    def test_create_response(self):
        self.holodeck.mock(Response(
            200,
            '''
            {
                "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "api_version": "2010-04-01",
                "date_created": "Mon, 22 Aug 2011 20:59:45 +0000",
                "date_updated": "Tue, 18 Aug 2015 16:48:57 +0000",
                "friendly_name": "Application Friendly Name",
                "message_status_callback": "http://www.example.com/sms-status-callback",
                "sid": "APaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "sms_fallback_method": "GET",
                "sms_fallback_url": "http://www.example.com/sms-fallback",
                "sms_method": "GET",
                "sms_status_callback": "http://www.example.com/sms-status-callback",
                "sms_url": "http://example.com",
                "status_callback": "http://example.com",
                "status_callback_method": "GET",
                "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Applications/APaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.json",
                "voice_caller_id_lookup": false,
                "voice_fallback_method": "GET",
                "voice_fallback_url": "http://www.example.com/voice-callback",
                "voice_method": "GET",
                "voice_url": "http://example.com"
            }
            '''
        ))
        
        actual = self.client.api.v2010.accounts(sid="ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
                                      .applications.create(friendly_name="friendly_name")
        
        self.assertIsNotNone(actual)

    def test_delete_request(self):
        self.holodeck.mock(Response(500, ''))
        
        with self.assertRaises(TwilioException):
            self.client.api.v2010.accounts(sid="ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
                                 .applications(sid="APaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa").delete()
        
        self.holodeck.assert_has_request(Request(
            'delete',
            'https://api.twilio.com/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Applications/APaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.json',
        ))

    def test_delete_response(self):
        self.holodeck.mock(Response(
            204,
            None,
        ))
        
        actual = self.client.api.v2010.accounts(sid="ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
                                      .applications(sid="APaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa").delete()
        
        self.assertTrue(actual)

    def test_fetch_request(self):
        self.holodeck.mock(Response(500, ''))
        
        with self.assertRaises(TwilioException):
            self.client.api.v2010.accounts(sid="ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
                                 .applications(sid="APaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa").fetch()
        
        self.holodeck.assert_has_request(Request(
            'get',
            'https://api.twilio.com/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Applications/APaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.json',
        ))

    def test_fetch_response(self):
        self.holodeck.mock(Response(
            200,
            '''
            {
                "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "api_version": "2010-04-01",
                "date_created": "Mon, 22 Aug 2011 20:59:45 +0000",
                "date_updated": "Tue, 18 Aug 2015 16:48:57 +0000",
                "friendly_name": "Application Friendly Name",
                "message_status_callback": "http://www.example.com/sms-status-callback",
                "sid": "APaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "sms_fallback_method": "GET",
                "sms_fallback_url": "http://www.example.com/sms-fallback",
                "sms_method": "GET",
                "sms_status_callback": "http://www.example.com/sms-status-callback",
                "sms_url": "http://example.com",
                "status_callback": "http://example.com",
                "status_callback_method": "GET",
                "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Applications/APaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.json",
                "voice_caller_id_lookup": false,
                "voice_fallback_method": "GET",
                "voice_fallback_url": "http://www.example.com/voice-callback",
                "voice_method": "GET",
                "voice_url": "http://example.com"
            }
            '''
        ))
        
        actual = self.client.api.v2010.accounts(sid="ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
                                      .applications(sid="APaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa").fetch()
        
        self.assertIsNotNone(actual)

    def test_list_request(self):
        self.holodeck.mock(Response(500, ''))
        
        with self.assertRaises(TwilioException):
            self.client.api.v2010.accounts(sid="ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
                                 .applications.list()
        
        self.holodeck.assert_has_request(Request(
            'get',
            'https://api.twilio.com/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Applications.json',
        ))

    def test_read_full_response(self):
        self.holodeck.mock(Response(
            200,
            '''
            {
                "applications": [
                    {
                        "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "api_version": "2010-04-01",
                        "date_created": "Fri, 21 Aug 2015 00:07:25 +0000",
                        "date_updated": "Fri, 21 Aug 2015 00:07:25 +0000",
                        "friendly_name": "d8821fb7-4d01-48b2-bdc5-34e46252b90b",
                        "message_status_callback": null,
                        "sid": "APaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "sms_fallback_method": "POST",
                        "sms_fallback_url": null,
                        "sms_method": "POST",
                        "sms_status_callback": null,
                        "sms_url": null,
                        "status_callback": null,
                        "status_callback_method": "POST",
                        "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Applications/APaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.json",
                        "voice_caller_id_lookup": false,
                        "voice_fallback_method": "POST",
                        "voice_fallback_url": null,
                        "voice_method": "POST",
                        "voice_url": null
                    }
                ],
                "end": 0,
                "first_page_uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Applications.json?PageSize=1&Page=0",
                "last_page_uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Applications.json?PageSize=1&Page=35",
                "next_page_uri": null,
                "num_pages": 36,
                "page": 0,
                "page_size": 1,
                "previous_page_uri": null,
                "start": 0,
                "total": 36,
                "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Applications.json?PageSize=1&Page=0"
            }
            '''
        ))
        
        actual = self.client.api.v2010.accounts(sid="ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
                                      .applications.list()
        
        self.assertIsNotNone(actual)

    def test_read_empty_response(self):
        self.holodeck.mock(Response(
            200,
            '''
            {
                "applications": [],
                "end": 0,
                "first_page_uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Applications.json?PageSize=1&Page=0",
                "last_page_uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Applications.json?PageSize=1&Page=35",
                "next_page_uri": null,
                "num_pages": 36,
                "page": 0,
                "page_size": 1,
                "previous_page_uri": null,
                "start": 0,
                "total": 36,
                "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Applications.json?PageSize=1&Page=0"
            }
            '''
        ))
        
        actual = self.client.api.v2010.accounts(sid="ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
                                      .applications.list()
        
        self.assertIsNotNone(actual)

    def test_update_request(self):
        self.holodeck.mock(Response(500, ''))
        
        with self.assertRaises(TwilioException):
            self.client.api.v2010.accounts(sid="ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
                                 .applications(sid="APaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa").update()
        
        self.holodeck.assert_has_request(Request(
            'post',
            'https://api.twilio.com/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Applications/APaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.json',
        ))

    def test_update_response(self):
        self.holodeck.mock(Response(
            200,
            '''
            {
                "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "api_version": "2010-04-01",
                "date_created": "Mon, 22 Aug 2011 20:59:45 +0000",
                "date_updated": "Tue, 18 Aug 2015 16:48:57 +0000",
                "friendly_name": "Application Friendly Name",
                "message_status_callback": "http://www.example.com/sms-status-callback",
                "sid": "APaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "sms_fallback_method": "GET",
                "sms_fallback_url": "http://www.example.com/sms-fallback",
                "sms_method": "GET",
                "sms_status_callback": "http://www.example.com/sms-status-callback",
                "sms_url": "http://example.com",
                "status_callback": "http://example.com",
                "status_callback_method": "GET",
                "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Applications/APaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.json",
                "voice_caller_id_lookup": false,
                "voice_fallback_method": "GET",
                "voice_fallback_url": "http://www.example.com/voice-callback",
                "voice_method": "GET",
                "voice_url": "http://example.com"
            }
            '''
        ))
        
        actual = self.client.api.v2010.accounts(sid="ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
                                      .applications(sid="APaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa").update()
        
        self.assertIsNotNone(actual)
