from urllib import urlencode
from urlparse import parse_qsl

from . import config
from .exceptions import RouterError

class Router(object):
    def __init__(self, base_url, controller, default=None):
        self._base_url = base_url
        self._controller = controller
        self._default = default.__name__ if default else ''

    def __call__(self, route):
        params = dict(parse_qsl(route[1:]))
        route = params.pop(config.ROUTE_TAG, self._default)

        if route.startswith('_'):
            raise RouterError("'{0}' route not allowed".format(route))

        try:
            func = getattr(self._controller, route)
        except:
            raise RouterError("'{0}' route not found".format(route))
        
        return func(params)

    def get(self, route, params=None, live=False):
        route = route.__name__
        if route.startswith('_'):
            raise RouterError("'{0}' route can not start with _".format(route))

        try:
            func = getattr(self._controller, route)
        except:
            raise RouterError("'{0}' route not found".format(route))

        if not params: params = {}
        params[config.ROUTE_TAG] = route

        _params = []
        for k in sorted(params):
            try: _params.append((k, unicode(params[k]).encode('utf-8')))
            except: _params.append((k,params[k]))

        url = "{0}?{1}".format(self._base_url, urlencode(_params))
        if live: url += "&_l=.pvr"

        return url