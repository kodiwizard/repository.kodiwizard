import os

import requests

import xbmc, xbmcgui, xbmcplugin

from .util import header_string
from .wvhelper import WVHelper

class View(object):
    def __init__(self, addon, handle):
        self._addon = addon
        self._handle = handle
        self._dialog = xbmcgui.Dialog()
        self._resolved = False

    def refresh(self):
        xbmc.executebuiltin('Container.Refresh')
        self._resolved = True

    def notification(self, message, heading=None, icon=None, time=3000):
        if not heading: heading = self._addon.name
        if not icon: icon = os.path.join(self._addon.path, 'icon.png')

        self._dialog.notification(heading, message, icon, time)

    def get_input(self, message, default='', hidden=False):
        return self._dialog.input(message, default)

    def dialog(self, message, heading=None):
        if not heading: heading = self._addon.name

        lines = list()
        for line in str(message).split('\n'):
            lines.append(line.strip())

        return self._dialog.ok(heading, *lines)

    def dialog_yes_no(self, message, heading=None, yeslabel=None, nolabel=None):
        if not heading: heading = self._addon.name

        lines = list()
        for line in str(message).split('\n'):
            lines.append(line.strip())

        return self._dialog.yesno(heading, *lines, yeslabel=yeslabel, nolabel=nolabel)

    def play(self, item):
        options       = item.pop('options', {})
        headers       = options.get('headers', {})
        cookies       = options.get('cookies', {})
        fetch_cookies = options.get('fetch_cookies', False)
        get_location  = options.get('get_location', False)
        use_ia_hls    = options.get('use_ia_hls', False)
        position      = options.get('position', None)

        if fetch_cookies:
            r = requests.get(item['url'], headers=headers, allow_redirects=False)
            cookies.update(r.cookies.get_dict())

        if get_location:
            r = requests.get(item['url'], headers=headers, allow_redirects=False)
            item['url'] = r.headers['location']

        _headers = header_string(headers, cookies)
        if item['url'].startswith('http'):
            item['url'] += '|' + _headers

        li = self._create_list_item(item)

        if position != None:
            li.setProperty('ResumeTime', str(position))
            li.setProperty('TotalTime', str(position))

        if item.get('vid_type') == 'hls' and use_ia_hls and WVHelper.supports_hls():
            li.setProperty('inputstreamaddon', 'inputstream.adaptive')
            li.setProperty('inputstream.adaptive.manifest_type', 'hls')
            if _headers: 
                li.setProperty('inputstream.adaptive.stream_headers', _headers)
                li.setProperty('inputstream.adaptive.license_key', '|' + _headers)

        elif item.get('vid_type') == 'widevine':
            WVHelper.require_widevine()

            li.setProperty('inputstreamaddon', 'inputstream.adaptive')
            li.setProperty('inputstream.adaptive.manifest_type', 'mpd')
            li.setProperty('inputstream.adaptive.license_type', 'com.widevine.alpha')
            if _headers: 
                li.setProperty('inputstream.adaptive.stream_headers', _headers)
            li.setProperty('inputstream.adaptive.license_key', '{0}|Content-Type=application/octet-stream&{1}|R{{SSM}}|'.format(item.get('vid_key'), _headers))

        if self._handle < 1:
            xbmc.Player().play(li.getPath(), listitem=li)
        else:
            xbmcplugin.setResolvedUrl(self._handle, True, li)
            self._resolved = True

    def _create_list_item(self, data):
        li = xbmcgui.ListItem(data.get('title'))
        if data.get('url'):
            li.setPath(data['url'])

        if data.get('playable', False):
            li.setProperty('IsPlayable', 'true')

        images = data.get('images', {})
        if not images.get('banner'):
            images['banner'] = images.get('fanart')
        if not images.get('fanart'):
            images['fanart'] = os.path.join(self._addon.path, 'fanart.jpg')
        if not images.get('thumb'):
            images['thumb'] = os.path.join(self._addon.path, 'icon.png')

        info =  data.get('info',{})
        if not info.get('title'):
            info['title'] = data.get('title')
        if not info.get('plot'):
            info['plot'] = info['title']

        li.setArt(images)
        li.setInfo('video', info)
        li.addStreamInfo('video', data.get('video',{}))
        li.addStreamInfo('audio', data.get('audio',{}))

        contexts = []
        for context in data.get('context', []):
            contexts.append((context[0], context[1]))

        li.addContextMenuItems(contexts)
        return li

    def items(self, items=[], content='videos', title=None, history=True, cache=True):
        for item in items:
            li = self._create_list_item(item)
            is_folder = item.get('is_folder', item.get('url') is not None and not item.get('playable', False))
            xbmcplugin.addDirectoryItem(self._handle, item.get('url'), li, is_folder)

        if content: xbmcplugin.setContent(self._handle, content)
        if title: xbmcplugin.setPluginCategory(self._handle, title)

        xbmcplugin.endOfDirectory(self._handle, updateListing=not history, cacheToDisc=cache)
        self._resolved = True

    def close(self, result=False):
        if not self._resolved and self._handle > 0:
            xbmcplugin.endOfDirectory(self._handle, succeeded=result, updateListing=False, cacheToDisc=False)
            self._resolved = True