def rediscloud_service_credentials():
    return {'port': '15348',
            'hostname': 'my.redis.domain.com',
            'password': 'my-redis-password'}


def rediscloud_service():
    return {'name': 'my-redis-instance-name',
            'label': 'rediscloud',
            'plan': '25mb',
            'tags': ['redis',
                     'key-value',
                     'Data Stores',
                     'Data Store'],
            'credentials': rediscloud_service_credentials()}


def blue_service_one_credentials():
    return {'port': '851',
            'hostname': 'my.blue.one.com',
            'password': 'my-blue-one-password'}


def blue_service_two_credentials():
    return {'port': '852',
            'hostname': 'my.blue.two.com',
            'password': 'my-blue-two-password'}


def red_service_one_credentials():
    return {'port': '451',
            'hostname': 'my.red.one.com',
            'password': 'my-red-one-password'}


def blue_service_one():
    return {'name': 'blue-service-instance-one-name',
            'label': 'colorservice',
            'plan': '25mb',
            'tags': ['blue',
                     'color'],
            'credentials': blue_service_one_credentials()}


def blue_service_two():
    return {'name': 'blue-service-instance-two-name',
            'label': 'sillyservice',
            'plan': '25mb',
            'tags': ['blue',
                     'color'],
            'credentials': blue_service_two_credentials()}


def red_service_one():
    return {'name': 'red-service-instance-one-name',
            'label': 'colorservice',
            'plan': '25mb',
            'tags': ['red',
                     'color'],
            'credentials': red_service_one_credentials()}