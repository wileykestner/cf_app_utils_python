import json
from fixtures import blue_service_one, blue_service_two, red_service_one, \
    rediscloud_service
import unittest
from cf_app_utils.service_locator import ServiceLocator


class TestServiceLocator(unittest.TestCase):

    def setUp(self):
        with open("fixtures/vcap_services_example.json") as json_file:
            services_string = json_file.read()
            services = json.loads(services_string)
            self.subject = ServiceLocator(services=services)

    def test_find_first_service_with_name(self):
        service = self.subject.find_first_service_with_name('rediscloud')

        self.assertEqual(service, rediscloud_service())

    def test_find_first_service_missing_name(self):
        service = self.subject.find_first_service_with_name('no-service')

        self.assertIsNone(service)

    def test_find_first_service_with_tag(self):
        service = self.subject.find_first_service_with_tag('blue')

        self.assertEqual(service, blue_service_one())

    def test_find_first_service_with_missing_tag(self):
        service = self.subject.find_first_service_with_tag('missing-tag')

        self.assertIsNone(service)

    def test_find_services_by_tag(self):
        expected_services = [blue_service_one(),
                             blue_service_two(),
                             red_service_one()]

        services = self.subject.find_services_with_tag('color')

        self.assertEqual(services, expected_services)

    def test_find_services_by_tags(self):
        expected_services = [blue_service_one(),
                             blue_service_two()]

        service = self.subject.find_services_with_all_tags(['color', 'blue'])

        self.assertEqual(service, expected_services)

    def test_find_services_with_label(self):
        expected_services = [blue_service_two()]

        services = self.subject.find_services_with_label('sillyservice')

        self.assertEqual(services, expected_services)

    def test_find_services_with_label_containing(self):
        expected_services = [blue_service_two()]

        services = self.subject.find_services_with_label_containing('lly')

        self.assertEqual(services, expected_services)

    def test_find_first_service_with_label(self):
        service = self.subject.find_first_service_with_label('sillyservice')

        self.assertEqual(service, blue_service_two())