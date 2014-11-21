import json
import os
import unittest
from cf_app_utils.service_url_provider import ServiceURLProvider


class TestServiceURLProviderWithServices(unittest.TestCase):
    def setUp(self):
        with open("fixtures/vcap_services_example.json") as json_file:
            services_string = json_file.read()
            services = json.loads(services_string)
            self.subject = ServiceURLProvider.provider(services)

    def test_url_with_service_name_for_service_with_uri(self):
        url = self.subject.url_for_first_service_with_name('elephantsql')
        expected_url = 'postgres://mypostgresusername:mypostgrespassword@mypostgres.domain.com:5432/mydatabasename'

        self.assertEqual(url, expected_url)

    def test_url_with_service_name_for_service_with_port_hostname_pass(self):
        url = self.subject.url_for_first_service_with_name('rediscloud',
                                                           scheme='redis')
        expected_url = 'redis://:my-redis-password@my.redis.domain.com:15348'

        self.assertEqual(url, expected_url)

    def test_url_with_service_name_for_missing_service(self):
        url = self.subject.url_for_first_service_with_name('missing')

        self.assertIsNone(url)


class TestWithEnvironmentVariableSetup(TestServiceURLProviderWithServices):
    def setUp(self):
        with open("fixtures/vcap_services_example.json") as json_file:
            services_string = json_file.read()
            os.environ['VCAP_SERVICES'] = services_string
            self.subject = ServiceURLProvider.provider()
