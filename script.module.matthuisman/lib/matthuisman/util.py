import hashlib
import logging
from urllib import quote

import xbmc, xbmcaddon

from .exceptions import ComsError

def hash_6(value, default=None):
    if not value:
        return default

    h = hashlib.md5(str(value))
    return h.digest().encode('base64')[:6]

def kodi_version():
    return int(xbmc.getInfoLabel("System.BuildVersion").split('.')[0])

def header_string(headers=None, cookies=None):
    headers = {} if headers == None else headers
    cookies = {} if cookies == None else cookies
    string = ''
    
    for header in headers:
        value = headers[header]
        if value: 
            string += '{0}={1}&'.format(header, quote(value))

    if cookies:
        string += 'Cookie='
        for cookie in cookies:
            string += '{0}%3D{1}; '.format(cookie, quote(cookies[cookie]))

    return string.strip('&')

def process_brightcove(program_data):
    try:
        error = program_data[0]['error_code']
    except:
        error = None

    if error:
        raise ComsError('Brightcove returned the following error: {0}'.format(error))

    videos = []
    for source in program_data['sources']:
        if not source.get('src'):
            continue

        if source.get('container') == 'MP4':
            videos.append({
                'url': source['src'], 
                '_sort': source.get('avg_bitrate', source.get('height')),
            })
        elif 'key_systems' in source and 'com.widevine.alpha' in source['key_systems']:
            videos.append({
                'url': source['src'],
                'vid_type': 'widevine', 
                'vid_key': source['key_systems']['com.widevine.alpha']['license_url'],
            })

    if videos:
        videos = sorted(videos, key=lambda x: x.get('_sort'), reverse=True)
        video = videos[0]
        video.pop('_sort', None)
        return video

    raise ComsError('Could not find a source from brightcove')

class LoggerHandler(logging.StreamHandler):
    LEVELS = {
        logging.DEBUG    : xbmc.LOGDEBUG,
        logging.INFO     : xbmc.LOGINFO,
        logging.WARNING  : xbmc.LOGWARNING,
        logging.ERROR    : xbmc.LOGERROR,
        logging.CRITICAL : xbmc.LOGFATAL,
    }

    def emit(self, record):
        msg = self.format(record)

        if isinstance(msg, unicode):
            msg = msg.encode('utf-8')

        level = self.LEVELS.get(record.levelno, xbmc.LOGDEBUG)
        xbmc.log(msg, level)

log = logging.getLogger(xbmcaddon.Addon().getAddonInfo('id'))
handler = LoggerHandler()
formatter = logging.Formatter('mjh_log[%(name)s] %(message)s')
handler.setFormatter(formatter)
log.addHandler(handler)
log.setLevel(logging.DEBUG)

_NOARG = object()