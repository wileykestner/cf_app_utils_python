import json
from cf_app_utils.service_locator import ServiceLocator
from fixtures import rediscloud_service_credentials, \
    blue_service_one_credentials, blue_service_two_credentials, \
    red_service_one_credentials
import unittest
from cf_app_utils.credentials_locator import CredentialsLocator


class TestCredentialsLocator(unittest.TestCase):
    def setUp(self):
        with open("fixtures/vcap_services_example.json") as json_file:
            services_string = json_file.read()
            services = json.loads(services_string)
            self.subject = CredentialsLocator(services_locator=ServiceLocator(services=services))

    def test_find_credentials_for_first_service_with_name(self):
        find = self.subject.find_credentials_for_first_service_with_name
        credentials = find('rediscloud')

        self.assertEqual(credentials, rediscloud_service_credentials())

    def test_find_credentials_for_missing_service_with_name(self):
        find = self.subject.find_credentials_for_first_service_with_name
        credentials = find('a-missing-service')

        self.assertIsNone(credentials)

    def test_find_credentials_for_first_service_with_tag(self):
        find = self.subject.find_credentials_for_first_service_with_tag
        credentials = find('blue')

        self.assertEqual(credentials, blue_service_one_credentials())

    def test_find_credentials_for_first_service_with_missing_tag(self):
        find = self.subject.find_credentials_for_first_service_with_tag
        credentials = find('missing-tag')

        self.assertIsNone(credentials)

    def test_find_all_credentials_for_services_with_tag(self):
        find = self.subject.find_all_credentials_for_services_with_tag
        expected_credentials = [blue_service_one_credentials(),
                                blue_service_two_credentials(),
                                red_service_one_credentials()]
        credentials = find('color')

        self.assertEqual(credentials, expected_credentials)

    def test_find_all_credentials_for_services_with_tags(self):
        find = self.subject.find_all_credentials_for_services_with_all_tags
        expected_credentials = [blue_service_one_credentials(),
                                blue_service_two_credentials(),]
        credentials = find(['color', 'blue'])

        self.assertEqual(credentials, expected_credentials)

    def test_find_credentials_for_first_service_with_label(self):
        find = self.subject.find_credentials_for_first_service_with_label
        expected_credentials = blue_service_one_credentials()
        credentials = find('colorservice')

        self.assertEqual(credentials, expected_credentials)

    def test_find_credentials_for_first_service_with_missing_label(self):
        find = self.subject.find_credentials_for_first_service_with_label
        credentials = find('missinglabel')

        self.assertIsNone(credentials)

    def test_find_credentials_for_services_with_label(self):
        find = self.subject.find_credentials_for_services_with_label
        expected_credentials = [blue_service_one_credentials(),
                                red_service_one_credentials()]
        credentials = find('colorservice')

        self.assertEqual(credentials, expected_credentials)