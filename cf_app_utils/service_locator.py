import itertools


class ServiceLocator(object):
    def __init__(self, services=None):
        assert services
        self.services = services

    def find_first_service_with_name(self, service_name):
        services = self.services.get(service_name, None)

        return self.first_service_or_none(services)

    def find_first_service_with_tag(self, tag):
        services = self.find_services_with_tag(tag)

        return services[0] if len(services) else None

    def find_services_with_tag(self, tag):

        return [s for s in self.all_services if tag in s['tags']]

    def find_services_with_all_tags(self, tags):
        tags_set = set(tags)
        services = self.all_services

        return [s for s in services if tags_set.issuperset(set(s['tags']))]

    def find_services_with_label(self, label):

        return [s for s in self.all_services if s['label'] == label]

    def find_services_with_label_containing(self, label):

        return [s for s in self.all_services if label in s['label']]

    def find_first_service_with_label(self, label):
        services = self.find_services_with_label(label)

        return self.first_service_or_none(services)

    @property
    def all_services(self):
        return itertools.chain.from_iterable(self.services.values())

    @staticmethod
    def first_service_or_none(services):
        return None if not (services and len(services)) else services[0]