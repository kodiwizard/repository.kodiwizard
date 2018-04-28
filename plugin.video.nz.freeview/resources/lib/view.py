import requests, json, time, os

import router, config
from render import Render

class View(object):
    def __init__(self, router):
        self._router = router
        self._render = Render.get_render()

    def menu(self, params):
        items = []

        data = self._get_data()
        _ids = sorted(data, key=lambda k: data[k].get('channel', data[k]['name']))
        for _id in _ids:
            station = self._parse_station(_id, data[_id], True)
            items.append(station)

        self._render.items(items)

    def clear_cache(self, params):
        try:
            os.remove(config.CACHE_FILE)
        except:
            pass
            
        self._render.notifcation("Cached cleared.")

    def _get_data(self):
        try:
            with open(config.CACHE_FILE, 'r') as f:
                data = json.load(f)

            if data.pop('cached') <= time.time():
                raise Exception("Cache Expired")

            return data
        except:
            pass

        try:
            data = requests.get(config.DATA_FILE, timeout=3).json()
        except:
            return {}

        data['cached'] = time.time() + config.CACHE_TIME
        with open(config.CACHE_FILE, 'w') as f:
            f.write(json.dumps(data, separators=(',',':')))
        data.pop('cached')

        return data

    def _parse_station(self, _id, station, is_menu=False):
        image = station.get('logo', None)

        info = {
            'title': station['name'],
            'originaltitle': station['name'],
            'plot': station.get('description',''),
            'plotoutline': station.get('description',''),
            'mediatype': 'video',
        }

        data = {
            'title': station['name'],
            'url': station.get('url'),
            'images': {'thumb': image, 'icon': image},
            'playable': True,
            'info': info,
            'video': station.get('video',{}),
            'audio': station.get('audio',{}),
        }

        if is_menu:
            data['url'] = self._router.get_route({'action': 'play', 'id': _id})

        return data

    def play(self, params):
        data = self._get_data()
        for _id in data:
            if _id == params.get('id'):
                station = self._parse_station(_id, data[_id])
                return self._render.play(station)

        self._render.notifcation("Could not find that station.")