from service_locator import ServiceLocator


class CredentialsLocator(object):

    def __init__(self, services_locator=None):
        assert services_locator
        self.service_locator = services_locator

    def find_credentials_for_first_service_with_name(self, name):
        service = self.service_locator.find_first_service_with_name(name)

        return self.credentials_or_none_with_service(service)

    def find_credentials_for_first_service_with_tag(self, tag):
        service = self.service_locator.find_first_service_with_tag(tag)

        return self.credentials_or_none_with_service(service)

    def find_all_credentials_for_services_with_tag(self, tag):
        services = self.service_locator.find_services_with_tag(tag)

        return self.credentials_with_services(services)

    def find_all_credentials_for_services_with_all_tags(self, tags):
        services = self.service_locator.find_services_with_all_tags(tags)

        return self.credentials_with_services(services)

    def find_credentials_for_first_service_with_label(self, label):
        service = self.service_locator.find_first_service_with_label(label)

        return self.credentials_or_none_with_service(service)

    def find_credentials_for_services_with_label(self, label):
        services = self.service_locator.find_services_with_label(label)

        return self.credentials_with_services(services)

    @staticmethod
    def credentials_or_none_with_service(service):
        return None if not service else service.get('credentials', None)

    @staticmethod
    def credentials_with_services(services):
        return [service['credentials'] for service in services]