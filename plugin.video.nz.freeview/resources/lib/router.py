try:
    from urlparse import parse_qsl #python2
    from urllib import urlencode
except:
    from urllib.parse import parse_qsl #python3
    from urllib.parse import urlencode

from view import View

class Router(object):
    def __init__(self, base_url):
        self._view = View(self)
        self._base_url = base_url

    def route(self, paramstring):
        params = dict(parse_qsl(paramstring[1:]))
        action = params.get('action')
        if action == 'play':
            self._view.play(params)
        elif action == 'clear_cache':
            self._view.clear_cache(params)
        else:
            self._view.menu(params)

    def get_route(self, params):
        return self._base_url + "?" + urlencode(params)
        