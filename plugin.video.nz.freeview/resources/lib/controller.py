from matthuisman.globs import config
from matthuisman.controller import Controller as BaseController

class Controller(BaseController):
    def home(self, params):
        channels = self._get_channels()

        if params.get('play'):
            channel = channels[params['play']]
            channel['url'] = channel['_play_url']
            return self._view.play(channel)
        
        slugs = sorted(channels, key=lambda k: channels[k].get('channel', channels[k]['title']))
        items = [channels[slug] for slug in slugs]

        self._view.items(items, cache=False)

    def toggle_ia(self, params):
        slug = params.get('slug')

        channels = self._get_channels()
        channel = channels[slug]

        ia_enabled = config.SETTINGS.get('ia_enabled', [])

        if slug in ia_enabled:
            ia_enabled.remove(slug)
            self._view.notification('Inputstream Disabled', heading=channel['title'], icon=channel['images']['thumb'])
        else:
            ia_enabled.append(slug)
            self._view.notification('Inputstream Enabled', heading=channel['title'], icon=channel['images']['thumb'])

        config.SETTINGS.set('ia_enabled', ia_enabled)
        self._view.refresh()

    def _get_channels(self):
        channels = {}

        data = config.CACHE.get(config.M3U8_FILE)
        if not data:
            data = self._api.get(config.M3U8_FILE).json()
            config.CACHE.set(config.M3U8_FILE, data, expiry=config.CACHE_TIME)

        ia_enabled = config.SETTINGS.get('ia_enabled', [])

        for slug in data:
            channel = data[slug]

            info = {
                'title': channel['name'],
                'plot': channel.get('description',''),
                'mediatype': 'video',
            }

            context = []
            use_ia = False

            url = channel['mjh_sub']
            if url.startswith('http'):
                use_ia = slug in ia_enabled

                if use_ia:
                    url = channel['mjh_master']
                    context.append(["Disable Inputstream", "XBMC.RunPlugin({0})".format(
                        self._router.get(self.toggle_ia, {'slug': slug}))])
                else:
                    context.append(["Enable Inputstream", "XBMC.RunPlugin({0})".format(
                        self._router.get(self.toggle_ia, {'slug': slug}))])

            item = {
                'title': channel['name'],
                'images': {'thumb': channel.get('logo', None)},
                'url': self._router.get(self.home, {'play': slug}, live=True),
                '_play_url': url,
                'playable': True,
                'info': info,
                'video': channel.get('video',{}),
                'audio': channel.get('audio',{}),
                'context': context,
                'options': {'type': 'hls' if use_ia else '', 'get_location': use_ia, 'headers': channel.get('headers', {})},
            }

            if channel.get('channel'):
                item['channel'] = channel['channel']

            channels[slug] = item

        return channels