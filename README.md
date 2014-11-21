cf_app_utils_python
===================

Creates URLS for services bound to your app deployed on Cloud Foundry.  The
service information is stored in the `VCAP_SERVICES` json dictionary in the
local environment of your running app process.

This library uses
the [v2 json format]
(http://docs.run.pivotal.io/devguide/deploy-apps/environment-variable.html)
of `VCAP_SERVICES`.

Example usage:

```
import os, json
from cf_app_utils.service_url_provider import ServiceURLProvider

services = json.loads(os.environ['VCAP_SERVICES'])
service_url_provider = ServiceURLProvider.provider(services=services)

database_url = service_url_provider.url_for_first_service_with_name('elephantsql')
redis_url = service_url_provider.url_for_first_service_with_name('rediscloud', scheme='redis')

```
