#######################################################################
# Import Modules Section
import xbmc, xbmcaddon, xbmcgui, xbmcplugin, base64
import os
#######################################################################

#######################################################################
# Set this to True to see the menu on non-android devices for dev work
DEVELOPER           = False
#######################################################################

#######################################################################
# Primary Addon Variables
AddonID             = xbmcaddon.Addon().getAddonInfo('id')
ADDON               = xbmcaddon.Addon(id=AddonID)
HOME                = xbmc.translatePath('special://home/')
ADDONS              = os.path.join(HOME, 'addons')
USERDATA            = os.path.join(HOME, 'userdata')
ADDON_DATA          = xbmc.translatePath(os.path.join(USERDATA, 'addon_data'))
ownAddon            = xbmcaddon.Addon(id=AddonID)
URL                 = base64.b64decode(b'aHR0cDovL3RlYW14a29kaS50ay9hcGtzLw==')
NEWSURL             = base64.b64decode(b'aHR0cDovL3RlYW14a29kaS50ay9hcGtzL25ld3MueG1s')
ADDONTITLE          = base64.b64decode(b'VGVhbSBYIEFwayBXaXphcmQ=')
#######################################################################

#######################################################################
# Filename Variables 
BASEURL             = URL
EMU_FILE            = BASEURL + base64.b64decode(b'ZW11bGF0b3JzLnR4dA==')
KODI_FILE           = BASEURL + base64.b64decode(b'a29kaS50eHQ=')
LIVETV_FILE         = BASEURL + base64.b64decode(b'bGl2ZXR2LnR4dA==')
VOD_FILE            = BASEURL + base64.b64decode(b'dm9kLnR4dA==')
SECURITY_FILE       = BASEURL + base64.b64decode(b'c2VjdXJpdHkudHh0')
TOOLS_FILE          = BASEURL + base64.b64decode(b'dG9vbHMudHh0')
#######################################################################

#######################################################################
# Theme Variables
FONTHEADER          = base64.b64decode(b'Rm9udDE0')
FANART              = xbmc.translatePath(os.path.join('special://home/addons/' + AddonID, 'fanart.jpg'))
ICON                = xbmc.translatePath(os.path.join('special://home/addons/' + AddonID, 'icon.png'))
ART                 = xbmc.translatePath(os.path.join('special://home/addons/' + AddonID, 'resources/art/'))
#######################################################################

#######################################################################
ADDONDATA           = os.path.join(USERDATA, 'addon_data', AddonID)
dialog              = xbmcgui.Dialog()
DIALOG              = xbmcgui.Dialog()
dp                  = xbmcgui.DialogProgress()
DP                  = xbmcgui.DialogProgress()
LOG                 = xbmc.translatePath('special://logpath/')
PLUGIN              = os.path.join(ADDONS, AddonID)
skin                = xbmc.getSkinDir()
USER_AGENT          = base64.b64decode(b'TW96aWxsYS81LjAgKFdpbmRvd3M7IFU7IFdpbmRvd3MgTlQgNS4xOyBlbi1HQjsgcnY6MS45LjAuMykgR2Vja28vMjAwODA5MjQxNyBGaXJlZm94LzMuMC4z')
#######################################################################