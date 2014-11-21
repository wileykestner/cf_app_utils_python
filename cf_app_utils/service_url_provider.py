from urlparse import ParseResult
from cf_app_utils.credentials_locator import CredentialsLocator
from cf_app_utils.service_locator import ServiceLocator


class ServiceURLProvider(object):

    @staticmethod
    def provider(services):
        assert services
        service_locator = ServiceLocator(services)
        credentials_locator = CredentialsLocator(service_locator)
        return ServiceURLProvider(credentials_locator)

    def __init__(self, credentials_locator):
        assert credentials_locator
        self.credentials_locator = credentials_locator

    def url_for_first_service_with_name(self, name, scheme=None):
        locator = self.credentials_locator
        find = locator.find_credentials_for_first_service_with_name
        credentials = find(name)
        if not credentials:
            return None

        if 'uri' in credentials:
            return credentials['uri']

        scheme = scheme or ''
        username = credentials.get('username', None)
        hostname = credentials.get('hostname', None)
        password = credentials.get('password', None)
        username_password = ''
        if username or password:
            username_password = "%s:%s@" % (username or '',
                                            password or '')
        user_pass_and_hostname = '%s%s' % (username_password, hostname)

        port = credentials.get('port', None)
        port = '' if not port else ':%s' % port
        netloc = '%s%s' % (user_pass_and_hostname, port)
        parse_result = ParseResult(scheme=scheme,
                                   netloc=netloc,
                                   path='',
                                   params='',
                                   query='',
                                   fragment='')
        return parse_result.geturl()
