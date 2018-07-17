import os, platform, re, shutil
import requests
import xbmc, xbmcgui, xbmcaddon

from .exceptions import WVError
from . import util

WV_SSD = {
    'Windows': 'ssd_wv.dll',
    'Linux': 'libssd_wv.so',
    'Darwin': 'libssd_wv.dylib'
}

WV_CDM = {
    'Windows': 'widevinecdm.dll',
    'Linux': 'libwidevinecdm.so',
    'Darwin': 'libwidevinecdm.dylib'
}
 
PLATFORMS = [
    'Windows64bit',
    'Windows32bit',
    'Darwinx86_64',
    'Linuxx86_64',
    'Linuxi386',
    'Linuxarmv7',
    'Linuxarmv8',
    'Linuxarm',
]

GIT_URL = 'https://raw.githubusercontent.com/matthuisman/decryptmodules/master/{0}/{1}/{2}'

ADDON_ID = 'inputstream.adaptive'

class WVHelper(object):
    @staticmethod
    def _get_ia():
        try:
            xbmc.executebuiltin('InstallAddon({})'.format(ADDON_ID), True)
            xbmc.executeJSONRPC('{{"jsonrpc":"2.0","id":1,"method":"Addons.SetAddonEnabled","params":{{"addonid":"{}","enabled":true}}}}'.format(ADDON_ID))
            return xbmcaddon.Addon(ADDON_ID)
        except:
            return None

    @staticmethod
    def supports_hls():
        addon = WVHelper._get_ia()
        return addon and int(addon.getAddonInfo('version')[0]) >= 2

    @staticmethod
    def require_widevine():
        def get_system_arch():
            system = platform.system()
            arch = platform.machine()

            if system == 'Windows':
                arch = platform.architecture()[0]

            elif 'armv' in arch:
                arm_version = re.search('\d+', arch.split('v')[1])
                if arm_version:
                    arch = 'armv' + arm_version.group()

            elif arch == 'arm':
                arch = 'armv8'

            elif arch == 'i686':
                arch = 'i386'

            if system == 'Linux' and xbmc.getCondVisibility('system.platform.android'):
                system = 'Android'

            if 'WindowsApps' in xbmc.translatePath('special://xbmcbin/'):
                system = 'UWP'

            return system, arch

        def has_ssd_wv():
            return os.path.exists(os.path.join(xbmc.translatePath(decrypt_path), WV_SSD[system]))

        def has_widevinecdm():
            return os.path.exists(os.path.join(xbmc.translatePath(decrypt_path), WV_CDM[system]))

        def remove_file(file_path):
            if os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.exists(file_path):
                os.remove(file_path)

        def get_widevinecdm():
            cdm_path = xbmc.translatePath(decrypt_path)
            filename = WV_CDM[system]
            download_path = os.path.join(cdm_path, filename)

            if not os.path.isdir(cdm_path):
                os.makedirs(cdm_path)
            else:
                remove_file(download_path)

            url = GIT_URL.format(system, arch, filename)
            progress_download(url, download_path, filename)
            os.chmod(download_path, 0755)

        def get_ssd_wv():
            cdm_path = xbmc.translatePath(decrypt_path)
            filename = WV_SSD[system]
            download_path = os.path.join(cdm_path, filename)

            if not os.path.isdir(cdm_path):
                os.makedirs(cdm_path)
            else:
                remove_file(download_path)

            paths = [os.path.join(addon_path, filename), os.path.join(addon_path, 'lib', filename), os.path.join(os.sep, 'usr', 'lib', filename)]
            for path in paths:
                if os.path.exists(path):
                    try:
                        shutil.copy(path, download_path)
                        os.chmod(download_path, 0755)
                        return
                    except:
                        continue

            url = GIT_URL.format(system, arch, filename)
            progress_download(url, download_path, filename)
            os.chmod(download_path, 0755)
            
        def progress_download(url, download_path, filename):
            res = requests.get(url, stream=True)
            res.raise_for_status()

            total_length = float(res.headers.get('content-length'))
            dp = xbmcgui.DialogProgress()
            dp.create("Installing DRM", "Downloading", url)

            with open(download_path, 'wb') as f:
                chunk_size = 1024
                downloaded = 0
                for chunk in res.iter_content(chunk_size=chunk_size):
                    f.write(chunk)
                    downloaded += len(chunk)
                    percent = int(downloaded*100/total_length)
                    if dp.iscanceled():
                        dp.close()
                        res.close()
                    dp.update(percent)

            dp.close()

        addon = WVHelper._get_ia()
        if not addon:
            raise WVError('Inputstream.adaptive add-on not found or not enabled.\
                        This add-on is required to play Widevine DRM content.')

        system, arch       =  get_system_arch()
        kodi_major_version = util.kodi_version()
        decrypt_path       = addon.getSetting('DECRYPTERPATH')
        addon_path         = xbmc.translatePath(addon.getAddonInfo('path')).decode("utf-8")

        error = None
        if system == 'UWP':
            error = 'Kodi Windows Store version does not support Widevine DRM playback.\nUse the Kodi installer from the Kodi website instead.'
        elif system == 'Android':
            if kodi_major_version >= 18:
                return
            else:
                error = 'Kodi 18 or higher required for Widevine DRM playback in Android.'
        elif 'aarch64' in arch:
            error = 'ARM 64bit does not support Widevine DRM playback. An OS with a 32-bit userspace is required. Try coreelec.org'
        # elif system == 'Linux':
        #     if kodi_major_version < 18 and arch in ['x86_64', 'i386']:
        #         error = 'Kodi 18 or higher required for Widevine DRM playback in Linux.'
        elif system == 'Windows':
            if kodi_major_version < 18:
                error = 'Kodi 18 or higher required for Widevine DRM playback in Windows.'
        elif system + arch not in PLATFORMS:
            error = 'This system (%s Kodi v%s) does not yet support Widevine Playback.' % (system + arch, kodi_major_version)
        elif kodi_major_version < 17:
            error = 'Kodi 17 or higher required for Widevine DRM playback.'

        if error:
            raise WVError(error)

        ver_slug = system + arch + addon.getAddonInfo('version')
        if ver_slug == addon.getSetting('_ver_slug') and has_ssd_wv() and has_widevinecdm():
            return

        try:
            get_ssd_wv()
            get_widevinecdm()
        except:
            raise WVError('There was an error installing Widevine. Please restart KODI and try again.')
        else:
            addon.setSetting('_ver_slug', ver_slug)