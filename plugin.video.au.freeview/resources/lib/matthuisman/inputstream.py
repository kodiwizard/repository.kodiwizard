import os, platform, re, shutil
import xbmc, xbmcaddon

from . import gui, settings
from .log import log
from .constants import IA_ADDON_ID, IA_VERSION_KEY, IA_HLS_MIN_VER, IA_MPD_MIN_VER, IA_MODULES_URL
from .language import _
from .util import get_kodi_version

class InputstreamItem(object):
    manifest_type = ''
    license_type  = ''
    license_key   = ''
    mimetype      = ''

    def check(self):
        return False

class HLS(InputstreamItem):
    manifest_type = 'hls'
    mimetype      = 'application/vnd.apple.mpegurl'

    def check(self):
        return settings.getBool('use_ia_hls', True) and supports_hls()

class MPD(InputstreamItem):
    manifest_type = 'mpd'
    mimetype      = 'application/dash+xml'

    def check(self):
        return supports_mpd()

class Playready(InputstreamItem):
    manifest_type = 'ism'
    license_type  = 'com.microsoft.playready'
    mimetype      = 'application/vnd.ms-sstr+xml'

    def check(self):
        return supports_playready()

class Widevine(InputstreamItem):
    manifest_type = 'mpd'
    license_type  = 'com.widevine.alpha'
    mimetype      = 'application/dash+xml'

    def __init__(self, license_key=None, content_type='application/octet-stream', challenge='R{SSM}', response=''):
        self.license_key  = license_key
        self.content_type = content_type
        self.challenge    = challenge
        self.response     = response

    def check(self):
        return install_widevine()

class Error(Exception):
    pass

def get_ia_addon():
    try:
        xbmc.executebuiltin('InstallAddon({})'.format(IA_ADDON_ID), True)
        xbmc.executeJSONRPC('{{"jsonrpc":"2.0","id":1,"method":"Addons.SetAddonEnabled","params":{{"addonid":"{}","enabled":true}}}}'.format(IA_ADDON_ID))
        return xbmcaddon.Addon(IA_ADDON_ID)
    except:
        return None

def open_settings():
    ia_addon = get_ia_addon()
    if not ia_addon:
        raise Error(_.IA_NOT_FOUND)
    ia_addon.openSettings()

def supports_hls():
    ia_addon = get_ia_addon()
    return bool(ia_addon and int(ia_addon.getAddonInfo('version')[0]) >= IA_HLS_MIN_VER)

def supports_mpd():
    ia_addon = get_ia_addon()
    return bool(ia_addon and int(ia_addon.getAddonInfo('version')[0]) >= IA_MPD_MIN_VER)

def supports_playready():
    ia_addon = get_ia_addon()
    return bool(ia_addon and get_kodi_version() > 17 and xbmc.getCondVisibility('system.platform.android'))

def install_widevine(reinstall=False):
    ia_addon = get_ia_addon()
    if not ia_addon:
        raise Error(_.IA_NOT_FOUND)

    system, arch = _get_system_arch()
    kodi_version = get_kodi_version()
    ver_slug     = system + arch + str(kodi_version) + ia_addon.getAddonInfo('version')

    if not reinstall and ver_slug == ia_addon.getSetting(IA_VERSION_KEY):
        return True

    from .session import Session

    widevine = Session().get(IA_MODULES_URL).json()['widevine']

    if kodi_version < 18:
        raise Error(_(_.IA_KODI18_REQUIRED, system=system))

    elif system == 'Android':
        return True

    elif system == 'UWP':
        raise Error(_.IA_UWP_ERROR)

    elif 'aarch64' in arch:
        raise Error(_.IA_AARCH64_ERROR)

    elif system + arch not in widevine['platforms']:
        raise Error(_(_.IA_NOT_SUPPORTED, system=system, arch=arch, kodi_version=kodi_version))

    decryptpath = xbmc.translatePath(ia_addon.getSetting('DECRYPTERPATH')).decode("utf-8")
    src, dst    = widevine['platforms'][system + arch]
    url         = widevine['base_url'] + src
    wv_path     = os.path.join(decryptpath, dst)

    try:
        if not os.path.isdir(decryptpath):
            os.makedirs(decryptpath)

        _download(url, wv_path)
        os.chmod(wv_path, 0755)
    except Exception as e:
        e.message = _.IA_ERROR_INSTALLING
        raise

    ia_addon.setSetting(IA_VERSION_KEY, ver_slug)
    gui.ok(_.IA_WV_INSTALL_OK)
    return True

def _get_system_arch():
    system = platform.system()
    arch   = platform.machine()

    if system == 'Windows':
        arch = platform.architecture()[0]

    elif 'arm' in arch:
        arch = 'armv7'

    elif arch == 'i686':
        arch = 'i386'

    if system == 'Linux' and xbmc.getCondVisibility('system.platform.android'):
        system = 'Android'

    if 'WindowsApps' in xbmc.translatePath('special://xbmcbin/'):
        system = 'UWP'

    return system, arch

def _download(url, dst_path):
    from .session import Session
    
    resp = Session().get(url, stream=True)
    resp.raise_for_status()

    total_length = float(resp.headers.get('content-length'))

    with gui.progress(_(_.IA_DOWNLOADING_FILE, url=url), heading=_.IA_WIDEVINE_DRM) as progress:
        if os.path.exists(dst_path):
            os.remove(dst_path)

        with open(dst_path, 'wb') as f:
            chunk_size = 1024
            downloaded = 0
            for chunk in resp.iter_content(chunk_size=chunk_size):
                f.write(chunk)
                downloaded += len(chunk)
                percent = int(downloaded*100/total_length)

                if progress.iscanceled():
                    progress.close()
                    resp.close()

                progress.update(percent)