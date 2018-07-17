import requests

from matthuisman.controller import Controller as BaseController

from . import config

class Controller(BaseController):
    def home(self, params):
        channels = self._get_channels()

        if params.get('play'):
            channel = channels[params['play']]
            channel['url'] = channel['_play_url']
            return self._view.play(channel)
        
        slugs = sorted(channels, key=lambda k: channels[k].get('channel', channels[k]['title']))
        items = [channels[slug] for slug in slugs]
        items.append({'title':'Settings', 'url': self._router.get(self.settings)})

        self._view.items(items, cache=False)

    def toggle_ia_hls(self, params):
        slug = params.get('slug')

        channels = self._get_channels()
        channel = channels[slug]

        ia_hls_enabled = self._addon.data.get('ia_hls_enabled', [])

        if slug in ia_hls_enabled:
            ia_hls_enabled.remove(slug)
            self._view.notification('Inputstream HLS Disabled', heading=channel['title'], icon=channel['images']['thumb'])
        else:
            ia_hls_enabled.append(slug)
            self._view.notification('Inputstream HLS Enabled', heading=channel['title'], icon=channel['images']['thumb'])

        self._addon.data['ia_hls_enabled'] = ia_hls_enabled
        self._view.refresh()

    def _get_channels(self):
        channels = {}

        url = config.M3U8_FILE
        func = lambda: requests.get(url).json()
        data = self._addon.cache.function(url, func, expires=config.CACHE_TIME)

        ia_hls_enabled = self._addon.data.get('ia_hls_enabled', [])

        for slug in data:
            channel = data[slug]

            info = {
                'title': channel['name'],
                'plot': channel.get('description',''),
                'mediatype': 'video',
            }

            context = []
            use_ia_hls = False
            url = channel['mjh_sub']

            if url.startswith('http'):
                use_ia_hls = slug in ia_hls_enabled

                if use_ia_hls:
                    url = channel['mjh_master']
                    context.append(["Disable Inputstream HLS", "XBMC.RunPlugin({0})".format(
                        self._router.get(self.toggle_ia_hls, {'slug': slug}))])
                else:
                    context.append(["Enable Inputstream HLS", "XBMC.RunPlugin({0})".format(
                        self._router.get(self.toggle_ia_hls, {'slug': slug}))])

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
                'vid_type': 'hls',
                'options': {'use_ia_hls': use_ia_hls, 'get_location': use_ia_hls, 'headers': channel.get('headers', {})},
            }

            if channel.get('channel'):
                item['channel'] = channel['channel']

            channels[slug] = item

        return channels